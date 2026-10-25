# Make one AI resource easier to use

A single corrected limit, tested starter or improved translation is a useful contribution. No large PR required. See [small starter tasks](docs/GOOD_FIRST_ISSUES.md).

## Add or update a resource

1. Fork the repo and edit **`data/resources.json`**. Copy a nearby entry and use a unique lowercase hyphenated `id`.
2. Add an official source, a useful summary and the limitations. Follow the [review policy](docs/VERIFICATION.md). Local software qualifies; trials and credits must be labelled honestly. No affiliate links or sponsored placement.
3. Run:

   ```bash
   python3 scripts/build-directory.py
   python3 scripts/check-repo.py
   ```

4. Open a PR using `Add: Name`, `Update: Name` or `Fix: description`. Describe what you changed, link your evidence and say whether you actually tested an account/app. Commit the generated files too.

Do not edit generated README catalog tables, `data/resources.csv` or `assets/catalog-data.js` directly. You do not need to update every translation for a resource change: translated guides point to the shared catalog.

## Prefer an issue first?

Use [Add resource](https://github.com/abbosaliboev/free-ai-bible/issues/new?template=add-resource.yml), [Outdated information](https://github.com/abbosaliboev/free-ai-bible/issues/new?template=outdated-resource.yml) or [Translation](https://github.com/abbosaliboev/free-ai-bible/issues/new?template=translation.yml). English is useful for cross-language review; reports in other languages are welcome.

## Improve a starter

Include your OS, Python version, exact setup steps and result. Keep dependencies in the template's requirements file. Never commit API keys, audio recordings, model weights or personal documents.

## Translate

Translate the short guide in `translations/`, retain working relative links, and link to the shared catalog instead of copying quotas that can go stale. Arabic uses an RTL wrapper; code blocks remain LTR. Human language review is welcome for every guide.

## Recognition and conduct

Merged contributors appear in [GitHub's contributor list](https://github.com/abbosaliboev/free-ai-bible/graphs/contributors). Maintainers should name contributors in meaningful release notes. Be respectful, discuss the work and explain disagreements. Do not submit promotional spam or fabricated tests.

Directory contributions are under the MIT license. Listed projects retain their own licenses.
