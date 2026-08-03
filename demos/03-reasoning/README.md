# Demo 03 — Reasoning model earns its cost

**Time:** ~10 minutes
**Recommended model:** a **reasoning** tier model (e.g. **Claude Opus 4.7** or **GPT-5.5**)
**Contrast model (start with this!):** a **lightweight** model — to show the failure mode

## The setup

There's a bug in this small two-file inventory module. The failing test in [`test_inventory.py`](test_inventory.py) describes the symptom — adding an item to warehouse A somehow makes it appear in warehouse B.

The bug is **subtle and cross-file**. There's a real temptation to "fix" the symptom inside the test, or to add a defensive check that masks the root cause. A reasoning model is more likely to look at where the data structure is created in the first place; a lightweight model is more likely to patch the obvious surface.

- [`inventory.py`](inventory.py) — defines warehouses and item operations.
- [`reporting.py`](reporting.py) — generates a report, calls into `inventory`.
- [`test_inventory.py`](test_inventory.py) — has one failing test.

## Run it

```bash
pytest demos/03-reasoning -q
```

You'll see one failing test. The error message is loud but the cause is **not** in `test_inventory.py`.

## Step 1 — try the lightweight model first

> Select a **lightweight** model (e.g. **Claude Haiku 4.5**).

> The test `test_each_warehouse_is_independent` in #file:demos/03-reasoning/test_inventory.py is failing.
> Run it, identify the root cause, and fix it. Do not modify the test.
> Stop as soon as the failing test passes.

### What you're likely to see
- A surface-level fix in `add_item` (deep-copying the items list on read).
- A defensive check in `generate_report`.
- A docstring warning the user to "always pass `items=[]` explicitly."
- A fix that makes the test pass but **doesn't fix the underlying bug** — easy to demonstrate by adding a third warehouse and reproducing the leak.

**Don't rescue it.** The wrong fix is the demo.

## Step 2 — switch to a reasoning model

> Reset chat. Select a **reasoning** model (e.g. **Claude Opus 4.7** or **GPT-5.5**).

> The test `test_each_warehouse_is_independent` in #file:demos/03-reasoning/test_inventory.py is failing.
>
> Diagnose the root cause across #file:demos/03-reasoning/inventory.py and #file:demos/03-reasoning/reporting.py. Explain the cause in one paragraph before changing any code, then apply the smallest fix at the root. Do not modify the test.
>
> Run `pytest demos/03-reasoning -q`. Stop when all tests are green.

### What you should see
- The agent reads both files before changing anything.
- It identifies that `add_warehouse(name, items=[])` uses a **mutable default argument** — every warehouse created without an explicit `items` shares the same list object.
- The fix is one line: `items=None` + `items = [] if items is None else items` inside the function.

## What to notice

- The lightweight model patches the surface. The reasoning model reads both files and finds the root cause.
- Same prompt, same failing test — different depth of diagnosis.
- After the fix, run the tests. Try adding a third warehouse to confirm the fix is at the root, not the symptom.

## Reset before the next demo

> Click "New chat" in Copilot Chat.
