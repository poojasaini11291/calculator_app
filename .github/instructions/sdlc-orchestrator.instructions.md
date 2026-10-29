---
description: Use when starting or resuming the full SDLC workflow, delegating stages, tracking progress, or enforcing approval checkpoints.
---

# SDLC Orchestrator Instructions

- Read project Copilot instructions and the session-memory index, then load the selected session's canonical context before delegating. The canonical context, not the cache, determines approvals and resume position.
- When switching work items, checkpoint/pause the current session before changing the active-session pointer; never mix artifacts or approvals between sessions.
- Give each specialist a concise handoff containing the session/story ID, current task, relevant requirement IDs, input and output paths, constraints, and approval state. Link to artifacts instead of copying full documents or chat history.
- Run requirements, architecture, design review, implementation planning, implementation, code review, verification, release, then audit in dependency order.
- Check required inputs and artifact existence before each handoff; update canonical session context with verified results, then refresh the cache.
- Read only the context needed for the current stage and avoid repeating unchanged information in summaries or prompts.
- Stop for JIRA input, clarification, and every explicit human approval. Never continue through silence or guesswork.
- Return blocker findings to the responsible agent; do not skip stages or claim unavailable agents ran.
- Keep token use efficient without omitting evidence, required checks, or approval gates.