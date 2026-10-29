# KAN-27 Square Root Implementation Plan

## Preconditions

- KAN-27 requirements and proposed scenarios V-001 through V-008 are approved.
- KAN-27 is an enhancement to the KAN-25 calculator.
- Round half-up to at most eight fractional decimal places and trim trailing zeros, as explicitly approved by the user.
- Keep the existing `/calculate` API contract and all KAN-26 files unchanged.

## Recommended Branch

`feature/KAN-27-square-root`

## Tasks

| Task ID | Task | Dependencies | Expected files | Verification |
|---------|------|--------------|----------------|--------------|
| KAN27-01 | Add a typed unary square-root request/response contract and pure decimal square-root function with negative-input validation and agreed formatting. | None | `src/schemas.py`, `src/calculator.py` | Unit-test zero, perfect-square integer, perfect-square decimal, negative input, and precision formatting. |
| KAN27-02 | Add `POST /sqrt` returning the result or the exact negative-input error; preserve `/calculate` behavior. | KAN27-01 | `src/routers/calculator.py` | API tests for success, negative HTTP 422/message, existing binary routes unchanged, and response under one second for representative inputs. |
| KAN27-03 | Add a mouse/touch-accessible `√` button. Send the current value to `/sqrt`; on success update the result and first operand while retaining the second operand and selected operation. | KAN27-02 | `src/static/index.html`, `src/static/app.js`, `src/static/style.css` | Browser-check button label/action, result replacement, negative feedback, and chaining the root into a binary calculation. |
| KAN27-04 | Add automated tests mapped to approved Jira requirements and verification scenarios. | KAN27-01 through KAN27-03 | `tests/test_calculator.py` | Run full pytest suite; record actual results. Keep V-001 through V-008 identified as approved derived scenarios, not Jira ACs. |
| KAN27-05 | Update session verification and release documentation. | KAN27-04 | `docs/sessions/KAN-27/plans/verification.md`, `docs/sessions/KAN-27/plans/changelog.md` | Map each FR/NFR to executed tests and browser evidence. |

## Proposed Verification Cases

- V-001: `sqrt(25)` displays `5`.
- V-002: `sqrt(20.25)` displays `4.5`.
- V-003: `sqrt(0)` displays `0`.
- V-004: Negative input shows the exact Jira error and leaves the app responsive.
- V-005: Successful root replaces the current result/operand without reload.
- V-006: Root result can be used in a subsequent binary calculation.
- V-007: Representative calculation completes within one second and formats to the approved precision.
- V-008: `√` is clearly labeled and works with mouse/touch interaction.

## Approval Status

Status: APPROVED

Approved explicitly by the user on 2026-10-28, including round-half-up, a maximum of eight fractional decimal places, and trimming trailing zeros.