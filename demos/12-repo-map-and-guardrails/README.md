# Demo 4 — `AGENTS.md` repo map + guardrail-driven feedback loop

**Time:** ~5 minutes
**Recommended model:** Any.
**No code changes required**, but you will create a file (`AGENTS.md`) and run existing tests / lint.

## Why this demo exists

Two ideas that compound:

1. **A repo map (`AGENTS.md` or `.github/copilot-instructions.md`) saves input tokens forever.** Without one, the agent reads ten files just to orient itself before every non-trivial task.
2. **Deterministic guardrails (tests, lint, security scans) save tokens by stopping wrong work fast.** One failing test costs less than five corrective agent turns.

The loop ties together: `/chronicle` shows you what's wasting tokens → encode the fix in instructions → guardrails enforce it → the next session is leaner.

## Step 1 — Show what's missing (45 sec)

Open a fresh chat. Paste:

> Where in this repo would I add a new demo that compares two ways of using slash commands? Don't make changes — just tell me which existing files set the conventions I'd need to follow.

Watch what happens:

- The agent reads multiple READMEs, the top-level `README.md`, possibly `pyproject.toml`, and `.github/copilot-instructions.md`.
- Each of those reads is **input tokens**.

> Talking point: "Every one of those reads is the agent orienting itself. With a proper repo map, most of that disappears."

## Step 2 — Look at the example `AGENTS.md` (60 sec)

Open [`example-AGENTS.md`](example-AGENTS.md) in the editor.

Point out what makes a good repo map (and what doesn't):

**Good:**

- Top-level layout in 5–10 lines.
- Conventions: language version, lint tool, test command, function-vs-class style.
- Known pitfalls the agent tends to repeat (cross-demo imports, etc.).
- Stop conditions and validation commands.

**Avoid:**

- Generic "be helpful" prose.
- AI-generated checklists that aren't grounded in observed misses.
- Personal preferences ("I like spaces over tabs"). Those belong in personal instructions, not repo-level.

> Talking point: "This file is **input tokens on every turn**. Every sentence you cut here is credits saved at scale. Aim for under 50 lines."

## Step 3 — Add it (or simulate adding it) (45 sec)

Copy `example-AGENTS.md` to the repo root as `AGENTS.md`:

```bash
cp demos/12-repo-map-and-guardrails/example-AGENTS.md AGENTS.md
```

In a **new chat**, re-paste the Step 1 prompt.

What changed:

- The agent answers with fewer reads (or none beyond the map itself).
- The response is more anchored to actual conventions.

## Step 4 — Guardrails as a token-saving tactic (90 sec)

Frame this as **counter-intuitive**: investing in pre-existing checks **lowers** total token use.

Live demo — pick one demo folder with passing tests (e.g. `demos/02-execution/`):

```bash
pytest demos/02-execution -q
ruff check demos/02-execution
```

Both green. Now in chat, ask:

> Add a new helper `apply_discount(cart, code)` to #file:demos/02-execution/cart.py. After making the change, run `pytest demos/02-execution -q` and `ruff check demos/02-execution`. Stop as soon as both are green.

What to watch for:

- The agent makes a change.
- Runs tests.
- If they fail, it adjusts on a tight feedback loop — usually 1–2 corrections.
- Stops at green.

Then state the counter-factual: **without** the test + lint requirement, agents tend to add the helper plus refactor adjacent code, plus add helpers nobody asked for. The deterministic checks are the cheapest "stop talking" signal you can give an agent.

> Talking point: "Teams with strong test + lint coverage see fewer agent retries, faster completion, and lower total token spend — even if each individual turn costs slightly more upfront because of the tool calls."

## Step 5 — Close the loop with `/chronicle` (30 sec)

In a chat where you've done real work today, paste:

> /chronicle:cost-tips

When a suggestion is concrete and recurring (e.g. *"you switch models mid-session in 30% of sessions"*), **encode it directly** into your `.github/copilot-instructions.md` or `AGENTS.md`.

> Example addition to `copilot-instructions.md`:
>
> ```
> - Do not switch models mid-session. If a different capability is needed, start a new chat or invoke a subagent.
> ```

> Talking point: "This is the highest-leverage habit in the session. One observation, encoded once, applies to every future run on this repo — yours, your teammates', and any cloud agents."

## What to notice

- A short, grounded repo map cuts orientation reads from many turns to zero.
- Tests and lint aren't just quality controls — they're **the cheapest way to terminate wrong agent work early**.
- `/chronicle` insights are only useful if you write them down somewhere the agent reads on every run.

## Reset

Discard the temporary `AGENTS.md` if you don't want to commit it:

```bash
git restore AGENTS.md 2>/dev/null || rm AGENTS.md
```

…or keep it. It is, after all, a real improvement.
