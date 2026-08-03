# Demo 05 — Research → Plan → Implement

**Time:** ~10 minutes
**You'll build:** a small CLI markdown link checker, in three phases, with **three different models** and **three separate chat sessions**.

This is the section §3 lesson from [the source doc](../../docs/improve-agent-quality-and-token-optimization.md) made concrete: phasing the work cuts wasted tokens, prevents context bloat, and lets you use the right capability at each step.

## What you'll build

A CLI:
```bash
python -m linkcheck demos/05-research-plan-implement/sample.md
```
that scans markdown files for broken local-file links and prints a report.

## What's in here

- [`sample.md`](sample.md) — a markdown file with a mix of working and broken links. This is the test input.
- [`linkcheck.py`](linkcheck.py) — empty stub. The agent will fill it in during the **Implement** phase.
- [`test_linkcheck.py`](test_linkcheck.py) — one failing smoke test. More tests will be written during the **Plan** phase.
- [`research-notes.md`](research-notes.md) — empty. The **Research** phase writes here.
- [`plan.md`](plan.md) — empty. The **Plan** phase writes here.

## The three phases

> **Critical:** start a **new chat** between each phase. Do not let earlier context bleed forward. That's the point of the demo.

---

### Phase 1 — Research (~2 min)
**Model:** a **general-purpose** model (e.g. **GPT-5.3-Codex** or **GPT-5 mini**).
**Goal:** explore the input, identify what kinds of links exist, surface edge cases.

> You are in research mode only. Do not write any implementation code.
>
> Read #file:demos/05-research-plan-implement/sample.md and produce a short, structured analysis covering:
> - Every distinct *kind* of link present (inline, reference, autolink, image, etc.).
> - Which links currently point to something that exists vs. something that doesn't.
> - Edge cases a link checker for this file would need to handle.
> - Suggested scope boundaries: what should be IN scope for a v1 CLI, and what should be explicitly OUT of scope.
>
> Write the analysis into #file:demos/05-research-plan-implement/research-notes.md. Keep it under 40 lines. No code.
>
> Stop after writing `research-notes.md`.

When the file is written, **scan it** and confirm it's grounded in the actual `sample.md`. If it's making things up, that's a red flag — call it out for the audience.

---

### Phase 2 — Plan (~3 min)
**Reset the chat.** Switch to a **reasoning** model (e.g. **Claude Opus 4.7** or **GPT-5.5**).

> You are in planning mode only. Do not write any implementation code.
>
> Read ONLY these files:
> - #file:demos/05-research-plan-implement/research-notes.md
> - #file:demos/05-research-plan-implement/test_linkcheck.py
>
> Produce a detailed implementation plan for a CLI at `python -m linkcheck <path>` that checks broken local-file links in a markdown file. The plan must include:
> - Public function signatures for `linkcheck.py` (with type hints).
> - A list of additional pytest test cases to add to `test_linkcheck.py`, covering the edge cases identified in research notes.
> - Explicit scope: what is in and what is out. Reference the research notes.
> - A short stop condition: what "done" means.
>
> Write the plan into #file:demos/05-research-plan-implement/plan.md. Use markdown headings. No code blocks longer than a single function signature.
>
> Stop after writing `plan.md`.

Read the plan with the audience. Point out: this plan was written *with no view of `sample.md`* — it depends entirely on the research summary. That's why phase isolation works.

---

### Phase 3 — Implement (~5 min)
**Reset the chat.** Switch to a **general-purpose** model (e.g. **GPT-5.3-Codex** or **Claude Sonnet 4.6**).

> Execution mode. Implement against the plan.
>
> Read ONLY:
> - #file:demos/05-research-plan-implement/plan.md
> - #file:demos/05-research-plan-implement/linkcheck.py
> - #file:demos/05-research-plan-implement/test_linkcheck.py
>
> Do the following:
> 1. Add the additional test cases from the plan into test_linkcheck.py.
> 2. Implement linkcheck.py so all tests pass.
> 3. Run `pytest demos/05-research-plan-implement -q` and `ruff check demos/05-research-plan-implement`. Both must be green.
>
> Stop as soon as both are green. Do not refactor beyond the plan. Do not add features the plan didn't list.

The agent should now be in tight loop with the guardrails (§4 of the doc). When `pytest` fails, watch how the agent adjusts. Narrate it.

## What to notice

- Each phase only loaded the files it needed. Research read `sample.md`. Plan read the research notes. Implementation read the plan. No phase saw everything — that's how context stays lean.
- Three different models ran across three phases. Total cost is almost always lower than running the strongest model for the whole thing.
- Watch `pytest` and `ruff` close the loop during the implementation phase. When a test fails, the agent adjusts and reruns rather than drifting.
- `research-notes.md` is a context packet. `plan.md` is a handoff contract. The same pattern scales to real features — only the scope of each phase changes.

## Reset for Q&A

```bash
git checkout demos/05-research-plan-implement/
```
