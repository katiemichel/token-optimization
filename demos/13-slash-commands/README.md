# Demo 5 — Context-control slash commands

**Time:** ~4-5 minutes
**Recommended model:** Any. These commands are model-agnostic context tools.
**No code changes required.** Runs entirely in Copilot Chat.

## Why this demo exists

Session 1's Demo 08 *used* `/compact`, `/fork`, and `/chronicle` in passing. This demo **teaches them deliberately** as the live steering wheel for context and cost. They frequently save more credits than swapping models — because they act directly on the thing you pay for every turn: the context window.

| Command | What it does | Reach for it when… |
| --- | --- | --- |
| `/compact` | Summarizes older turns to reclaim context-window space | Same task, history has grown noisy, you want to continue |
| `/fork` | Branches the conversation, inheriting history | You want to explore a side path without polluting the main thread |
| `/chronicle` | Generates insights from your real session history | You want to know what's actually wasting credits |

> Decision rule: **same task + noisy history → `/compact`** · **side exploration → `/fork`** · **new task → new chat** · **what's wasting credits → `/chronicle`**.

## Step 1 — `/compact` to reclaim context (90 sec)

**Setup — build a long session first.** In a fresh chat, paste these turns in sequence, waiting for a response each time:

> Turn 1: I'm building a Python CLI that checks markdown links. What standard-library modules are relevant?

> Turn 2: Use `re` and `pathlib`. Write a function that extracts all local file links from a markdown string.

> Turn 3: Extend it to check whether each linked file actually exists.

> Turn 4: Add a `--verbose` flag. Actually — make the output format configurable too, JSON or plain.

Now the session is carrying four turns of history into every new request. Compact it:

> /compact focus on the function's current behavior, its arguments, and what's still unresolved

**[Point out:]**
- The older turns collapse into a short summary — fewer input tokens on every subsequent turn.
- The focus string controls what survives. Without it, `/compact` summarizes everything; with it, you keep what matters.
- `/compact` is a **cache boundary** — if you're on Auto, this is a safe point for it to re-route the model.

## Step 2 — `/fork` for a side exploration (90 sec)

Continue from the compacted session. You want to try an alternative output design without losing your main thread.

> /fork

In the forked chat, ask the side question:

> In this fork only: sketch an alternative where output is a single JSON object streamed to stdout. Don't change the main design — I'm just exploring.

**[Point out:]**
- The fork **inherited the full history** — you didn't re-explain anything.
- Your original thread is untouched and stays focused.
- You can also hover any previous message and choose **Fork Conversation** to branch from that exact checkpoint.

**[Say:]** "Fork is for 'what if?'. New chat is for 'different task'. Don't use a new chat for exploration — you'd lose the context. Don't use a fork for a genuinely new task — you'd drag stale context in."

## Step 3 — `/chronicle` to learn from your history (60 sec)

In any chat where you've done real work today:

> /chronicle:cost-tips

Then:

> /chronicle:tips

**[Point out:]**
- `:cost-tips` is tactical — personalized token/credit reduction advice from your actual sessions.
- `:tips` is strategic — broader workflow efficiency patterns.
- These analyze **your real session history**, not generic best practices.

**[Tie to Demo 4:]** When `/chronicle` surfaces a recurring miss (e.g. "you switch models mid-session in 30% of sessions"), encode it into `AGENTS.md` or `.github/copilot-instructions.md`. One observation → standing rule forever. That's the feedback loop closing.

## What to notice

- All three commands act on the context window — the thing you pay for on every turn.
- `/compact` and `/fork` are about **shape** (what history is carried). `/chronicle` is about **learning** (what to change next time).
- None of them require changing models, yet together they often beat model-swapping on credit savings.

## Reset

> Click **New chat**. Discard the long session and the fork created during this demo.
