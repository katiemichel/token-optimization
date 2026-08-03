# Demo 2 — Reasoning effort & custom subagents on cheaper models

**Time:** ~5 minutes
**Recommended models:**
- Main session: **Claude Sonnet 4.6** or **GPT-5.5** (something that supports configurable reasoning effort).
- Subagent: **Claude Haiku 4.5** or **Gemini 3.5 Flash** (a lightweight model).

## Why this demo exists

Two related ideas, both new in Session 2:

1. **Reasoning effort is a dial.** Higher effort = more thinking tokens = more credits. Use the regular level unless the task actually needs more.
2. **Subagents shouldn't run on the main session's expensive model.** A custom agent with a pinned cheap model + a small `tools` list is the right pattern for routine sub-work (code review, lint cleanup, doc generation, test scaffolding).

Crucially, **invoking a subagent does not invalidate the main session's cache** the way a mid-session model swap would. Subagents are the cache-safe way to "switch models" for a piece of work.

## Step 1 — Reasoning effort, the cheap way (90 sec)

Open a fresh chat on a model that supports configurable reasoning effort.

**Default-effort prompt:**

> List the three highest-risk edge cases in `linkcheck.py` for malformed reference-style links. Be brief.

Note the per-turn cost (hover the response).

Now open the model picker, raise the reasoning effort to **high**, **start a new chat** (so the cache change doesn't penalize this turn), and paste the **same** prompt.

Compare:

- Output length and "show your work" depth.
- Per-turn credit cost.

> Talking point: "The high-effort answer wasn't more *correct* — it was more *elaborate*. The default was already right. Raising effort is for problems where you can articulate, in advance, why deeper reasoning will pay off."

**Why a new chat:** Changing reasoning effort mid-session invalidates the cache (Demo 1, Step 5). Treat reasoning effort as a session-start decision.

## Step 2 — Look at the included custom agent (60 sec)

Open [`code-reviewer.agent.md`](code-reviewer.agent.md) in the editor.

Walk the room through the three things that make it cost-efficient:

- **`model:`** pinned to a lightweight tier. The reviewer never escalates.
- **`tools:`** a tight allowlist (read-only file tools + grep). No edits, no terminal, no MCP toolsets.
- **Prompt scope** is narrow and ends with a stop condition ("return findings, do not propose patches").

> Talking point: "A subagent doesn't need the same capability surface as the main agent. Every tool you leave on costs tokens on every turn it runs."

## Step 3 — Invoke the subagent (90 sec)

Back in the main chat (still on your reasoning-tier model), paste:

> Use the `code-reviewer` subagent to review #file:demos/03-reasoning/inventory.py and list the top three concerns. Do not write patches yet.

Then, when it returns:

> Now, on this main model, propose fixes for the top concern only.

What to point out:

- The subagent returned findings without burning reasoning-tier tokens.
- The main agent used its expensive capacity only for the actual fix work.
- Open Cache Explorer (from Demo 1) — the main session's cache hit rate **did not collapse** when the subagent ran. Subagents are cache-safe.

## Step 4 — When to skip a custom agent (30 sec)

State out loud — this is as important as the positive examples:

- One-off review of one file: just use the main model directly. The setup cost isn't worth it.
- The subagent needs the full repository context: it won't have it (each subagent runs in its own session). Use a main-agent turn.
- The task is "fix this" — subagents are best at **producing findings or artifacts**, not unbounded edit loops.

## What to notice

- Reasoning effort is a per-session decision, not a per-turn one.
- Subagents with pinned cheap models are the cleanest way to do sub-work without paying main-model rates.
- A `tools:` allowlist on a custom agent is **input-token savings on every invocation**, not just a safety feature.

## Reset before the next demo

> Click **New chat**. Demo 3 starts clean.
