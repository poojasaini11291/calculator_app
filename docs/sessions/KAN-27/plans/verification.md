# KAN-27 Verification Report

## Requirement Results

| Requirement | Verification | Result |
|-------------|--------------|--------|
| FR-001 | Static page test checks the visible √ control and accessible name. | PASS |
| FR-002 | API tests cover 25, 20.25, and 0. | PASS |
| FR-003 | API tests cover exact roots and `sqrt(2)` formatted to eight places. | PASS |
| FR-004 | Negative API input returns HTTP 422 and the exact Jira error string. | PASS |
| FR-005 | Browser check confirms result output and first operand are updated. | PASS |
| FR-006 | Browser check confirms `sqrt(25)` then addition with retained second operand 2 yields 7. | PASS |
| NFR-001 | Three local `/sqrt` requests measured approximately 46.80 ms, 7.68 ms, and 4.09 ms. | PASS |
| NFR-002 | Decimal test cases and eight-place `sqrt(2)` result match approved formatting. | PASS |
| NFR-003 | Browser accessibility snapshot reports a `Square root` button with visible `√`; mouse interaction verified. | PASS |

## Test Execution

- Command: `python -m pytest -q`
- Result: 14 passed, 0 failed.
- Warnings: Two upstream Starlette/httpx TestClient deprecation warnings; tests pass.
- Browser: Verified square root, first-operand replacement, retained second operand, chained binary addition, negative-input error, and eight-place output.
- Response-time sample: Three local API requests were each below one second.

## Notes

- V-001 through V-008 are user-approved derived verification scenarios; Jira did not provide a numbered acceptance-criteria section.
- The custom automation-tester profile was not independently launchable from this chat; tests and browser checks were run directly and are reported with observed results.