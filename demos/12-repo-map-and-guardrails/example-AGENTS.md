# Repository map

Python 3.11+ workshop demo repo for **model selection & token efficiency** with GitHub Copilot. Demos are intentionally small and didactic.

## Layout

- `demos/00–08/` — Core model-selection demos. Each is self-contained. **Do not import across demos.**
- `demos/09–13/` — Operations demos (cache, reasoning effort, tools/exclusions, repo map/guardrails, slash commands).
- `docs/model-cheatsheet.md` — one-page task→tier→model reference.
- `.github/copilot-instructions.md` — repo-scoped instructions (loaded every turn — keep short).

## Conventions

- Python 3.11+, **standard library only** unless a specific demo's README says otherwise.
- Lint with `ruff`, test with `pytest`. Both must pass before commits.
- Functions over classes unless state is genuinely required.
- Type hints on public functions; skip on one-line helpers.
- Each demo's `README.md` contains the **exact prompt** to paste during the workshop. Do not silently edit those prompts.

## Validation commands

```bash
pytest -q
ruff check .
```

## Known pitfalls (encoded from observed agent misses)

- Agents tend to cross-import between demo folders — don't. Each demo is its own world.
- Agents tend to add docstrings to one-line helpers. Don't. See conventions above.
- Agents tend to refactor "for cleanliness" in demo files. The mess in some demos is intentional pedagogy.
- Tests in a demo may be **failing on purpose** to drive the workshop. Read the demo README before "fixing" a red test.

## Output expectations for agents on this repo

- Be concise. No preamble like "Sure, I can help with that."
- Show diffs, not whole files, unless the file is new.
- Stop as soon as the requested validation commands are green.
