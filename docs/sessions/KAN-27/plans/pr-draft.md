# Pull Request Draft: KAN-27 Square Root

## Summary

Add the Jira KAN-27 square-root enhancement to the KAN-25 Calculator.

## Changes

- Add `POST /sqrt` using Decimal arithmetic and the specified negative-input error.
- Add a visible, accessible `√` button that updates the result and first operand for subsequent calculations.
- Preserve existing binary operations and the stateless, database-free design.

## Verification

- `python -m pytest -q`: 14 passed, 0 failed; two upstream deprecation warnings.
- Browser verified square-root result replacement, chaining, negative error, and precision output.
- Three measured local API requests completed in under one second.

## Known Limitations

- Browser interactions are manually verified; no browser automation framework was added.
- Code review and test stages were executed inline because custom agent profile launching is unavailable in this chat.

## Approval Status

Draft only. Await explicit approval before creating a GitHub pull request. Do not merge without separate final approval.