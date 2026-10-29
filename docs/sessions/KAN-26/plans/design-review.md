# Design Review

## Review Summary

The proposed design is a small, local FastAPI JSON API with SQLite persistence, matching KAN-26. Isolating it under `projects/kan-26-task-api/` keeps the completed KAN-25 Calculator project separate.

## Requirement Coverage

| Requirement | Design coverage |
|-------------|-----------------|
| FR-001 | Create endpoint and input schema require title, description, and status/default. |
| FR-002 | List endpoint returns all persisted tasks and an empty array when none exist. |
| FR-003 | Get-by-ID endpoint returns a task object. |
| FR-004 | PATCH endpoint updates only fields supplied by the client. |
| FR-005 | Delete endpoint returns a confirmation. |
| FR-006 | SQLite auto-increment primary key supplies IDs. |
| FR-007 | Schema and persistence constrain status values and default to `todo`. |
| FR-008 | Routes return HTTP 404 and the required exact message for missing IDs. |

## Findings

1. **Acceptance-criteria gap:** Jira has no explicit ACs for FR-006, FR-007, and FR-008. The architecture maps these requirements, but the planner should propose verifiable cases and request confirmation before implementation begins.
2. **Project boundary:** The proposed subdirectory keeps KAN-26 separate within the same Git repository. This satisfies the stated separate-project decision without creating an unrequested GitHub repository; note this boundary in the plan.

## Decisions

- Use a self-contained project directory with its own source, dependencies, tests, and SQLite file.
- Do not alter the existing calculator source or its root runtime dependencies.
- Preserve the exact not-found message from FR-008.
- Keep the listed five Jira ACs distinct from any proposed ACs for FR-006 through FR-008.

## Final Review Status

CONDITIONALLY APPROVED FOR IMPLEMENTATION PLANNING. No architecture blocker remains. The implementation plan must present proposed FR-006 through FR-008 verification cases for user confirmation before development.