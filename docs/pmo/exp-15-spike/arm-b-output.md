<!-- EXP-15 臂 B（干预版）原始产出 · 独立上下文 subagent · 2026-08-27 · 逐字存档供独立复核，父 agent 未编辑正文 -->
<!-- 协议：R-4 commit-then-reveal（红队 Step 1 承诺稿在 A/B 存在前写入并冻结）+ R3 各视角独立检索 + R1 松绑模板 + R2 强制分歧节 -->

# proj-shape：ORD-43 是否升级为跨轮「讨论覆盖图」

# Step 1 · 视角 R · 红队（承诺稿 · 在 A/B 存在之前写下，不再修改）

**红队人选：Ryan Singer**（*Shape Up* 作者，原 Basecamp 产品策略负责人）。理由：本提案的核心机制是「一份跨周期持续存在、需要每轮 review 的中央清单」，Singer 是当代对这一机制批评最系统、且给出了替代方案的人。

**承诺立场：反对升级。ORD-43 应保持"单轮 / 可选 / 高风险维度 only"。** 不是"缓一缓"，是"这个方向本身走反了"。

## 1. 先做一次"去名字测试"

把 "discussion coverage map" 这个名字拿掉，只看机制：一份中央清单；条目在 Round 01 一次性生成、之后只增不减；每一轮开始前 AI 要读它，每一轮结束后要更新它的 status；它的存在理由是"提醒你还有东西没做"。**这是 backlog 的定义。** 给它换个名字（map / 覆盖图 / 大纲）不改变它的动力学。

【已公开立场】*Shape Up* 第 7 章 "Bets, Not Backlogs"：
> "Backlogs are a big weight we don't need to carry. Dozens and eventually hundreds of tasks pile up that we all know we'll never have time for. The growing pile gives us a feeling like we're always behind even though we're not."
> "Backlogs are big time wasters too. The time spent constantly reviewing, grooming and organizing old ideas prevents everyone from moving forward on the timely projects that really matter right now."
> — https://basecamp.com/shapeup/2.1-chapter-07

【已公开立场】Jason Fried：
> "We don't believe in backlogs. When you have backlogs, they make you feel guilty. It's a constant reminder of 'this is all the shit I haven't gotten to.'"
> "things change through context. Your backlog could be six months old. That's the problem with backlogs: they're old!"
> — https://justinjackson.ca/nobacklogs

【模拟推理】这个项目的用户是**单人、非专家、易被淹没**。backlog 的 guilt 效应在这种用户身上不是减弱而是放大：一个专家看到"营销维度：未讨论"会判断"不重要，跳过"；一个非专家看到同一行，会判断"我漏了一块，我不够格开始做"。你正在给一个已经模糊焦虑的人发一张永远填不满的表。**并且这直接违反该项目自己的最高杠杆原则**——"lower the energy required to maintain order"。

## 2. 覆盖率矩阵的病理是已知的，而且逐条对得上

【已公开立场】Jama Software（工具厂商，立场折扣已注）：
> "A documented bad practice that produces false confidence occurs when only requirement numbers populate the matrix rather than requirement text or summaries. An RTM can appear fully populated while the actual requirement-to-artifact relationships are never validated."
> — https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/requirements-traceability-matrix-pros-and-cons/

【已公开立场】Arorian（同为厂商博客，同样打折）：
> "This is the most dangerous hidden cost ... not the time it wastes, but the confidence it manufactures. Incomplete traceability that looks complete produces worse outcomes than obviously broken traceability, because engineers act on it."
> — https://arorian.com/manual-mbse-alm-traceability/

**这一条对本提案是致命的，因为用户的动机恰恰是"避免遗漏"。** 覆盖图只能覆盖"你在 Round 01 就已经想到的维度"。真正会杀死项目的遗漏，按定义不在那张表里。而表一旦填满，人和 AI 都会停止找遗漏。**它不减少遗漏，它减少你去找遗漏的动机，同时给你一张证明你没遗漏的纸。**

## 3. 时间点选错了：这是在最该发散的时刻投放锚点

【已公开立场】Smith, Ward & Schumacher (1993)，经 Purdue *Journal of Problem Solving* 综述转述：
> "participants who were provided with several examples of solutions prior to the idea generation task were more likely to incorporate the exemplified features into their responses compared to participants who were not presented with such exemplars. However, no difference was observed in the total number of generated ideas"
> — https://doi.org/10.7771/1932-6246.1093

【已公开立场】Kohn & Smith（*Applied Cognitive Psychology*）直接测了"类别广度"：
> "Exchanging ideas in a group reduced the number of domains of ideas that were explored by participants. Additionally, ideas given by brainstormers conformed to ideas suggested by other participants. ... Although fixation was observed in brainstorming in terms of conformity and restriction of the breadth of ideas, it did not influence the number of ideas generated"
> — https://doi.org/10.1002/acp.1699 · 摘要页 https://www.researchgate.net/publication/227683493_Collaborative_Fixation_Effects_of_Others'_Ideas_on_Brainstorming
> 背景综述 https://ecologylab.net/research/publications/constrainingEffects.pdf

**给出示例/类别会减少被探索的类别数量，但不减少产出量。** 用户会觉得"讨论很充分、条目很多"，而实际探索的维度范围收窄了。**这个机制专门骗过用户对"我讨论够了吗"的自我评估。**

【模拟推理】AI 特有的加重：AI 生成的"技术/商业/营销"是训练分布里最高频的商业计划书骨架。你不是在给用户一张属于他这个项目的地图，你是在给他一张属于"平均项目"的地图。对一个非专家用户，他没有能力判断这张地图哪几格对他不适用——他会全填。

## 4. 项目自己的 JIT 原则否决了它

在 Round 01 刚结束时，"营销维度未讨论"的不决定成本约等于 0。它在 Round 05 可能变高，那就 Round 05 再说。

【已公开立场】Ron Jeffries：
> "Always implement things when you actually need them, never when you just foresee that you need them."
> — https://www.ronjeffries.com/xprog/articles/practices/pracnotneed/

【已公开立场】Martin Fowler：
> "Planned design assumes change is hard, and thus tries to predict where it occurs. If changes occur within the predicted boundaries then it's easy, but if it falls outside those boundaries you're out of luck." / "the fundamental question I ask is 'is change predictable?'"
> — https://martinfowler.com/bliki/EvolutionarySOA.html

**一个非专家用户的模糊想法，其"讨论维度结构"恰恰是整个系统里最不可预测的东西。** 这是 planned design 的最差适用场景。

## 5. 跨轮维护 = 陈旧化，而这次读者是 AI

【已公开立场】
> "No documentation costs you time on a predictable schedule... Stale documentation costs you time at the worst possible moments."
> — https://sync-o.io/blog/stale-documentation-engineering

【已公开立场】
> "AI repeats a stale doc with full confidence and never flags that it might be wrong, which removes the human hesitation that used to contain the damage."
> "The most dangerous documents are the best-formatted and highest-ranked ones, because polish and search position suppress scrutiny."
> — https://slite.com/learn/dangers-of-stale-documentation

【模拟推理】**一张结构整齐的维度表恰恰是"格式最好看"的文档**，它会压制审视。而写它的是 AI、读它的也是 AI、判断它是否过期的还是 AI——**没有外部校正的自我强化回路**。项目自己有原则"只自动化低误报检查"——"这个维度是否已经讨论充分"是纯语义判断，是该原则明令排除的那一类。本提案等于偷偷把它自动化了，只不过输出的不是告警而是一行 status。

## 6. 这不是新设计，是 ORD-43 已写明失败模式的实例化

ORD-43 自己记录的失败模式是 "dimension table becoming a bureaucratic form"。本提案在两个轴上各推一格：**可选 → 事实强制**（跨轮维护的东西不可能可选），**单轮 → 跨轮**。当一份设计文档已经写下"这样做会变成官僚表格"，而新提案正是朝那个方向走，**举证责任在提案方**。

**并且退出成本不对称。** 现在 rollback 很便宜（删掉一个可选 section）；升级后 rollback 会变贵（跨轮引用、DECISIONS 锚点、AI 每轮读入习惯都要拆）。红队要求：**如果一定要做，先把退出路径写出来并标价，再决定做不做。**

## 7. 红队认为真问题在别处（替代方案）

【模拟推理 · 基于 Shape Up 的 appetite 概念】用户说的是"避免遗漏"，但他真正的焦虑是**"我不知道什么时候讨论算够了"**。覆盖清单是对这个焦虑的错误答案——它把"够了"定义成"表填满了"，而表永远填不满。Shape Up 的答案是 **appetite**：固定时间盒、可变范围。翻译到 proj-shape：给讨论一个 appetite（最多 N 轮，之后必须做 readiness 判断）；"遗漏"由**下游便宜地回流**兜底，而不是由上游穷举预防；真正要防的是"遗漏了会让整个方案报废的那一件事"——那应该是 **1–3 条 kill-criteria**，不是一张 N×4 的表。

**红队最终承诺：不升级。** 若用户坚持要动，红队愿意在揭示轮讨论"最小可退版本"，但反对把它称为 coverage map、反对跨轮 status 维护、反对 AI 预生成维度分类法。

# Step 2 · 两个独立视角（各自独立检索）

## 视角 A · Jeff Patton（*User Story Mapping* 作者）— 「你要的不是维度表，是骨架；而骨架必须有叙事」

我先讲我怎么走到这儿的。我花了十几年劝人别把待建的东西写成一列清单。我见过的失败几乎从来不是"漏了某一类"——而是每一条都在、没有一条缺，可是屋子里没有一个人能连贯地讲出这个产品到底是什么。清单看着完备，理解是碎的。

【已公开立场】*The New User Story Backlog is a Map*：
> "The flat backlog is poor explanation of what a system does. Arranging user stories in the order you'll build them doesn't help me explain to others what the system does."
> — https://jpattonassociates.com/the-new-backlog/

所以对"扁平不够"这个直觉，我站在提案这一边。红队想把它一笔勾销，我不接受。**但提案里的那个东西不是 map，是 taxonomy，这两者的差别正好是全部关键。**

【已公开立场】story map 的力量不在"二维"，在于横轴是**有叙事顺序的 backbone**：活动卡片按 "the order that you would choose if describing the business process to someone unfamiliar with it" 排列（https://www.infoq.com/news/2009/03/story-map/）。

"技术 / 商业 / 营销"没有顺序。它是分类，不是叙事。**分类不会暴露空白，叙事才会。** 分类表的空格只告诉你"这一格是空的"——没有信息量，因为它永远是空的。而叙事里的空白会让你**卡住讲不下去**，这是有信息量的信号。

【已公开立场】走查要问："Does the journey make chronological sense? Are there gaps (moments where the user doesn't know what to do)?"（https://antoinepeze.com/en/story-mapping-workshop/）；空白的用法：
> "If you cannot articulate the user tasks under a backbone activity, it means you need more user research in that area. The map becomes a research agenda: the empty spaces tell you where to investigate next."
> — https://makeitnice.de/en/frameworks/story-mapping/

【已公开立场】Atlassian："Story maps help reveal missing steps, confusing experiences, duplicate work, or areas where the team lacks enough user insight."（https://www.atlassian.com/agile/product-management/story-mapping）

【已公开立场】*Why Documents Fail and What You Can Do About It*：
> "Shared documents aren't shared understanding." / "If you replace a conversation with a document, you've stopped using stories." / "The best documents use words and pictures to help us recall our conversations, they don't replace them."
> — http://flowcon.org/dl/flowcon-sanfran-2014/slides/JeffPatton_WhyDocumentsFailAndWhatYouCanDoAboutIt.pdf · 速查卡 https://jpattonassociates.com/wp-content/uploads/2015/03/story_essentials_quickref.pdf

【已公开立场 · 二手转述】"Good documents are like vacation photos... what's most important isn't what's written down—it's what we remember when we read it."（https://www.linkedin.com/posts/jakubzalas_i-re-read-the-introduction-to-user-story-activity-7359456584197963776-Sjmw）

【模拟推理】把这句话当判据审本提案，得到一个干净的分叉：

- 如果这张图是 **AI 生成出来、交给人去看**的——那它就是"用文档替代对话"。它必然失败，而且以最难察觉的方式失败：用户读了，点头，以为自己理解了，实际什么都没建立。
- 如果它是 **人和 AI 在对话中一起走出来的，并且每一轮被重新走一遍**——那它是"度假照片"，是唤起上一轮对话的锚，而不是替代品。这个版本可能有用。

【模拟推理】我最看重的输出不是覆盖度，是 **walking skeleton**。翻译成讨论层：**能把这个想法从头到尾讲成一个完整故事所需的最小决策集合。** 这是比"覆盖度"好得多的 readiness 判据，因为它有停止点：故事讲通了就够了，讲不通就还差。**覆盖度没有停止点。**

【模拟推理 · 回应红队】红队说这是 backlog 换皮。我比屋子里任何人都更恨 backlog——我写了一本书反对它。**但红队把两种病理混成了一种**：backlog 的病理来自"条目是待办、带优先级、只增不减"；map 的病理完全不同，是**变成挂在墙上再也没人走过一遍的壁纸**。这两种病要用不同的药。红队开的药（appetite 时间盒）能治"什么时候停"，治不了"停下来的那一刻，我们对这个东西有没有共同理解"。

**我的立场：支持升级，但三个约束是硬的——(1) 必须是叙事骨架，不是维度分类法；(2) 必须人机一起走出来，不能 AI 预生成；(3) 每轮要重走一遍，而不是每轮更新一列 status。**

## 视角 B · 上下文工程视角（Anthropic Applied AI 公开工程立场 + Chroma *Context Rot* 实证）

说明：这不是单一个人的模拟，是两份有公开记录的工程立场的组合。Chroma 技术报告原始页面抓取超时未取到，以下引用为我确实取到的二手覆盖报道，已注明。

【已公开立场 · 二手覆盖】Chroma Research 2025-07 *Context Rot*，18 个前沿模型控制输入长度单一变量：
> "every single one of the 18 models showed performance degradation as input length increased. Not most. Not some. All of them."
> — https://hivetrail.com/blog/context-rot-chroma-study

LongMemEval 组最贴近本议题：
> "The focused version contains only the relevant material and averages about 300 tokens. The full version buries the same answer in the surrounding conversation and averages about 113k tokens. Models handled the focused prompts well and degraded consistently on the full ones."
> — https://glasp.co/articles/context-rot-rag-long-context-hybrid · https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens

**这组数字把这场辩论换了一个题目。** 前面两个视角都在争"这份文档对人好不好"。但在 proj-shape 里，跨轮的主要读者不是人——是 Round 05 那个必须重建"前四轮谈过什么"的 AI。那是**注意力预算分配**问题，有测量、有工程共识。

【已公开立场】Anthropic：
> "context windows of all sizes will be subject to context pollution and information relevance concerns... compaction, structured note-taking, and multi-agent architectures."
> "Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window."
> — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents · https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools · https://platform.claude.com/docs/en/build-with-claude/compaction

**所以在"要不要一份跨轮持久化的状态"上，我支持提案方向，理由是工程上的。** 但同一批证据把它的**形态约束死了**，而用户原提案三条全踩错：

**(a) 必须极短。**【已公开立场】"find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome"（同上）。一张十几行、四列、带来源的表作为每轮固定开销，是拿注意力预算换整齐。

**(b) 长了以后中间会被吞掉。**【已公开立场】*Lost in the Middle*（TACL 2024）：
> "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models."
> — https://aclanthology.org/2024.tacl-1.9/ · https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long

成因定位到内在位置注意力偏置：
> "LLMs exhibit an U-shaped attention bias where the tokens at the beginning and at the end of its input receive higher attention, regardless of their relevance."
> — https://arxiv.org/pdf/2406.16008

【模拟推理】**一张有"中间"的维度表，中间那几行会被系统性地少看。而"被遗漏的维度"恰恰最可能沉在中间——这个机制会优先吞掉它最该保住的那些行。** 硬约束：表必须短到不存在"中间"。

**(c) 预生成本身就是被否掉的模式。**【已公开立场】
> "Just-in-time over precomputation. The consensus that emerged from Anthropic, LangChain, and the Chroma research is that pre-loading knowledge into long contexts loses to retrieval at inference, on quality and on cost."
> — https://www.reactify-solutions.com/articles/context-engineering-ai-agents-2026

【模拟推理】"Round 01 之后由 AI 一次性生成多维度大纲"就是 precomputation 的定义。这一条我和红队结论一致，尽管路径完全不同。

**(d) 一条我必须诚实报告的、对我自己不利的结果。**【已公开立场 · 二手覆盖】
> "Logically coherent haystacks consistently produced worse performance than randomly shuffled haystacks across all 18 models."
> — https://hivetrail.com/blog/context-rot-chroma-study

【模拟推理】这条削弱了"整齐结构 = 对模型友好"这个几乎所有人都默认的直觉。**我不会假装这条支持我——它不支持。** 它意味着这份东西的收益**必须实测，不能从"结构化=好"推出来**。

**(e) 但正因如此，这件事不需要靠辩论定。它可测。**【模拟推理】在第 N 轮，让 AI 在有/无这份状态两种条件下回答"前面几轮里哪些结论与本轮相关"，比对人工标注黄金集，测 recall。这是**结构性检查、不是语义一致性检查**（比对"提到了没有"，不是"讨论得够不够"），不触碰项目"只自动化低误报检查"原则。**若 recall 没有可观测提升，提案自动作废。**

**我的立场：跨轮持久化状态方向对，有工程共识支撑；但用户提的具体形态——Round 01 预生成、多维度分类、给人读——三项全错。正确形态是：极短、增量 append、只给 AI 读、且带一个 recall 指标做存废判据。**

# Step 3 · 视角 R · 揭示轮

读完 A 和 B 之后，我的承诺立场不变：**不升级**。但有一处让步，先说让步。

**让步（并说明是什么证据改变了我）。** 视角 B 给出的 LongMemEval 对比改变了我的一个判断。我在 Step 1 里默认"跨轮召回问题"是想象出来的焦虑；~300 token 聚焦版与 ~113k token 完整版之间那个稳定的差距说明它不是——跨会话状态重建是真问题，而且已被测量。我接受这一点。但这不改变结论，因为它证明的是"需要一份压缩状态"，而 `DECISIONS.md` **已经就是**那份状态。它是**回顾性**的（已经决定了什么）。提案要加的是**前瞻性**的（还有什么没讨论）。回顾性压缩不制造 guilt、不制造虚假覆盖感、不需要 AI 做"讨论得够不够"的语义判断。B 的证据支持前者，不支持后者。

**第一处反对：我不同意视角 A 的核心结论——「换成叙事骨架就能逃掉 backlog 的病理」。**

Patton 的 backbone 之所以能让"讲不下去"成为真信号，是因为它锚在一个**外部可核对的事实**上：用户确实先做第 1 步、再做第 2 步。那个顺序不是团队编的，是可以去观察的。proj-shape 讨论的对象是一个**还不存在的想法**，没有 journey 可走。A 把 backbone 换成"这个想法的叙事"时，那条叙事本身正是待讨论的东西。**用一个尚未确定的东西当骨架去检测遗漏，是循环论证。** 落地之后，"讲不下去"只会退化成"AI 觉得讲不下去"——又回到项目原则明令排除的那类语义自动判断。

而且 A 自己引的材料就写着 *"Shared documents aren't shared understanding."*——同一句话反过来也砸在 A 自己的方案上。story map 的核心成分是**一屋子人各自不同的心智模型当场相撞**。proj-shape 里只有一个人和一个 AI，而那个 AI 没有独立的心智模型可撞——它生成的正是被讨论的内容。**A 是拿一个"多人共享理解"的工具去解一个"单人 + AI"的问题。**

**第二处反对：视角 B 的结论——「方向是对的，因为 structured note-taking 是 long-horizon agent 的标准解」——是错的。**

B 偷换了对象。Anthropic 说的 structured note-taking 记的是 **agent 自己的执行状态**：我试过什么、什么失败了、进行到哪一步。它 write-mostly、自用、任务结束即弃、**没有规范性含义**。B 想要的东西有 status 列、有规范性（一行"未讨论"就是在说"你欠着"）、要跨轮沉淀成项目资产、并且会被人瞥见。**名字像，失效模式完全不同。**

更要命的是，**B 自己引的两条证据反向指着 B 的结论**：其一，B 引的 *just-in-time over precomputation* 明确说预加载输不过 inference-time 检索——而"Round 01 后生成维度大纲"就是 precomputation；其二，B 诚实报出的 coherent haystack 结果（连贯结构比打乱顺序表现更差，18 个模型全部如此）直接打在 B 自己主张的"整齐的小表"上。**B 应该得出的结论是"不要预生成任何结构"，而不是"预生成一个短的"。**

**第三处反对：我也不同意视角 A 关于「这份东西必须给人读」的结论。**

A 说 map 的全部价值在共享理解，所以不给人读就毁掉了它。但项目有一条硬规则：人最多读 5 个 artifact。A 的方案还要求人**每一轮重走一遍地图**——这是持续的人力开销，不是一次性的。A 没有说这一格从现有的 5 个里挤掉哪一个。在这一点上我站视角 B：如果这东西非做不可，就别给人看。**而 A 如果接受"不给人看"，A 自己的论证（价值全在共享理解）就自动否掉了这个 artifact——A 的方案不存在既满足自己前提又满足项目约束的版本。**

**立场不变。** 我承认跨轮召回是真问题（B 的功劳）。我不承认前瞻性覆盖表是它的解。如果一定要动，最低条件仍是 Step 1 结尾那三条：不叫 coverage map、不做跨轮 status 维护、不由 AI 预生成维度分类法。

# Step 4 · 分歧表（未解决，不做调和）

| # | 争议点 | 一方立场 | 另一方立场 | 本轮未解决 / 交人裁决点 |
|---|---|---|---|---|
| 1 | 是否应存在**跨轮持久化**的讨论状态清单 | **R**：不应该。机制上等同 backlog，违反项目自身"降低维序能耗"原则，且 ORD-43 已把这个失败模式写在纸上；rollback 成本会从"删一节"升到"拆引用" | **A**：应该，但只作为叙事骨架 ／ **B**：应该，是 long-horizon agent 的标准解，有 LongMemEval 数据支撑 | 未解决。R 只让步到"回顾性状态（DECISIONS.md）够了"，A/B 都要求增加前瞻性成分。这是根问题，其余四行都依赖它 |
| 2 | 维度**从哪来**：AI 预生成分类法 vs 从内容中涌现 vs 稳定 schema | **A**：必须从用户自己的叙事中涌现，横轴要有真实顺序；AI 给的"技术/商业/营销"是分类不是骨架，不会暴露空白 | **B**：需要一个跨轮**稳定**的 schema，否则轮与轮之间 AI 无法对齐；schema 稳定性是机器可用的前提。（R 两个都反对） | 未解决，且这是 **A 与 B 之间的直接对立**：涌现要求形状可变，机器对齐要求形状固定。两者不可同时满足 |
| 3 | 这份 artifact **给谁读** | **A**：给人读。它的全部价值是共享理解，做成 AI 内部状态就没有存在理由了 | **B**：只给 AI 读。人只有 5 个 artifact 额度，这个不配占；给人看还会触发 guilt。**R 在此站 B** | 未解决。R 在揭示轮指出 A 的方案不存在"既满足自己前提、又满足 ≤5 硬规则"的版本；A 未回应 |
| 4 | "覆盖度"到底**降低还是提高**遗漏风险 | **R**：净负面。false confidence 让人停止找遗漏；且 fixation 实证显示给出类别会**减少被探索的类别数**而不减少产出量——专门骗过用户的自我评估 | **A**：能降低，但机制不是格子填满，是叙事"讲不下去"暴露空白 ／ **B**：应交由实测（recall 指标）而非论证，且自报 coherent-haystack 结果削弱了"整齐即有效" | 未解决。三方对**同一个可观测量**给出了相反预测，因此这一行是最适合用实验切开的 |
| 5 | **时机**：Round 01 之后立刻生成，还是更晚/按需 | **A**：越早越好，map 的价值就在于早期暴露空白 | **R + B**：都反对预生成，但理由不同——R 用 JIT／最后责任时刻，B 用 "just-in-time over precomputation" | 未解决。注意这一行 R 与 B 结论相同但推理路径无交集；A 单独一侧，且 A 的理由（早暴露）恰恰要求它落在 R/B 都认为最不该做的时点 |

# Step 5 · 收敛（仅列真实一致点）

以下三点三方**独立**得出相同结论，且与 Step 4 的五行分歧**并存**，不构成对它们的取代或缓和：

1. **用户原提案的那个具体形态，三方一致否决。** 即"Round 01 之后由 AI 预生成一份技术／商业／营销的多维度大纲"。理由完全不同——R：那是训练分布里的平均骨架，不是这个项目的地图；A：分类法不是叙事骨架，不会暴露空白；B：这是 precomputation，与 just-in-time 共识相反。三条独立路径指向同一结论，这是本轮**证据最强的单一结论**。
2. **不能给"未讨论"这类 status 字段以规范性含义。** R：对非专家用户产生 guilt；A：空白应当触发一次对话，而不是变成一条待办；B：让 AI 判断"某维度讨论得够不够"是纯语义充分性判断，项目原则明令不自动化这一类。
3. **确实存在一个真问题需要解，只是三方开的药不同。** 三方都同意"用户不知道什么时候讨论算够了"是真实且值得解决的。但停止判据的形态没有共识——R 主张 appetite；A 主张 walking skeleton；B 主张可测指标（跨轮 recall）。**同意有病，不同意药方。**

# Step 6 · 建议

不要按用户原样实施——Step 5 第 1 条是本轮唯一由三条独立推理共同支撑的结论。**分歧表第 2 行（维度从哪来）和第 3 行（给人读还是给 AI 读）必须由人先裁决**，因为这两个问题决定了这份 artifact 究竟是什么东西，任何实验设计都取决于它们，且 A 与 B 在这两行上的立场在逻辑上不可同时成立。裁决之后，唯一值得付出的下一步是第 4 行指向的那个实验：在一次真实讨论中并行跑带／不带骨架两个版本，测 B 提出的跨轮 recall 与 R 提出的"被探索维度类别数"。**在人做出第 2、3 行的裁决之前，ORD-43 保持现状。**

---

```
AUDIT
red_team_named_oppositions: 3
disagreement_rows: 5
urls_red_team: https://basecamp.com/shapeup/2.1-chapter-07, https://justinjackson.ca/nobacklogs, https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/requirements-traceability-matrix-pros-and-cons/, https://arorian.com/manual-mbse-alm-traceability/, https://doi.org/10.7771/1932-6246.1093, https://doi.org/10.1002/acp.1699, https://www.researchgate.net/publication/227683493_Collaborative_Fixation_Effects_of_Others'_Ideas_on_Brainstorming, https://ecologylab.net/research/publications/constrainingEffects.pdf, https://www.ronjeffries.com/xprog/articles/practices/pracnotneed/, https://martinfowler.com/bliki/EvolutionarySOA.html, https://sync-o.io/blog/stale-documentation-engineering, https://slite.com/learn/dangers-of-stale-documentation
urls_perspective_a: https://jpattonassociates.com/the-new-backlog/, http://flowcon.org/dl/flowcon-sanfran-2014/slides/JeffPatton_WhyDocumentsFailAndWhatYouCanDoAboutIt.pdf, https://jpattonassociates.com/wp-content/uploads/2015/03/story_essentials_quickref.pdf, https://www.infoq.com/news/2009/03/story-map/, https://makeitnice.de/en/frameworks/story-mapping/, https://antoinepeze.com/en/story-mapping-workshop/, https://www.atlassian.com/agile/product-management/story-mapping, https://www.linkedin.com/posts/jakubzalas_i-re-read-the-introduction-to-user-story-activity-7359456584197963776-Sjmw
urls_perspective_b: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools, https://platform.claude.com/docs/en/build-with-claude/compaction, https://aclanthology.org/2024.tacl-1.9/, https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long, https://arxiv.org/pdf/2406.16008, https://hivetrail.com/blog/context-rot-chroma-study, https://www.reactify-solutions.com/articles/context-engineering-ai-agents-2026, https://glasp.co/articles/context-rot-rag-long-context-hybrid, https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens
```

**引用完整性说明（原文附）**：所有 URL 均为本次实际检索所得。Chroma *Context Rot* 技术报告原始页面抓取超时未取到，故视角 B 引用的是确实取到的二手覆盖报道，已在正文标注。视角 A 引用的 LinkedIn 链接为他人对 Patton 书中原文的摘录，正文已标为二手转述。Jama、Arorian、sync-o、slite 为厂商/商业博客，红队已自行标注可信度折扣。
