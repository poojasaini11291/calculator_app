# KAN-28 Requirements

**Status: APPROVED BY HUMAN (the KAN28-PLN-01 policy decisions below; no other new approvals inferred)**

## JIRA details

| Field | Value |
|---|---|
| Key | KAN-28 |
| URL | https://poojasaini11291.atlassian.net/browse/KAN-28 |
| Title | Calculator - GHCP — Requirements_Test_1 |
| Priority | Not provided in Jira |
| Status | Not provided in Jira |
| Labels | Not provided in Jira |
| Linked issues | Not provided in Jira |
| Dependencies | Not provided in Jira |

### Source and provenance

The user confirmed that the story content below was retrieved directly from the actual issue in their authenticated shared Jira browser page and authorized requirements drafting from it. This browser-verified, user-provided issue content is the source for this document. No Jira integration or MCP retrieval was performed by this workflow, and Jira was not modified.

### Original user story

> As a user, calculate square root of a number to obtain results without manual calculation.

## Objective

Enable a user to calculate the square root of a supported nonnegative value and use the result in subsequent calculations, without manual calculation.

## Functional requirements

| ID | Requirement |
|---|---|
| FR-001 | Provide a √ operation and compute square roots for valid nonnegative values. |
| FR-002 | Accept positive integers, positive decimals, and zero as square-root inputs. |
| FR-003 | Round the computed result to 8 decimal places using `ROUND_HALF_UP`, and display it with up to 8 decimal places. |
| FR-004 | For negative input, display exactly `Invalid input. Square root of a negative number is not supported.` The application must not crash or freeze. |
| FR-005 | Replace the current display value with the result and show it immediately. |
| FR-006 | Allow the square-root operation result to be used in subsequent calculations. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-001 | Complete the square-root operation within 1 second, measured from activation of √ in the browser until the result is displayed in the browser. |
| NFR-002 | Calculate the result with mathematical accuracy to the supported precision. |
| NFR-003 | Make the operation clearly labeled √ and accessible via mouse/touch. |

## Human-approved policy decisions

The user explicitly approved these decisions in the latest instruction for
KAN28-PLN-01:

- **Precision and rounding:** Use 8 decimal places with `ROUND_HALF_UP`.
- **Precision configuration source:** Use the named code-level constant
  `SQUARE_ROOT_PRECISION = 8` in `src/calculator.py`. Repository evidence shows
  no settings/environment configuration framework; this is consistent with
  the existing module-level `SQUARE_ROOT_ERROR` constant in that file and the
  module-level constant in `src/main.py`. No new configuration infrastructure
  is specified.
- **NFR-001 timing boundary:** Measure from √ activation in the browser until
  the result is displayed in the browser.

These are human-approved policy decisions, not claims about Jira story text.

## Acceptance criteria

| ID | Given | When | Then | Traceability |
|---|---|---|---|---|
| AC-001 | A supported nonnegative value is available for the operation | The user invokes the √ operation | The application computes its square root | FR-001 |
| AC-002 | The input is a positive integer, a positive decimal, or zero | The user invokes the √ operation | The value is accepted as input for the operation | FR-002 |
| AC-003 | A valid nonnegative input has been entered | The square-root operation completes | The computed result is rounded to 8 decimal places using `ROUND_HALF_UP` and displayed with no more than 8 decimal places | FR-003 |
| AC-004 | The input is negative | The user invokes the √ operation | The display shows exactly `Invalid input. Square root of a negative number is not supported.` and the application does not crash or freeze | FR-004 |
| AC-005 | A current display value and a valid square-root input are present | The user invokes the √ operation | The current display value is replaced by the result, which is shown immediately | FR-005 |
| AC-006 | A square-root result has been produced | The user performs a subsequent calculation using that result | The result is available for that subsequent calculation | FR-006 |
| AC-007 | A supported nonnegative input is ready for the operation | The user activates √ in the browser | The result is displayed in the browser within 1 second of activation | NFR-001 |
| AC-008 | A supported nonnegative input is ready for the operation | The user invokes the √ operation | The computed result is mathematically accurate to the supported precision | NFR-002 |
| AC-009 | The square-root operation is presented to the user | The user accesses it via mouse or touch | The operation is clearly labeled √ and accessible using the chosen input method | NFR-003 |

## Assumptions and open points

- No additional assumptions have been used to define behavior beyond the supplied story.
- The details of how an operation result is selected or entered into a subsequent calculation are not specified.
- The story identifies mouse/touch access but does not specify further accessibility criteria.

## Dependencies

Not provided in Jira. No dependencies are inferred.

## Scope

This requirements artifact covers only the square-root behavior, supported input classes, result precision/display, negative-input handling, immediate display replacement, subsequent use, performance, accuracy, and mouse/touch access stated in KAN-28. Requirements for other operations or behaviors are not defined by the supplied story and are not added here.

## Traceability summary

| Source | Requirements | Acceptance criteria |
|---|---|---|
| KAN-28 user story and FR1–FR6 | FR-001–FR-006 | AC-001–AC-006 |
| KAN-28 NFR1–NFR3 | NFR-001–NFR-003 | AC-007–AC-009 |

## Clarification summary

The user explicitly approved the precision/rounding policy, its code-level
configuration source, and the NFR-001 browser timing boundary recorded above.
These decisions do not alter the browser-verified Jira story or imply approval
of other open interaction details or additional accessibility criteria.
