# Design Review

## Review Summary

The design extends the completed calculator with unary square root while preserving existing binary behavior. A dedicated `/sqrt` endpoint keeps the current `/calculate` contract stable; the UI writes the successful result back to the current operand so it can feed a subsequent operation.

## Requirement Coverage

| Requirement | Design coverage |
|-------------|-----------------|
| FR-001 | Add a clearly labeled `√` UI action. |
| FR-002 | Use a decimal input schema supporting positive integers, decimals, and zero. |
| FR-003 | Return and display the result using an agreed maximum of eight fractional decimal places. |
| FR-004 | Reject negative input with the exact Jira message and no server crash. |
| FR-005 | Update the result area immediately and replace the current operand. |
| FR-006 | Preserve the computed root as the current operand for the existing binary operation. |
| NFR-001 | Local calculation endpoint is expected to meet the one-second target. |
| NFR-002 | Decimal calculation and explicit formatting preserve agreed result accuracy. |
| NFR-003 | Use a visible `√` button operable with mouse and touch. |

## Findings

1. **Precision policy resolved:** Jira does not define rounding mode or trailing-zero display. The user approved round-half-up to at most eight fractional places and trimming trailing zeros before implementation.
2. **No Jira acceptance criteria:** The approved V-001 through V-008 scenarios are derived verification examples, not Jira-provided ACs; retain this distinction in tests and reports.

## Design Decisions

- Add `POST /sqrt` rather than altering the existing two-operand `/calculate` request contract.
- Use the first/current operand as the square-root input.
- On success, update the result output and first operand, preserving the second operand and selected binary operation for chaining.
- On negative input, display the exact Jira error without changing the existing calculator result or crashing.
- Do not add a database or external dependency.

## Final Review Status

APPROVED. No architecture blockers remain. The implementation plan and precision-formatting rule were explicitly approved before development.