# How entries are reviewed

`data/resources.json` is the source of truth. README tables, CSV and browser data are generated with `python3 scripts/build-directory.py`.

## Review levels

- `needs-review`: old entry or candidate; no current free-access claim is made.
- `docs-reviewed`: official pricing, documentation, repository or model card reviewed on `reviewed`. This is documentary evidence, not a live account test.

Do not advance a review date merely because a URL returns HTTP 200. Link availability cannot prove a free allowance, a working account or a usable model.

## Check an entry

1. Open the official source, avoiding search snippets and third-party quota lists.
2. Identify what is free: recurring tier, local software, one-time credits or trial. Do not relabel credits as a permanent tier.
3. Record restrictions: card, region, account eligibility, intended use, model-specific quotas and data handling when relevant.
4. Check software and model licenses separately. A free client can still require a paid API.
5. Set `reviewed` to the actual review date and `verification` to `docs-reviewed`. Include evidence in the PR. Account signup/testing is optional; say explicitly whether you performed it.
6. Regenerate views and run `python3 scripts/check-repo.py`.

`card` is `no`, `yes`, `conditional` or `unknown`. Use `unknown` when the official page does not establish the signup requirement. `kind` is `free-tier`, `local`, `credit`, `trial`, `paid` or `unconfirmed`.

For an entry that loses free access, keep a clear correction with `kind: paid`, or explain removal in the changelog. Review cloud entries frequently; suggest rechecks after 90 days. No claim of weekly human verification is made.
