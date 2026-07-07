#!/usr/bin/env python3
"""Validate SKILL.md frontmatter and directory layout for all skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DECISIONS_MD = REPO_ROOT / "docs" / "discuss" / "DECISIONS.md"
README_MD = REPO_ROOT / "README.md"
DISCUSS_DIR = REPO_ROOT / "docs" / "discuss"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SKIP_DIRS = {"template", "_template"}

PIPELINE_STAGES = {"exploring", "deciding", "ready-for-implementation", "blocked"}
ID_PATTERN = re.compile(r"(?:INV|ORD|EXP)-\d+[a-z]?")
SKILLS_REF_PATTERN = re.compile(r"skills/([a-z0-9][a-z0-9-]*)/")


def parse_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing YAML frontmatter (must start with ---)")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("unclosed YAML frontmatter")
    meta = yaml.safe_load(parts[1])
    if not isinstance(meta, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return meta


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]

    try:
        meta = parse_frontmatter(skill_md)
    except (yaml.YAMLError, ValueError) as exc:
        return [f"{skill_dir.name}: {exc}"]

    name = meta.get("name")
    description = meta.get("description")

    if not name or not isinstance(name, str):
        errors.append(f"{skill_dir.name}: 'name' is required in frontmatter")
    elif len(name) > 64:
        errors.append(f"{skill_dir.name}: 'name' exceeds 64 characters")
    elif not NAME_PATTERN.match(name):
        errors.append(f"{skill_dir.name}: 'name' must be lowercase alphanumeric with hyphens")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: directory name must match name '{name}'")

    if not description or not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_dir.name}: 'description' is required and must be non-empty")
    elif len(description) > 1024:
        errors.append(f"{skill_dir.name}: 'description' exceeds 1024 characters")

    body_lines = skill_md.read_text(encoding="utf-8").splitlines()
    if len(body_lines) > 600:
        errors.append(f"{skill_dir.name}: SKILL.md is very long ({len(body_lines)} lines); consider references/")

    return errors


def _extract_first_yaml_block(text: str) -> str | None:
    """Return the body of the first ```yaml fenced block, or None."""
    match = re.search(r"```yaml\n(.*?)\n```", text, re.DOTALL)
    return match.group(1) if match else None


def _exp_table_status(decisions_text: str) -> dict[str, str]:
    """Map each EXP id in DECISIONS to its 状态 cell (last column of its row)."""
    status: dict[str, str] = {}
    for line in decisions_text.splitlines():
        if not line.lstrip().startswith("| EXP-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        exp_id = cells[0]
        if ID_PATTERN.fullmatch(exp_id):
            status[exp_id] = cells[-1]
    return status


def _sync_section_ids(round_text: str) -> set[str]:
    """IDs appearing in any 'DECISIONS 同步状态' section of a round file."""
    ids: set[str] = set()
    in_section = False
    for line in round_text.splitlines():
        if line.startswith("#"):
            in_section = "DECISIONS 同步状态" in line
            continue
        if in_section and line.lstrip().startswith("|"):
            ids.update(ID_PATTERN.findall(line))
    return ids


def validate_cross_artifact() -> list[str]:
    """Cross-artifact consistency checks (C1–C4); see docs/discuss/15-*.md."""
    errors: list[str] = []

    if not DECISIONS_MD.is_file():
        return [f"cross-artifact: DECISIONS.md not found: {DECISIONS_MD}"]
    decisions_text = DECISIONS_MD.read_text(encoding="utf-8")

    # C1: pipeline-state block present with required fields + valid stage.
    pipeline_state: dict | None = None
    yaml_body = _extract_first_yaml_block(decisions_text)
    if yaml_body is None:
        errors.append("cross-artifact[C1]: DECISIONS.md missing ```yaml``` pipeline-state block")
    else:
        try:
            block = yaml.safe_load(yaml_body)
        except yaml.YAMLError as exc:
            block = None
            errors.append(f"cross-artifact[C1]: pipeline-state block is not valid YAML: {exc}")
        if isinstance(block, dict) and isinstance(block.get("pipeline-state"), dict):
            pipeline_state = block["pipeline-state"]
            for field in ("stage", "status", "pending_exp"):
                if field not in pipeline_state:
                    errors.append(f"cross-artifact[C1]: pipeline-state missing '{field}'")
            stage = pipeline_state.get("stage")
            if stage is not None and stage not in PIPELINE_STAGES:
                errors.append(
                    f"cross-artifact[C1]: pipeline-state.stage '{stage}' not in {sorted(PIPELINE_STAGES)}"
                )
            if "pending_exp" in pipeline_state and not isinstance(pipeline_state["pending_exp"], list):
                errors.append("cross-artifact[C1]: pipeline-state.pending_exp must be a list")
        elif yaml_body is not None:
            errors.append("cross-artifact[C1]: first ```yaml``` block has no 'pipeline-state' mapping")

    # C2: each pending_exp id exists in the EXP table and is still open.
    exp_status = _exp_table_status(decisions_text)
    if pipeline_state is not None and isinstance(pipeline_state.get("pending_exp"), list):
        for exp_id in pipeline_state["pending_exp"]:
            if exp_id not in exp_status:
                errors.append(
                    f"cross-artifact[C2]: pending_exp '{exp_id}' has no row in §待验证尝试 table"
                )
                continue
            cell = exp_status[exp_id].lower()
            if "passed" in cell or "aborted" in cell:
                errors.append(
                    f"cross-artifact[C2]: pending_exp '{exp_id}' is marked closed (passed/ABORTED) in EXP table"
                )

    # C3: skills/* <-> README index, bidirectional.
    skill_names = {
        p.name
        for p in SKILLS_DIR.iterdir()
        if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")
    } if SKILLS_DIR.is_dir() else set()
    if README_MD.is_file():
        readme_text = README_MD.read_text(encoding="utf-8")
        referenced = set(SKILLS_REF_PATTERN.findall(readme_text))
        for name in sorted(skill_names - referenced):
            errors.append(f"cross-artifact[C3]: skill '{name}' not referenced in README.md")
        for name in sorted(referenced - skill_names):
            errors.append(f"cross-artifact[C3]: README.md references skills/{name}/ but no such skill dir")
    else:
        errors.append(f"cross-artifact[C3]: README.md not found: {README_MD}")

    # C4: every id in a round file's 同步状态 section must appear somewhere in DECISIONS.md.
    known_ids = set(ID_PATTERN.findall(decisions_text))
    for round_md in sorted(DISCUSS_DIR.glob("[0-9][0-9]-*.md")):
        round_text = round_md.read_text(encoding="utf-8")
        for rid in sorted(_sync_section_ids(round_text)):
            if rid not in known_ids:
                errors.append(
                    f"cross-artifact[C4]: {round_md.name} 同步状态 references '{rid}' absent from DECISIONS.md"
                )

    return errors


def main(argv: list[str]) -> int:
    targets = argv[1:] if len(argv) > 1 else None

    if not SKILLS_DIR.is_dir():
        print(f"error: skills directory not found: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(
        p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")
    )

    if targets:
        skill_dirs = [SKILLS_DIR / t for t in targets]
        missing = [d for d in skill_dirs if not d.is_dir()]
        if missing:
            for d in missing:
                print(f"error: skill not found: {d.name}", file=sys.stderr)
            return 1

    if not skill_dirs:
        print("warning: no skills found under skills/", file=sys.stderr)
        return 0

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    # Cross-artifact checks are repo-global; run only on a full validation (no targets).
    cross_checked = targets is None
    if cross_checked:
        all_errors.extend(validate_cross_artifact())

    if all_errors:
        print("validation failed:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    suffix = " + cross-artifact (C1–C4)" if cross_checked else ""
    print(f"ok: {len(skill_dirs)} skill(s) validated{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
