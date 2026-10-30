# KAN-28 Verification

## Status

**VERIFIED for the executed automated and browser checks.** Both pytest
commands passed. Local browser interaction verified square-root success,
negative-input messaging, and reuse of the result in a subsequent calculation.
Four browser activation-to-display measurements were below the one-second
target. Touch-device interaction was not independently exercised.

The developer added a served-JavaScript source-contract assertion to
`tests/test_calculator.py`. Passing that assertion is not equivalent to
executing the frontend in a browser.

## Requirement-to-test coverage

| Requirement | Existing focused test(s) / evidence | Coverage type | Actual result |
|---|---|---|---|
| FR-001 | `test_square_root` (parameterized); `test_calculator_page_and_assets_are_served` | API test and served-page/source contract, plus local browser interaction | Automated tests PASS; browser mouse activation of √ with input 81 displayed 9 |
| FR-002 | `test_square_root` (positive integer, positive decimal, zero inputs) | API test | Automated tests PASS |
| FR-003 | `test_square_root`; `test_square_root_precision_is_eight_decimal_places`; `test_square_root_rounds_half_up_to_eight_decimal_places` | API assertions and precision policy assertion | Automated tests PASS |
| FR-004 | `test_square_root_of_negative_returns_exact_error`; `test_square_root_frontend_error_flow_contract_clears_displayed_result` | API test and served-JavaScript source contract, plus local browser interaction | Automated tests PASS; browser input -9 displayed exactly the specified error and the page remained usable |
| FR-005 | `test_calculator_page_and_assets_are_served`; `test_square_root_frontend_error_flow_contract_clears_displayed_result` | Markup/asset and JavaScript source assertions, plus local browser result-display checks | Automated tests PASS; browser displayed 9 for √81 and 12 for subsequent 9 + 3 |
| FR-006 | `test_square_root_result_can_be_used_in_next_operation` | API integration test | Automated tests PASS |
| NFR-001 | `test_calculator_page_and_assets_are_served` checks that the served script contains the named Performance API measure | Source-contract assertion plus live browser timings from √ activation to result display | PASS in four local browser trials: 28.8–34.7 ms |
| NFR-002 | `test_square_root`; `test_square_root_rounds_half_up_to_eight_decimal_places` | API result/rounding assertions | Automated tests PASS |
| NFR-003 | `test_calculator_page_and_assets_are_served` checks the √ label/button markup | Served-markup assertion and live mouse activation | PASS for visible √ button and mouse; touch-device interaction not independently tested |

The source-contract assertion for the negative-input flow inspects served
JavaScript for the active-value selection and clearing stale displayed result
and hint on failure. It does **not** execute JavaScript in a browser. Similarly,
the performance source assertion confirms only that a measurement call is
present; it does not demonstrate the one-second target.

## Commands and actual execution results

| Command | Actual output/result |
|---|---|
| `python -m pytest tests/test_calculator.py -k "square_root" -q` | PASS — exit 0; 9 passed, 7 deselected; 2 deprecation warnings; 0.32s on the clean-base branch. |
| `python -m pytest -q` | PASS — exit 0; 16 passed; 2 deprecation warnings; 0.61s on the clean-base branch. |

These are the actual execution results reported from the parent session. The
deprecation warnings are recorded; no warning-free result is claimed.

## Browser/UI and NFR-001

The calculator was served locally at `http://127.0.0.1:8765/` and exercised
through the browser:

- Mouse activation with input `81` displayed `9`; the measured
  activation-to-display interval was 34.7 ms.
- Subsequent calculation using the square-root result (`9 + 3`) displayed
  `12`.
- Negative input `-9` displayed exactly
  `Invalid input. Square root of a negative number is not supported.` and the
  page remained usable.
- Additional browser trials produced `sqrt(0) = 0` in 34.7 ms,
  `sqrt(20.25) = 4.5` in 30.4 ms, and
  `sqrt(123456789) = 11111.11106056` in 28.8 ms.

The measurements use the approved browser √ activation-to-result-display
boundary and the app's Performance API measurement after the result has passed
through two animation frames. All four observed durations were below one
second. These are local browser observations, not a guarantee for other
devices or environments. Touch-device interaction was not separately tested.

## Verification summary

- Focused pytest suite: **PASS** — 9 passed, 7 deselected, 2 deprecation
  warnings, 0.32s on the clean-base branch.
- Full project pytest suite: **PASS** — 16 passed, 2 deprecation warnings,
  0.61s on the clean-base branch.
- Local browser success, negative-input, and subsequent-calculation checks:
  **PASS**.
- NFR-001: **PASS in four local trials**, observed range 28.8–34.7 ms for the
  approved boundary.
- Touch-device interaction: **not independently tested**.
