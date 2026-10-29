---
name: sdlc-workflow-orchestration
description: 'Start or resume the full agentic SDLC by delegating to specialist agents in dependency order and enforcing human approval gates.'
---

# SDLC Workflow Orchestration

1. Read `.github/copilot-instructions.md` and `.cache/sdlc/session-memory.json` if present. Select the requested session and load its canonical context under `context/`; treat the canonical file as authoritative. Locate only artifacts needed for the next stage.
2. Run stages in order and delegate to the named agent: business analyst; solution architect; solution engineer; branch/git planner; developer; code reviewer; automation tester; deploy/build engineer; chronicle auditor.
3. Requirements stage: obtain a JIRA key/URL, retrieve the real story, clarify ambiguity, produce requirements, and stop for approval.
4. Architecture and design review follow approved requirements. Planning follows review; produce the plan and stop for explicit approval. Do not start production implementation before approval.
5. Delegate implementation, then code review. Return blockers to the developer and repeat review until resolved. Delegate verification and require actual passing tests before release.
6. Delegate release preparation. Get explicit approval before PR creation; after final PR review, require explicit approval before merge.
7. Give each agent a compact handoff: session/story ID, stage objective, relevant requirement IDs, input paths, expected artifact path, constraints, and approval state. Reference files rather than copying full documents or chat history.
8. After each stage, verify its expected artifact and update canonical session context with actual results, approvals, and history; then refresh the compact cache entry. If the cache disagrees with canonical state, rebuild it from canonical session files. Keep summaries concise but evidence-backed.
9. Stop whenever user input/approval or an unavailable integration/agent blocks progress. Report completed stages, artifacts, blockers, and the next required decision.
10. Delegate the workflow audit after other stages and produce the final HTML report from verified evidence only.