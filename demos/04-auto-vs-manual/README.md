# Demo 04 — Auto vs. manual, head-to-head

**Time:** ~10 minutes
**This demo runs no new code.** It re-runs the prompts from demos 01–03 through **Auto** and compares results to the deliberate manual picks.

## Why this matters

Auto in VS Code Copilot Chat is **task-optimized and intent-based** — it evaluates the complexity of each turn and routes to the model best suited for that intent, while also accounting for real-time system health. It even routes along **cache boundaries** to avoid the cost of mid-session model swaps.

So the question is no longer "is Auto good enough?" It's: **for a mixed-task day, does Auto match or beat what I'd pick by hand — without me having to think about it?**

## How to run it

You'll re-run three of the prompts you already used. Each one starts from a clean state.

> Tip: if your VS Code layout supports it, open two chat panes side-by-side and run Auto on the left, manual pick on the right.

### Round 1 — lightweight task (Demo 01 prompt)

1. **Reset Demo 01.** From a terminal:
   ```bash
   git checkout demos/01-lightweight/messy.py
   ```
2. Start a new chat. Set the model to **Auto**.
3. Paste this prompt:

   > Open #file:demos/01-lightweight/messy.py.
   >
   > Refactor it for readability without changing behavior:
   > - Add concise docstrings to every public function (one line each).
   > - Use built-in generics (list[int], dict[str, int]) instead of typing.List etc. Remove the typing import if it becomes unused.
   > - Use descriptive parameter names.
   > - Make `ruff check demos/01-lightweight` pass.
   >
   > Do not change function names, signatures (other than parameter names), or behavior. Do not add new functions. Run `pytest demos/01-lightweight -q` and `ruff check demos/01-lightweight`.
   > Stop as soon as both commands are green.
4. Note: which model did Auto route to? (Hover over the assistant response in Copilot Chat.) How does the diff compare to the lightweight-model run from Demo 01?

### Round 2 — execution task (Demo 02 prompt)

1. **Reset Demo 02.**
   ```bash
   git checkout demos/02-execution/cart.py
   ```
2. Start a new chat. Set the model to **Auto**.
3. Paste this prompt:

   > Implement the functions in #file:demos/02-execution/cart.py to match #file:demos/02-execution/SPEC.md.
   >
   > When you're done:
   > - All tests in demos/02-execution must pass: `pytest demos/02-execution -q`
   > - `ruff check demos/02-execution` must pass.
   > - Do not add new public functions. Do not change function signatures.
   >
   > Stop as soon as both commands are green.
4. Note: did Auto pick the same tier as you did manually in Demo 02? How does turn time / number of tool calls compare?

### Round 3 — reasoning task (Demo 03 prompt)

1. **Reset Demo 03.**
   ```bash
   git checkout demos/03-reasoning/inventory.py
   ```
2. Start a new chat. Set the model to **Auto**.
3. Paste this prompt:

   > The test `test_each_warehouse_is_independent` in #file:demos/03-reasoning/test_inventory.py is failing.
   >
   > Diagnose the root cause across #file:demos/03-reasoning/inventory.py and #file:demos/03-reasoning/reporting.py. Explain the cause in one paragraph before changing any code, then apply the smallest fix at the root. Do not modify the test.
   >
   > Run `pytest demos/03-reasoning -q`. Stop when all tests are green.
4. Note: did Auto pick a reasoning-tier model? Did it find the root cause, or fix the symptom?

## Scorecard

Use [`scorecard.md`](scorecard.md) as a template — fill it in live and project it. The participants see Auto vs. manual scored on the same three tasks in the same room. That's the demo.

## What to notice

- Check which model Auto routed to — hover over the response to see. Does it match the tier you picked manually in demos 01–03?
- On the execution round, Auto should stay in general-purpose tier even across a long session. That's cache-boundary routing working as intended.
- Where Auto doesn't match your manual pick, ask: was the manual pick actually better, or was it habit?

## When to override Auto

- Architecture / naming / boundary decisions → pin a reasoning model.
- Long sequences of nearly-identical edits → pin a lightweight model.
- Benchmarks, reproducibility, or regression bisects → pin a specific model.
- Everything else → trust Auto.

## Reset before the next demo

> Click "New chat", and run `git checkout demos/` from the terminal to reset all demo files.
