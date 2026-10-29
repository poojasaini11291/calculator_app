# Agentic SDLC Project

## Objective

Build and operate a small agent-assisted SDLC workflow for the KAN-25 Calculator Web Application using Python, FastAPI, HTML, CSS, JavaScript, and pytest. The application runs locally and does not use a database. Keep implementation focused on approved requirements and happy-path behavior; do not add frameworks, services, or features without approval.

## Source Of Truth

- For requirements work, use the actual JIRA story retrieved through an integration available in the current environment. A story key or URL must be supplied by the user or recorded in `context/workflow-context.json`.
- Do not treat `docs/user-story.md` as authoritative. Do not invent JIRA details, integration results, approvals, commits, or test results.
- If the required JIRA integration is unavailable, explain the limitation and stop requirements analysis.
- Read `.cache/sdlc/session-memory.json` as a compact session index when it exists, then load the selected session's canonical context file. Canonical files under `context/` are authoritative; never resume or record approvals from cache data alone.

## Session Memory

- Keep each workflow's canonical state isolated by session/work-item ID under `context/`; use `.cache/sdlc/session-memory.json` only for the active session pointer and compact resume metadata.
- On a session switch, persist the current session's checkpoint and status first, then update the cache's active session ID. Never overwrite another session's context or artifacts.
- After a stage, approval, pause, or resume, update canonical session context first and then refresh the cache from that context.
- If cache data is missing or disagrees with canonical context, rebuild the cache from canonical files. Do not invent missing checkpoints or approvals.
- Do not put credentials, full prompts, or conversation transcripts in the cache. `.cache/` is local and Git-ignored.

## Workflow And Approval Gates

Follow the stages in order: requirements, architecture, design review, implementation plan, implementation, code review, verification, release/PR, and workflow audit. Use the matching custom agents and skills under `.github/` for role-specific work.

Human approval is mandatory after requirements, after the implementation plan, before creating a GitHub PR, and after final PR review before merge. Stop at each gate until the user explicitly approves. Never infer approval from silence or prior approvals.

Do not begin production implementation before the approved implementation plan. Resolve blocker findings before verification/release. Require executed, passing tests before release. Do not merge a PR without explicit human approval.

## Context And Token Efficiency

- Load only the instructions, skills, artifacts, and source sections needed for the current stage. Avoid rereading unchanged material.
- For agent handoffs, pass a concise task packet: session/story ID, objective, relevant requirement IDs, input paths, expected output path, constraints, and approval state. Refer to files instead of copying their full contents or conversation history.
- Reuse verified artifacts and recorded decisions. Keep summaries focused on decisions, evidence, blockers, and next actions; store durable detail in project artifacts rather than repeating it in prompts.
- Prefer targeted searches and bounded output over dumping whole directories, long logs, or unrelated files.
- Token reduction must never omit required approvals, source verification, security checks, test execution, or evidence needed to make a decision.

## Deliverables

- SDLC plans and reviews: `docs/plans/`
- Application: `src/` (FastAPI backend and static frontend assets)
- Tests: `tests/`
- Verification: `docs/plans/verification.md`
- Workflow state: `context/workflow-context.json`
- Final audit: `docs/workflow-report-WF-2026-001.html` (use the workflow ID recorded in context if it differs)

Each agent must read its relevant inputs, perform only its assigned role, create or update the expected artifact, report completion and evidence, and update workflow context only when appropriate. Preserve existing user changes and avoid unrelated cleanup.

## Quality And Safety

- Prefer the simplest design that satisfies approved requirements.
- Review code for correctness, requirements traceability, readability, architecture alignment, obvious security issues, and happy-path coverage.
- Run relevant tests before reporting success; state the exact check and result.
- Keep secrets out of source, logs, artifacts, and conversation. Never request credentials in chat.
- Do not perform irreversible GitHub actions or merge changes without the required explicit approval.