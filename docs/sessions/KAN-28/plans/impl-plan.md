# KAN-28 Implementation Plan

## Status and scope

Planning is based on the human-approved
`docs/sessions/KAN-28/plans/requirements.md`,
`docs/sessions/KAN-28/plans/architecture.md`,
`docs/sessions/KAN-28/plans/design-review.md` (approved), and canonical evidence in
`context/sessions/KAN-28.json`.

The requirements' source provenance is direct reading of actual issue content
from the user's authenticated shared Jira browser. This plan does not claim
Jira MCP retrieval. Scope is limited to the approved square-root behavior and
its integration with the existing calculator; existing arithmetic behavior is
not to be changed.

The user approved 8 decimal places with `ROUND_HALF_UP`, a module-level
`SQUARE_ROOT_PRECISION = 8` constant in `src/calculator.py`, and the browser
√ activation-to-result-display boundary for NFR-001. These decisions are
recorded in the approved requirements and architecture artifacts.

## Approval and blocker status

The implementation plan and the following KAN28-PLN-01 decisions are approved:

- Precision: 8 decimal places with `ROUND_HALF_UP`, configured through the
  named code-level constant `SQUARE_ROOT_PRECISION = 8`; no new configuration
  infrastructure.
- Performance boundary: from √ activation in the browser until the result is
  displayed in the browser.

KAN28-PLN-01 is complete. Other unspecified interaction details remain
bounded by the approved requirements and architecture; do not broaden scope.

## Ordered tasks

| Task ID | Task | Dependencies | Expected files | Verification point |
|---|---|---|---|---|
| KAN28-PLN-01 | **Resolve and approve implementation blockers.** Completed: the user approved precision, rounding/configuration, and the one-second measurement boundary; the approved requirements and architecture record those decisions. | None; blocks all implementation tasks | `docs/sessions/KAN-28/plans/requirements.md`, `docs/sessions/KAN-28/plans/architecture.md`, `docs/sessions/KAN-28/plans/design-review.md` | Decisions are explicit, consistent across artifacts, and human-approved. **Completed.** |
| KAN28-PLN-02 | **Align and verify square-root service behavior.** Reconcile existing logic and API contract with the approved decisions. Preserve decimal-text request/result handling, support positive integers, positive decimals, and zero, and retain the exact specified negative-input message and non-crashing response. Change only what is needed; do not alter existing arithmetic behavior. | KAN28-PLN-01 | `src/calculator.py`, `src/routers/calculator.py`, `src/schemas.py` (only if contract changes are necessary), `tests/test_calculator.py` | Focused API/domain tests cover supported inputs, zero, negative input and exact error text, selected precision/rounding behavior, and result formatting. |
| KAN28-PLN-03 | **Align and verify browser interaction.** Confirm the √ control reads the active value, displays/replaces it with the API result immediately, and makes that result available as the first operand for the existing subsequent-calculation flow. Display the required negative-input message without leaving the UI unusable. Keep mouse/touch access and the clear √ label. | KAN28-PLN-01, KAN28-PLN-02 | `src/static/app.js`, `src/static/index.html`, `src/static/style.css` (only if needed), `tests/test_calculator.py` (only if adding applicable page/asset assertions) | Verify successful and negative-input UI flows, result handoff to a later calculation, and visible/control access via mouse or touch. Do not add unspecified accessibility requirements. |
| KAN28-PLN-04 | **Verify the agreed one-second requirement.** Measure the operation using only the start/end boundaries approved in KAN28-PLN-01. Use representative supported inputs and report the measurement method/results; avoid introducing a brittle timing assertion unless the agreed method supports one. | KAN28-PLN-01, KAN28-PLN-02, KAN28-PLN-03 | `tests/test_calculator.py` only if a suitable deterministic verification belongs there; otherwise no additional source file is presumed | Evidence shows completion within one second under the agreed measurement boundary and records the method used. |
| KAN28-PLN-05 | **Run focused and regression verification; review scope.** Run the project test suite and inspect the final diff to ensure only approved square-root behavior and necessary tests changed. | KAN28-PLN-02, KAN28-PLN-03, KAN28-PLN-04 | No additional files expected; existing test suite, including `tests/test_calculator.py` | Focused square-root checks and full regression suite pass; no unrelated arithmetic behavior or unrelated worktree changes are included. |

## Suggested branch

`feature/KAN-28-square-root`

Recommendation only; do not create the branch as part of planning.

## Handoff

This plan was explicitly approved by the user. KAN28-PLN-01 decisions are
resolved and approved. Implementation proceeded under KAN28-PLN-02 through
KAN28-PLN-05; release remains subject to the separate GitHub push-protection
and PR approval gates recorded in the canonical session.
