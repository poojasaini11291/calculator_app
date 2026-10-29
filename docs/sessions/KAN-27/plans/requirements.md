# Requirements Document

## 1. Jira Story Details

- Jira Story Key: KAN-27
- Jira Story URL: https://poojasaini11291.atlassian.net/browse/KAN-27
- Summary: Calculator - GHCP — Requirements_Test
- Issue Type: Task
- Priority: Medium
- Status: To Do
- Linked issues: None returned by Jira.

## 2. Project Objective

Extend the calculator to calculate and display the square root of a valid non-negative number, handle negative input with the specified error, and allow the result to be used in subsequent calculations.

## 3. Original User Story

As a user I want to calculate the square root of a number using the calculator so that I can quickly obtain mathematical results without manual calculation.

## 4. Functional Requirements

- FR-001: The calculator shall provide a square-root button labeled `√`.
- FR-002: The calculator shall accept positive integers, positive decimal numbers, and zero as square-root inputs.
- FR-003: When the user selects the square-root function, the calculator shall display the square-root result with up to the configured decimal precision. Jira gives 8 decimal places as an example but does not state the final configured value.
- FR-004: For a negative input, the calculator shall display exactly: `Invalid input. Square root of a negative number is not supported.` The application shall not crash or freeze.
- FR-005: The calculated result shall replace the existing value in the display area and be visible immediately after calculation.
- FR-006: The user shall be able to use the square-root result for subsequent calculations.

## 5. Non-Functional Requirements

- NFR-001: Square-root calculation shall complete within 1 second.
- NFR-002: The calculator shall return mathematically accurate results up to the supported precision.
- NFR-003: The square-root button shall be clearly labeled `√` and accessible via mouse/touch interaction.

## 6. Proposed Verification Scenarios

Jira does not provide a numbered acceptance-criteria section. The following are proposed examples derived from the requirements, not original Jira acceptance criteria. Confirm or revise them before planning tests:

- V-001 (FR-001, FR-003): Enter 25, invoke `√`, and display 5.
- V-002 (FR-002, FR-003): Enter 20.25, invoke `√`, and display 4.5.
- V-003 (FR-002, FR-003): Enter 0, invoke `√`, and display 0.
- V-004 (FR-004): Enter a negative value, invoke `√`, show the exact specified error, and keep the application responsive.
- V-005 (FR-005): Confirm the square-root result replaces the current displayed value without waiting for a page reload.
- V-006 (FR-006): Use a square-root result as an operand in a following arithmetic operation and verify the resulting value.
- V-007 (NFR-001, NFR-002): Confirm an ordinary calculation completes within 1 second and is correct to the approved precision.
- V-008 (NFR-003): Confirm `√` is visibly labeled and operable with mouse and touch input.

## 7. Assumptions

- The story appears to enhance the KAN-25 Calculator application based on its summary and description, but Jira returned no linked issue. Confirm that relationship before finalizing scope.
- A browser UI action is expected because the story refers to a visible button and calculator display; exact placement and interaction with the existing form are not specified.
- No precision value, rounding mode, or trailing-zero display rule is fixed by Jira.

## 8. Dependencies

- The existing calculator application and its result display, if KAN-27 is confirmed as its enhancement.
- No new external service or database requirement is stated.

## 9. Out Of Scope

Jira does not specify an out-of-scope list. Do not infer additional calculator functions or data persistence.

## 10. Requirements Traceability

| Jira Story | Requirement ID | Proposed Verification | Description |
|------------|----------------|-----------------------|-------------|
| KAN-27 | FR-001 | V-008 | Provide a clearly labeled square-root button. |
| KAN-27 | FR-002 | V-001, V-002, V-003 | Accept positive integer, positive decimal, and zero inputs. |
| KAN-27 | FR-003 | V-001, V-002, V-003, V-007 | Display accurate square-root result at agreed precision. |
| KAN-27 | FR-004 | V-004 | Show the exact negative-input error without crashing/freezing. |
| KAN-27 | FR-005 | V-005 | Replace the current displayed value immediately. |
| KAN-27 | FR-006 | V-006 | Allow the result to be used by a following calculation. |
| KAN-27 | NFR-001 | V-007 | Complete calculation within one second. |
| KAN-27 | NFR-002 | V-001, V-002, V-003, V-007 | Preserve mathematical accuracy to the approved precision. |
| KAN-27 | NFR-003 | V-008 | Provide a clear, mouse/touch-accessible `√` control. |

## 11. Clarification Summary

- Jira KAN-27 was retrieved read-only. It contains six functional requirements and three non-functional requirements; no explicit acceptance criteria or linked issues were returned.
- The user approved KAN-27 as an enhancement to KAN-25, approved the proposed verification scenarios V-001 through V-008, and confirmed the interaction: square root uses the current displayed value, replaces it, and leaves the result available for subsequent calculations.
- The user approved a maximum precision of eight decimal places, round-half-up, and trimming trailing zeros on 2026-10-28.

## 12. Approval Status

Status: APPROVED

Approved explicitly by the user on 2026-10-28, including the eight-place precision cap, round-half-up, trailing-zero trimming, and proposed verification scenarios V-001 through V-008.