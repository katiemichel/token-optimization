# Demo 02 — General-purpose model on execution work

**Time:** ~8 minutes
**Recommended model:** a **general-purpose / Codex** tier model (e.g. **GPT-5.3-Codex**, **GPT-5 mini**, or **Claude Sonnet 4.6**)
**Contrast model (optional):** a **reasoning** model — to show wasted thought on clear-spec work

## The setup

You're going to build a small `Cart` module from a written spec. The spec is detailed enough that any general-purpose model should produce a working implementation in one or two turns. The tests already encode the behavior — they're red right now.

- [`SPEC.md`](SPEC.md) — the spec the agent will work from.
- [`cart.py`](cart.py) — a near-empty stub. Functions exist but `raise NotImplementedError`.
- [`test_cart.py`](test_cart.py) — failing tests that describe the intended behavior.

This is the sweet spot for general-purpose / Codex tier models per the [model cheatsheet](../../docs/model-cheatsheet.md): the plan is clear, the agent just needs to execute it cleanly.

## Run it

```bash
pytest demos/02-execution -q   # red — that's expected
```

## The exact prompt to paste

> Select **GPT-5.3-Codex** (or **GPT-5 mini** / **Claude Sonnet 4.6**) in the model picker.

> Implement the functions in #file:demos/02-execution/cart.py to match #file:demos/02-execution/SPEC.md.
>
> When you're done:
> - All tests in demos/02-execution must pass: `pytest demos/02-execution -q`
> - `ruff check demos/02-execution` must pass.
> - Do not add new public functions. Do not change function signatures.
>
> Stop as soon as both commands are green.

## What to notice

- The agent reads the spec, writes the code, runs the tests, and stops. No extras.
- "Stop as soon as both commands are green" is doing real work — without it, agents tend to add helpers or propose additional tests.
- Note how fast this feels compared to Demo 03. Clear spec + execution model = fast loop.

## Reset before the next demo

> Click "New chat" in Copilot Chat. Demo 03 must start clean.
