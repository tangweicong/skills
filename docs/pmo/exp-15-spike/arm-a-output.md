<!-- EXP-15 臂 A（现状格式）原始产出 · 独立上下文 subagent · 2026-08-27 · 逐字存档供独立复核，父 agent 未编辑正文 -->

# ORD-43 升格为「跨轮讨论覆盖地图」（J-3）· 多专家设计分析

## Step 1 · 轻量框定（查证前问题清单）

| # | 待查问题 | 为什么必须先答 |
|---|----------|----------------|
| Q1 | 结构化清单在"防遗漏"上是否有实证效果？**边界条件**是什么（什么任务类型有效、什么形态会失效）？ | 用户诉求的核心动词就是"避免遗漏"。若清单类机制在开放式任务上无效，整个提案的收益侧就不成立 |
| Q2 | 清单的**形态纪律**是什么（长度 / 触发点 / 谁来读）？失效时长什么样？ | ORD-43 已记录的失败模式是"沦为官僚表格"。需要外部纪律来定义"升格但不膨胀"的具体边界 |
| Q3 | 在讨论**早期**确定一份多维度大纲，会不会**锚定**后续思考、反而制造新的遗漏？ | 这是提案的自反风险：为防遗漏而引入的机制本身可能收窄解空间 |
| Q4 | 「跨轮维护」这一属性本身的**维护经济学**如何？同类工件（追溯矩阵）的实测成本与衰减规律？ | 直接对撞本项目"降低维持秩序所需能量"这条最高杠杆原则 |
| Q5 | 对**非专家**用户，外部结构化脚手架是净帮助还是净负担？**随时间**如何变化？ | 用户明确把"人的非专业性"作为立项理由。若脚手架的收益随时间反转，"持续跨轮"这个设计就直接错了 |

## Step 2 · 已查证事实（共享证据基底 · 三视角共用）

**清单有效性与边界（Q1）**

- **F1 · 清单在规程化任务上有强正面证据**——WHO 19 项手术安全清单，8 家医院 7688 例：住院死亡率 **1.5%→0.8%（P=0.003）**，并发症 **11.0%→7.0%（P<0.001）**。[NEJM 2009](https://www.nejm.org/doi/full/10.1056/NEJMsa0810119)
- **F2 · 同一清单在强制推行下复制失败**——Ontario 101 家医院、前后各约 10.7 万例：调整后死亡风险 0.71%→0.65%（**OR 0.91, 95% CI 0.80–1.03, P=0.13**）、并发症 3.86%→3.82%（**OR 0.97, P=0.29**），**均不显著**。作者结论："as currently implemented, surgical safety checklists did not result in improved patient outcomes."[ICES / NEJM 2014](https://www.ices.on.ca/publications/journal-articles/introduction-of-surgical-safety-checklists-in-ontario-canada/) · [doi:10.1056/nejmsa1308261](https://doi.org/10.1056/nejmsa1308261)
  → **F1+F2 的联合读法：效果不在清单本身，在实施形态。**

**清单的形态纪律与失效形态（Q2）**

- **F3 · 硬性形态规则**（Boorman/Gawande）——① 必须定义 **pause point**（何时用）；② **DO-CONFIRM（先做后核）** 与 READ-DO（照着做）二选一；③ **5–9 项**（"the limit of working memory"）；④ 只放 **killer items**（"最危险被跳过、却又确实常被忽略"的步骤）；⑤ 一页、无杂色。超过 **60–90 秒**人开始 shortcutting，**反而漏步**。[joelhooks · Checklist Manifesto 摘录](https://joelhooks.com/the-checklist-manifesto/)
- **F4 · 复杂问题用的不是任务清单，是沟通清单**——Gawande 三分法 simple / complicated / **complex**（结果高度不确定、专业能力必要但不充分）。complex 问题上有效的是 **communication checklist**（建筑业 submittal schedule 为原型）：**它不规定怎么解决，只规定"到某个时点、哪些人必须就哪个方面对话一次"**。[tosummarise 书摘](https://www.tosummarise.com/book-summary-the-checklist-manifesto-by-atul-gawande/) · [grahammann 书摘](https://grahammann.net/book-notes/the-checklist-manifesto-atul-gawande)
- **F5 · 清单疲劳 / 非自愿自动化**——清单增殖后使用者滑向 tick-box：**在打勾的同时并未真的核对**，该现象被论证为"工作系统诱发的安全风险"；从业者自陈归因于**态度 + 糟糕的设计**，并给出设计判据："Checklists should be comprehensive but **not too detailed**. Otherwise, it can lead to checklist fatigue."[JECT 2024](https://ject.edpsciences.org/articles/ject/full_html/2024/01/ject230046/ject230046.html) · [doi:10.1258/095148405774518615](https://doi.org/10.1258/095148405774518615)

**记法的认知代价与锚定风险（Q3）**

- **F6 · 两个关键维度 + 探索式设计的画像**（Green 认知维度框架）——**viscosity = resistance to change**（分 repetition 型与 **knock-on 型**：改一处需连带改多处以恢复一致）；**premature commitment = constraints on the order of doing things**（被迫在拿到信息之前做决定）。原文："**The most demanding activity is exploratory design** … Viscosity has to be as low as possible, premature commitment needs to be reduced, visibility must be high."另有 **provisionality**（对标记的承诺程度：能否草稿式、what-if 式地记）。[CT2001](https://www.cl.cam.ac.uk/~afb21/publications/CT2001.pdf) · [doi:10.1145/345513.345233](https://doi.org/10.1145/345513.345233)
- **F7 · 抽象是有代价的止痛药**——"One way to reduce viscosity is to introduce abstractions, but that **will always require an abstraction manager** … and some **early commitment to choose which abstractions to define**. The abstractions themselves may then become viscous, introduce hidden dependencies."[doi:10.1145/345513.345233](https://doi.org/10.1145/345513.345233)
- **F8 · 设计固着**（Jansson & Smith 1991）——给工程师一个**被明确标注了缺陷的**示例，专家与新手**都会把示例的关键特征复制进自己的方案**；定义为"blind, sometimes counterproductive adherence to a limited set of ideas"。关键细节：给示例**不减少产出数量**（fluency 不变），减少的是**解空间宽度**。[Design Studies 1991](https://www.sciencedirect.com/science/article/abs/pii/0142694X9190003F) · [DRS 复现论文](https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=1716&context=drs-conference-papers)

**跨件覆盖工件的维护经济学（Q4）**

- **F9 · 手工维护的追溯矩阵普遍不回本**——Cockburn："在这行 30 年 … **从没见过一张追溯矩阵回本**"；另有实测项目"建立+保鲜的人力成本高到客户把追溯要求从合同里删掉"。工具厂商侧亦承认：需求变化快过手工更新速度时 RTM 的影响分析价值即退化，并把"**维护负担导致团队把更新推迟到项目结束**"直接列为"该工件已不再发挥作用"的判据。[InfoQ](https://www.infoq.com/news/2008/06/agile-traceability-matrix/) · [Jama](https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/requirements-traceability-matrix-pros-and-cons/)
- **F10 · 但追溯在场且新鲜时确有实效**——71 人受控实验，两个第三方项目上的真实维护任务：有追溯组平均**快 24%**、正确解**多 50%**。[Empirical Software Engineering 2014](https://link.springer.com/article/10.1007/s10664-014-9314-z)
  → **F9+F10 的联合读法：价值是真的，亏损点在"保鲜成本"，不在"有没有用"。**

**脚手架对非专家的收益曲线（Q5）**

- **F11 · 常驻提示会反转为有害**（Nückles et al. 2010，两个学期长纵向实验）——实验 1：有提示组在**前半学期**策略使用与学习成果均优于无提示组，**学期末优势消失**。实验 2：渐隐组 vs **常驻提示组** —— 渐隐组策略使用**越来越多**，常驻组**越来越少**，**学期末常驻提示组的学习成果显著低于渐隐组**。机制：学习者内化策略后，外部提示变成 redundant stimulus，产生 **extraneous cognitive load**。[全文 PDF](https://www.jsums.edu/english/files/2014/03/nuckles.pdf) · [ERIC EJ880291](https://eric.ed.gov/?id=EJ880291)
- **F12 · expertise reversal 的一般形式**——对新手有效的指导，随知识增长会变得多余乃至有害；处方是**按当前水平动态适配 + 逐步撤除（guidance fading）**，而非恒定高支撑。[Instructional Science 2009](https://link.springer.com/article/10.1007/s11251-009-9102-0) · [Sweller · The Guidance Fading Effect](https://cogscisci.wordpress.com/wp-content/uploads/2019/08/sweller-guidance-fading.pdf)

## Step 3 · 三视角

#### 视角 A · Atul Gawande（外科医生 / WHO 手术安全清单主导者 /《清单革命》作者）

**选用理由**：本题最核心的争议轴 = **「一张清单式的东西到底能不能防住遗漏，以及必须长成什么形状」**。Gawande 是唯一同时握有**大规模阳性结果（F1）与自家清单被复制失败（F2）**两端的人，也是唯一把"清单形态"写成可执行规则（F3）并明确区分"任务清单 vs 沟通清单"（F4）的人——这正是 ORD-43 失败模式（"沦为官僚表格"）缺的那把尺子。

**【原话】**（书中原文，经二手摘录站转录，未核对原书页码）："They supply a set of checks to ensure the stupid but critical stuff is not overlooked, and they supply **another set of checks to ensure people talk and coordinate and accept responsibility** while nonetheless being **left the power to manage the nuances and unpredictabilities** the best they know how."[grahammann 书摘](https://grahammann.net/book-notes/the-checklist-manifesto-atul-gawande) · [tosummarise 书摘](https://www.tosummarise.com/book-summary-the-checklist-manifesto-by-atul-gawande/)

**【模拟推理】**：

- **软件想法的早期讨论在三分法里是 complex，不是 complicated**（每个想法的维度构成都不同，专业能力必要但不充分）。因此覆盖地图应做成 **communication checklist**：每行不是"这个维度做完了吗"，而是"**到某个时点，必须就某个维度对话一次**"。这条区分同时化解了本项目"只自动化低误报检查"的纪律冲突——"你漏了营销"是高误报的语义断言，而"到 readiness 前请就营销对话一次"是零误报的流程提示。
- **升格 ≠ 扩容。** F3 给出可直接抄用的硬边界：**≤7 行**（5–9 项工作记忆上限，给非专家用户留余量）、**只放 killer dimensions**（漏了会致命的，不是全集）、**必须绑定明确的 pause point**、**用 DO-CONFIRM 而非 READ-DO**（先自由讨论，事后回来核，而不是照着大纲逐项讨论）。ORD-43 现有的"只覆盖高危维度、其余走散文"其实已经踩在这条线上——**升格要保住的正是这条线**。
- **F2 是这个提案最该抄的教训**：同一张清单，自愿实施显著有效，行政强制推行归零。翻译到本项目 = **强制每轮维护地图，等价于 Ontario 的强制模式**；由 AI 在明确 pause point 上主动派生一次、由人决定采纳，等价于有效模式。
- **状态列不许出现"已覆盖/完整"。** 只允许 `已讨论 / 未讨论 / **已明确判定不适用**`。第三种是全表价值最高的一行——它记录的是一次**主动排除决定**（真实的范围信息），而"已覆盖"是一个无法验证的完整性宣称，正是 F5 里"打了勾但没核对"的书面版。

**关切 → 路径**：关切 = 一张跨轮持久的多维度表最可能的归宿是被打勾而非被读（F5）。达成用户原目标（防遗漏）的路径 = **把它做成 ≤7 行的沟通清单，绑在 2 个 pause point 上**（苏格拉底轮结束、readiness 评估前），**用 DO-CONFIRM 语气**，**状态列禁用"已覆盖"、启用"已明确判定不适用"**。这四条都是纯写法约束，改 skill 文档即可，不引入任何新工件。

#### 视角 B · Thomas R. G. Green（认知维度框架 Cognitive Dimensions of Notations 创立者）

**选用理由**：第二条独立争议轴 = **「把它从『单轮一次性段落』改成『跨轮持久记法』，这个属性本身要付什么代价」**。视角 A 只管清单内容长什么样，不回答"持久化"这个动作的成本。Green 的框架是少数**专门给"记法本身"的认知代价命名并可度量**的语言，而且他的 premature commitment / viscosity 两个维度恰好一一对应本提案的两个风险，比泛泛引用"锚定效应"贴题。

**【原话】**："Viscosity: **resistance to change**. … We distinguish repetition viscosity, many actions of the same type, from **knock-on viscosity, where further actions are required to restore consistency**." / "Premature commitment: **constraints on the order of doing things**." / "**The most demanding activity is exploratory design** … Viscosity has to be as low as possible, premature commitment needs to be reduced, visibility must be high."[CT2001](https://www.cl.cam.ac.uk/~afb21/publications/CT2001.pdf) · [doi:10.1145/345513.345233](https://doi.org/10.1145/345513.345233)

**【模拟推理】**：

- **先给这个提案做一次维度画像**：多轮讨论 = exploratory design（Green 明说这是要求最苛刻的活动，要求 viscosity 最低、premature commitment 最少、provisionality 高）。而"跨轮**维护**的覆盖地图"正好把三项全部推向坏的方向——每轮讨论完要回头改地图（repetition viscosity）、改了一行要连带调整状态与出处以恢复一致（**knock-on viscosity**，F9 里追溯矩阵死掉的正是这一条）、在苏格拉底轮就把维度定死（premature commitment）。**这不是"是否该做"的否决，是"该做成什么记法"的定位。**
- **决定性的一招：把地图从「被维护的工件」改成「被派生的视图」。** 覆盖地图不落成一个需要增量编辑的常驻文件，而是**每次需要时由 AI 从各轮 `NN-*.md` + `DECISIONS.md` 重新生成**。这样 knock-on viscosity **降到 0**（改讨论轮不需要连带改地图），保鲜成本**降到 0**（视图永远是当下真相的函数，不存在"过期"）。F9 与 F10 合在一起给的正是这个结论：追溯的价值是真的，亏在手工保鲜——**那就让它成为导出物，而不是被维护物**。这也直接对上本项目"降低维持秩序所需能量"这条最高杠杆原则：**派生视图的维护能量结构性为零，而不是"尽量少"**。
- **premature commitment 的对策不是"别写维度"，而是 provisionality**（F6 第三个维度）。具体三条：① 派生时输出**候选维度**而非唯一维度集；② 表头固定声明"本表非穷举、示例性质"；③ **永久保留一行 `表外 / 未归类`**，专收不属于任何既有维度的东西。这一行是对 F8 设计固着的直接结构对策——固着降低的是解空间宽度而非产出数量，所以"多写点"没用，**必须有一个不属于任何格子的格子**。
- **F7 是给"要不要引入维度抽象"的收费提醒**：引入抽象总要配一个抽象管理器，抽象本身也会变黏。派生视图形态恰好绕过了这一条——**没有需要人来管理的抽象，只有一次性重新计算**。

**关切 → 路径**：关切 = "跨轮维护"这个词本身就把记法推到探索式设计最不适合的角落。达成原目标（跨轮范围边界）的路径 = **保留跨轮语义，取消跨轮维护**——覆盖地图定义为**派生视图**（按需从轮次文件重算）、输出**候选维度**而非定论、固定带 `表外` 行。跨轮一致性由"每次重算"提供，而不是由"每次维护"提供。

#### 视角 C · John Sweller（认知负荷理论创立者 · expertise reversal / guidance fading 效应）

**选用理由**：第三条独立轴 = **「这份脚手架对**这个具体的人**、在**项目的哪个阶段**成立」**。用户的立项理由明确写的是"基于人的非专业性"——那么就必须用研究"给新手加支撑"的那一支来量它。Sweller 这一支是唯一同时给出**支撑有效**与**支撑何时反转为有害**两端量化结论的（F11/F12），而这恰好决定"持续跨所有后续轮次"这个设计成不成立。

**【原话】**："instructional designs and techniques that are relatively effective for novice learners can **lose their effectiveness and even have negative consequences with increasing levels of expertise**. As a result, instructional methods including **the amount of instructional guidance provided to learners should be dynamically tailored to changing levels of learner expertise** in a particular area or domain."[Sweller · The Guidance Fading Effect](https://cogscisci.wordpress.com/wp-content/uploads/2019/08/sweller-guidance-fading.pdf)

**【模拟推理】**：

- **前半程：用户的直觉有直接实验支持。** F11 实验 1 前半学期，有提示组在策略使用与成果上双双优于无提示组。翻译过来 = **苏格拉底轮刚结束、用户对自己项目的维度结构最没概念的那个时点，一份外部派生的维度大纲的收益是最大的。这是全流程中最该给脚手架的一刻，值得单独实现。**
- **后半程：正是本提案的设计缺陷所在。** F11 实验 2 的对照组名字就叫 **permanent prompts（常驻提示）**——结果是学期末**显著劣于渐隐组**，且常驻组的策略使用是**逐期下降**的。提案里"persists across all subsequent rounds"这个属性，与实验里被证伪的那一臂**同构**。机制也说得很具体：用户内化了维度感之后，外部表格变成 redundant stimulus，产生 extraneous cognitive load——**对一个被明确描述为"容易被压垮"的用户，这是最不该额外施加的负荷类型**。
- **所以正确的形状是「首次强、之后渐隐、有退休条件」**：① **苏格拉底轮后派生 1 次**（支撑峰值）；② **readiness 评估 / 交 proj-plan 前派生 1 次**（此时"不决策的代价"最高，与 JIT/LRM 的最后责任时刻重合）；③ **中间轮次不派生**；④ **给退休触发器**。ORD-43 已有的回滚条款（不再产生新洞察就退回手工 open items）可直接复用为退休条件，只需补一个可观察的度量——**连续 2 次派生没有产出任何新的 `未讨论` 行 → 停止派生**。F11 里的 fading 是"策略被满意地使用一次就撤掉该提示"，这条度量是同一逻辑的工件版。
- **对"人最多读 5 个 artifact"这条硬规则的直接推论**：覆盖地图**不应占用第 6 个名额**。派生视图形态天然满足——它渲染进当轮的 `NN-*.md` 的一节，或作为 GATE 前的一次性呈现，**不产生新的常驻阅读对象**。

**关切 → 路径**：关切 = "跨所有后续轮次持续"这一条与 F11 中被证伪的常驻提示臂同构，对易过载的非专家尤其不利。达成原目标（帮非专家建立范围感）的路径 = **把"持续"换成"两个峰值 + 渐隐 + 明示退休条件"**：苏格拉底轮后派生一次拿到 F11 前半程的全部收益，readiness 前再派生一次守住遗漏关口，中间轮不打扰，并用"连续 2 次无新增 `未讨论` 行"作为可观察的停机信号。

## Step 4 · 收敛

三个视角从**内容形态 / 记法经济学 / 用户时间轴**三条独立路径进入，在四点上收敛：

1. **用户的诉求成立，但"cross-round maintained"这个修饰词要换掉。** 三方都不反对"给非专家一份多维度范围指引"——A 认可防遗漏（F1）、B 认可跨轮一致性有真实价值（F10）、C 认可首次派生时点收益最大（F11 前半程）。三方各自独立地否掉的是**同一个词：maintained（被持续维护）**。A 的理由是维护会催生打勾行为（F5）、B 的理由是 knock-on viscosity 会杀死它（F6/F9）、C 的理由是常驻提示已被实验证伪（F11 实验 2）。
2. **一致的替代形态 = 派生视图（derived view），而非维护工件。** 由 AI 从各轮 `NN-*.md` + `DECISIONS.md` 按需重算，跨轮语义由"每次重算"提供，而非由"每次编辑"提供。这一条同时把提案的成本从"低"（原 J-3 估计）落到**结构性为零**，并且是唯一与本项目"降低维持秩序所需能量"原则同向而非反向的形态。
3. **一致的边界纪律，四条可直接写进 skill**：**≤7 行只放 killer dimensions**（F3）；绑定 **2 个 pause point**（苏格拉底轮后 / readiness 前），中间轮不强制（F3+F11）；状态列**禁用"已覆盖"、启用"已明确判定不适用"**（F5 + 本项目"只自动化低误报检查"）；固定保留 **`表外 / 未归类`** 一行 + 输出**候选**维度而非定论（F6 provisionality / F8 设计固着）。
4. **必须自带退休条件。** ORD-43 现有的回滚条款直接复用，补一条可观察度量：**连续 2 次派生零新增 `未讨论` 行 → 停止派生**。F2 与 F11 从两个完全不同的领域指向同一件事——**这类机制的失败从来不是"设计得不好"，而是"该停的时候没停"**。

**未收敛（留给人裁决，不做调和）**：视角 A 认为 pause point 应绑在**流程时点**上（苏格拉底轮后 / readiness 前），视角 B 的派生视图逻辑其实允许**任意时点按需重算**（因为成本为零，"何时看"变成纯人的选择）。两者导出不同的 skill 写法：A 是"AI 在这两个时点主动派生"，B 是"用户随时可要求派生，AI 只在这两个时点主动提醒"。本轮无据可定——**主动派生 vs 按需派生，是这个议题剩下的唯一真实分歧**。

## Step 5 · 建议

**做，但把提案里的"cross-round maintained"改成"按需派生的视图"**——保留跨轮语义与范围边界这两项用户真正要的东西，取消"每轮维护"这个所有证据都指向失败的属性。落地形态 = AI 从各轮讨论文件按需重算的 **≤7 行 killer-dimension 沟通清单**，绑苏格拉底轮后与 readiness 前两个 pause point，状态列禁用"已覆盖"、固定带 `表外` 行，并复用 ORD-43 现有回滚条款作为退休触发器（连续 2 次零新增 `未讨论` 行即停）。

这样改之后它**不是 ORD-43 的升格，而是 ORD-43 的一次「命名 + 接线」**：机制没变（还是维度 × 取值 × 状态 × 出处），变的只是由谁在什么时候生成它——因此不新增人的阅读工件、不新增维护负担，与本项目 JIT 与"降低维持秩序所需能量"两条原则同向。剩下需要你拍板的只有一处：**苏格拉底轮后由 AI 主动派生，还是仅在你要求时派生（AI 只在两个时点提醒）**。
