# Requirements Document

## 1. Jira Story Details

- Jira Story Key: KAN-26
- Jira Story URL: https://poojasaini11291.atlassian.net/browse/KAN-26
- Summary: Task Management REST API — Requirements
- Issue Type: Task
- Priority: Medium
- Status: To Do
- Linked issues: None returned by Jira.

## 2. Project Objective

Build a simple Task Management REST API that allows users to create, view, update, and delete tasks, persists tasks using SQLite, and exposes a REST interface through FastAPI.

## 3. Original User Story

As a user, I want to create, view, update and delete tasks, so that I can manage my daily activities.

## 4. Functional Requirements

- FR-001: The system shall allow a user to create a task with title, description, and status.
- FR-002: The system shall return a list of all tasks.
- FR-003: The system shall return a single task by its ID.
- FR-004: The system shall allow a user to partially update a task (title, description, or status).
- FR-005: The system shall allow a user to delete a task by its ID.
- FR-006: Each task shall have an auto-incremented integer ID assigned by the system.
- FR-007: Task status shall be restricted to `todo`, `in_progress`, or `done`; the supplied data model gives `todo` as the default.
- FR-008: When a task ID does not exist, the API shall return HTTP 404 with `Task with ID {id} does not exist`.

## 5. Non-Functional Requirements And Technology

Jira does not provide separately numbered non-functional requirements. Its project objective specifies:

- Python and FastAPI for the REST API.
- SQLite persistence.
- A clean REST interface.

No additional performance, availability, authentication, deployment, or security requirements were supplied in the story.

## 6. Data Model

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | integer | System-assigned | Auto-incremented on create. |
| title | string | Yes | Supplied by user. |
| description | string | Yes | Supplied by user. |
| status | string | Yes | `todo`, `in_progress`, or `done`; default `todo`. |

## 7. API Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/tasks` | Create a task. |
| GET | `/tasks` | Retrieve all tasks. |
| GET | `/tasks/{id}` | Retrieve a task by ID. |
| PATCH | `/tasks/{id}` | Partially update a task. |
| DELETE | `/tasks/{id}` | Delete a task by ID. |

## 8. Acceptance Criteria

- AC-001 (FR-001): `POST /tasks` with valid fields returns HTTP 201 and a task including its assigned ID.
- AC-002 (FR-002): `GET /tasks` returns HTTP 200 with a JSON array, including an empty array when no tasks exist.
- AC-003 (FR-003): `GET /tasks/{id}` returns HTTP 200 with the task object when found.
- AC-004 (FR-004): `PATCH /tasks/{id}` returns HTTP 200; only supplied fields change and other fields remain unchanged.
- AC-005 (FR-005): `DELETE /tasks/{id}` returns HTTP 200 with a confirmation message.

Jira does not provide separately numbered acceptance criteria for FR-006, FR-007, or FR-008. Their behavior is present in the functional requirements/data model above, but should be confirmed or supplemented before test planning rather than converted into invented criteria.

## 9. Assumptions

- None added. The requirements above are transcribed from the retrieved Jira issue.

## 10. Dependencies

- Python runtime.
- FastAPI.
- SQLite.
- No external service dependency is stated in Jira.

## 11. Out Of Scope

Jira does not specify an out-of-scope list. Do not infer extra capabilities or exclusions during implementation planning without clarification.

## 12. Requirements Traceability

| Jira Story | Requirement ID | Acceptance Criteria | Description |
|------------|----------------|---------------------|-------------|
| KAN-26 | FR-001 | AC-001 | Create a task with title, description, and status. |
| KAN-26 | FR-002 | AC-002 | List tasks; return an empty array when none exist. |
| KAN-26 | FR-003 | AC-003 | Retrieve one task by ID. |
| KAN-26 | FR-004 | AC-004 | Partially update only supplied fields. |
| KAN-26 | FR-005 | AC-005 | Delete a task and return a confirmation. |
| KAN-26 | FR-006 | Not separately specified | Assign an auto-incremented integer ID. |
| KAN-26 | FR-007 | Not separately specified | Restrict status values and default to `todo`. |
| KAN-26 | FR-008 | Not separately numbered | Return the specified 404 message for a missing ID. |

## 13. Clarification Summary

- Jira KAN-26 was retrieved read-only. It is a Task Management REST API story with eight functional requirements and five explicitly listed acceptance criteria.
- Scope clarification: the user approved KAN-26 as a separate project from the completed KAN-25 Calculator. The proposed implementation location is `projects/kan-26-task-api/` within this repository; KAN-25 source and dependencies will remain untouched.
- Acceptance-criteria clarification: Jira supplies no separately numbered criteria for FR-006 through FR-008. Proposed test cases are listed in the implementation plan for explicit review; they are not represented as Jira-supplied criteria.

## 14. Approval Status

Status: APPROVED

Approved explicitly by the user on 2026-10-28, including the decision that KAN-26 is a separate project. The proposed verification detail for FR-006 through FR-008 remains subject to review at implementation-plan approval.