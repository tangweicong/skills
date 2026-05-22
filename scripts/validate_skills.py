#!/usr/bin/env python3
"""Validate SKILL.md frontmatter and directory layout for all skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SKIP_DIRS = {"template", "_template"}


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

    if all_errors:
        print("validation failed:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"ok: {len(skill_dirs)} skill(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
