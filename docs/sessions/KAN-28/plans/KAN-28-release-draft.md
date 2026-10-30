# KAN-28 Release Draft

**State:** The first push attempt was rejected by GitHub push protection
(GH013) because a pre-existing ancestor contained a credential. The flagged
GitHub PAT was subsequently rotated. The blocked local branch is preserved as
`feature/KAN-28-square-root-blocked-local`; an approved clean-history retry is
being prepared from `origin/main` on `feature/KAN-28-square-root`. KAN-28
planning artifacts are isolated under `docs/sessions/KAN-28/plans/` to
preserve existing `docs/plans/` files. The clean branch tests pass, but it has
not yet been committed, pushed, or opened as a PR. Merge remains unapproved.

## Changelog

- Add square-root calculation for nonnegative inputs, with an 8-decimal
  `ROUND_HALF_UP` policy and result reuse in subsequent calculations.
- Show the specified error for negative inputs and clear stale result content
  on the failure path.
- Add browser-side activation-to-display instrumentation for the approved
  performance boundary.

## PR Description

### Summary

Implement the KAN-28 square-root operation in the calculator, including
nonnegative input handling, approved precision/rounding behavior, negative
input messaging, and reuse of the result in a following calculation.

### Changes Made

- Implement the named `SQUARE_ROOT_PRECISION = 8` policy and
  `ROUND_HALF_UP` result rounding.
- Handle positive integers, positive decimals, and zero; report the specified
  exact error for negative input.
- Clear stale result and hint content when the square-root request fails.
- Measure browser √ activation through result display using the approved
  timing boundary.
- Add/retain API, precision, subsequent-operation, and served-JavaScript
  contract assertions as recorded in the verification artifact.

### Test Evidence

Executed and passed:

- `python -m pytest tests/test_calculator.py -k "square_root" -q` — exit 0;
  9 passed, 7 deselected; 2 deprecation warnings; 0.32s on the clean-base
  branch.
- `python -m pytest -q` — exit 0; 16 passed; 2 deprecation warnings; 0.61s
  on the clean-base branch.

Recorded local browser checks in `docs/sessions/KAN-28/plans/verification.md`:

- `√` on `81` displayed `9`; four activation-to-display measurements ranged
  from 28.8 ms to 34.7 ms.
- Reusing the result in `9 + 3` displayed `12`.
- `-9` displayed the specified error and the page remained usable.
- Additional observed results: `sqrt(0) = 0`, `sqrt(20.25) = 4.5`, and
  `sqrt(123456789) = 11111.11106056`.

The independent final code review in `docs/sessions/KAN-28/plans/code-review.md` reports PASS
with no actionable findings.

### Known Limitations

- Touch-device interaction was not independently tested.
- Browser timing values are local observations, not a guarantee for other
  devices or environments.
- The negative-flow and frontend assertions are served-JavaScript
  source-contract checks, not browser-executed automated tests; live browser
  checks are recorded separately.
- The code reviewer did not independently verify the complete Git worktree
  diff. Reviewers should inspect the final diff and confirm unrelated
  KAN-26/KAN-27/`.mcp` work is preserved and outside this change.
- Both pytest commands emitted two deprecation warnings; no warning-free
  result is claimed.

### Reviewer Checklist

- [ ] Confirm the final diff is limited to the intended KAN-28 changes and
      does not alter unrelated KAN-26/KAN-27/`.mcp` work.
- [ ] Verify 8-place `ROUND_HALF_UP` behavior and supported input classes.
- [ ] Confirm the exact negative-input message and stale-result clearing.
- [ ] Confirm the √ result can be used in a subsequent calculation.
- [ ] Review the recorded browser timing boundary/results and note that
      touch-device interaction was not tested.
- [ ] Review the automated test outcomes and recorded deprecation warnings.

## Provenance and Workflow Gate

Jira story provenance is browser-read from the user's authenticated shared Jira
page; no Jira MCP retrieval was performed. The canonical KAN-28 session has
`workflow_id: null`; no workflow ID is asserted here. The user had explicitly
authorized creating the local branch, committing scoped KAN-28 files, pushing,
and creating a PR. The push failed because GitHub secret scanning detected a
credential in pre-existing ancestor commit `c005dee...` (`.mcp.json:11`); the
credential value is intentionally not reproduced. No remote branch or PR
exists according to the prior report; remote state has not been queried as part
of this update. The user has since explicitly confirmed that the identified
GitHub PAT has been rotated and separately authorized a clean-history branch
replay, push, and PR retry. This is separate from the prior PR-creation
approval. The token value was not provided or received, and no secret was
accessed. The authorized replay/push/PR retry has not been performed or
verified; PR creation remains incomplete. No Git or remote operation was
performed while recording these confirmations. Do not bypass or allowlist
push protection or edit `.mcp.json`. Obtain separate explicit approval before
any future merge; merge remains unapproved.
