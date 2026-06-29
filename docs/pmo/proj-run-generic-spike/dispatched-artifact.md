<!-- WORKER OUTPUT produced via conversation-fallback adapter (EXP-08). spawn = parent-as-worker; this file = collect target. -->
# Dispatch test artifact

- objective: 证明 conversation-fallback adapter 能完成一次 spawn→collect→validate 闭环（无 Cursor 依赖）
- adapter: conversation-fallback (context_isolation=false)
- specialist: subagent:explorer（由父 agent 内联扮演）
- validated-by: proj-run core validation gate（ORD-22 structural+behavioral）
- runtime: 任意（本次在非-sub-agent 的纯对话路径下产生）
