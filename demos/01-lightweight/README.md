# Demo 01 — Lightweight model on lightweight work

**Time:** ~7 minutes
**Recommended model:** a **lightweight** tier model (e.g. **Claude Haiku 4.5** or **Gemini 3.5 Flash**)
**Contrast model (optional):** a **reasoning** tier model (e.g. **Claude Opus 4.7** or **GPT-5.5**) — to show over-engineering

## The setup

[`messy.py`](messy.py) is a small, working utility module that is intentionally:
- Inconsistently formatted
- Missing docstrings on public functions
- Using `from typing import List` and other pre-3.9 type spellings
- Using single-letter parameter names

The behavior is correct. The tests in [`test_messy.py`](test_messy.py) pass today and **must still pass after the refactor**.

## Run it

```bash
pytest demos/01-lightweight -q
ruff check demos/01-lightweight
```

`ruff` reports a handful of issues. `pytest` is green.

## The exact prompt to paste

> Select **Claude Haiku 4.5** (or another lightweight tier model) in the model picker.

> Open #file:demos/01-lightweight/messy.py.
>
> Refactor it for readability without changing behavior:
> - Add concise docstrings to every public function (one line each).
> - Use built-in generics (list[int], dict[str, int]) instead of typing.List etc. Remove the typing import if it becomes unused.
> - Use descriptive parameter names.
> - Make `ruff check demos/01-lightweight` pass.
>
> Do not change function names, signatures (other than parameter names), or behavior. Do not add new functions. When you're done, run `pytest demos/01-lightweight -q` and `ruff check demos/01-lightweight`.
>
> Stop as soon as both commands are green.

## What to notice

- Every change in the diff traces directly to a bullet in the prompt — nothing extra was added.
- No new class, split files, or verbose docstrings.
- Response time feels fast. This is what the right model for the task looks like.

## Reset before the next demo

> Click "New chat" in Copilot Chat. Demo 02 must start clean.
