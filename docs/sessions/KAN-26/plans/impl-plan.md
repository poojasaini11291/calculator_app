# KAN-26 Task Management REST API Implementation Plan

## Preconditions

- Requirements are explicitly approved.
- KAN-26 is treated as a separate project from KAN-25 Calculator.
- Confirm the proposed verification cases for FR-006 through FR-008 below before implementation starts.
- Do not alter the calculator source or root dependencies.

## Project Location

`projects/kan-26-task-api/`

## Recommended Branch

`feature/KAN-26-task-api`

## Tasks

| Task ID | Task | Dependencies | Expected files | Verification |
|---------|------|--------------|----------------|--------------|
| KAN26-01 | Scaffold the isolated FastAPI project, dependency file, package structure, local run instructions, and project-local SQLite configuration. | None | `projects/kan-26-task-api/requirements.txt`, `src/main.py`, `src/database.py`, `README.md` | Import/start the app without importing Calculator modules or initializing the root app. |
| KAN26-02 | Define the task table, request/response schemas, allowed statuses, and repository operations. | KAN26-01 | `src/models.py`, `src/schemas.py`, `src/repository.py` | Unit-test repository create/list/get/update/delete and persisted IDs using a temporary SQLite database. |
| KAN26-03 | Implement POST/GET/PATCH/DELETE task routes and required success responses. | KAN26-02 | `src/routers/tasks.py`, `src/main.py` | API tests for AC-001 through AC-005. |
| KAN26-04 | Add verification for FR-006, FR-007, and FR-008 after the proposed cases are confirmed. | KAN26-02, KAN26-03 | `tests/test_tasks.py` | Proposed: IDs are assigned and increase across creates; omitted status defaults to `todo` and unsupported values are rejected; missing IDs return HTTP 404 with the exact FR-008 message for applicable endpoints. Confirm endpoint coverage and validation response details before treating these as approved criteria. |
| KAN26-05 | Run the isolated project test suite and document requirement traceability and local setup. | KAN26-01 through KAN26-04 | `projects/kan-26-task-api/tests/`, `projects/kan-26-task-api/README.md`, `docs/sessions/KAN-26/plans/verification.md` | Run pytest from the project directory; record actual results mapped to FR/AC IDs. |

## Scope Constraints

- Use FastAPI and SQLite as specified by Jira.
- Keep app, runtime dependencies, tests, and database under the isolated KAN-26 project directory.
- Do not add a frontend, authentication, deployment, history, pagination, or other unapproved features.
- Preserve all KAN-25 Calculator files and workflow records.
- Do not begin implementation until this plan and the proposed FR-006 through FR-008 verification cases are explicitly approved.

## Approval Status

Status: AWAITING HUMAN APPROVAL

The requirements and separate-project decision are approved. Please review the proposed verification cases for FR-006 through FR-008 and approve or request changes to this plan before implementation.