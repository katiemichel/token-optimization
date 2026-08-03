# Demo 07 — Managing Context in Local IDE

**Time:** ~10 minutes
**Recommended model:** Any — the lesson is model-agnostic
**No code required.** This demo runs entirely in Copilot Chat.

**Follow-along format:** Paste each prompt exactly, in order, in a fresh chat where instructed.

> Use this demo in place of Demo 06 if participants don't have Copilot Coding or Cloud agent access.

## The setup

Token cost isn't just about prompt length. Every turn injects the full session history — stale decisions, topic changes, and prior task artifacts inflate every subsequent turn silently. This demo walks through four concrete patterns and what to do when you notice each one.

Reference card: [`context-signals.md`](context-signals.md)

## Step 1 — Start a new chat

Continue the Demo 03 debug chat and ask for docs in the same session. Then open a fresh chat and ask for the same docs.

## What to notice

- The fresh-chat response is shorter and doesn't reference the prior debug session.
- Old context was injecting itself into an unrelated task.
- **Rule:** new task or new model = new chat.

## Step 2 — Compact and continue

**Setup — build a noisy session first.** Open a new Copilot Chat and paste these four turns in sequence, waiting for a response each time:

> Turn 1: I'm working on a Python CLI that checks markdown links. What libraries are available for parsing markdown in the standard library?

> Turn 2: OK, let's use re and pathlib. Write a function that extracts all local file links from a markdown string.

> Turn 3: That works but I also want to check if the files actually exist. Can you extend it?

> Turn 4: Now I want to add a --verbose flag. Actually, wait — can we make the output format configurable? Like JSON or plain text?

Now paste Turn 5:

> Summarize what we've built so far in bullet form: what the function does, what arguments it takes, and what's still unresolved. Keep it under 10 lines.
>
> After the summary, continue with: add a `--format` flag that accepts `json` or `plain` (default: `plain`). Do not repeat context from the summary.

## What to notice

- Four turns collapsed to ~10 lines; every subsequent turn is cheaper.
- The continuation builds on the summary without re-expanding the history.
- "Do not repeat context from the summary" is doing real work — try removing it and compare.

## Step 3 — Optimize always-on custom instructions

This step focuses on real token reduction, not just output style changes.

Open [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md). Explain that this file is injected every turn, so shorter and tighter instructions reduce repeated input tokens.

### Live update (2-3 minutes)

Do a quick, human-written refinement in the file:

- Keep only rules that are always true for this repo.
- Remove generic advice and duplicated wording.
- Base edits on real misses you have seen in this workshop.
- Target a small file (roughly 8-15 bullets total).

If your setup supports scoped instruction files, move task-specific guidance out of the always-on file and into a directory-scoped instruction file for that demo folder.

Example shape (adjust paths to your repo):

```md
---
applyTo: "demos/05-research-plan-implement/**"
---

- For this demo, preserve failing-first tests.
- Keep output to diffs unless a file is new.
- Avoid cross-demo imports.
```

Now run a three-chat comparison.

**Chat A — baseline behavior (current repo instructions).** Open a fresh chat and paste:

> Write a Python function called `load_env` that reads a `.env` file from a given path and returns key-value pairs as a dict. Skip blank lines and lines starting with `#`.

**Chat B — simulate bloated always-on instructions.** Open another fresh chat and paste:

> Treat this as an always-on instruction block for this session:
> - Use extensive explanatory prose before code.
> - Include implementation alternatives and tradeoff analysis.
> - Add a full test strategy section even for tiny snippets.
> - Repeat assumptions and constraints before and after the solution.
> - Provide a complete file rewrite, not a focused snippet.
>
> Task: write `load_env` exactly as in Chat A.

**Chat C — simulate optimized always-on instructions.** Open another fresh chat and paste:

> Treat this as an always-on instruction block for this session:
> - Be concise.
> - For small tasks, return only the needed code.
> - Avoid repeated explanation unless asked.
>
> Task: write `load_env` exactly as in Chat A.

## What to notice

- Chat B demonstrates instruction bloat: longer prompts produce longer responses and usually more follow-up churn.
- Chat C shows optimized instruction shape: less repeated prose and tighter outputs.
- This is the key distinction: local overrides change behavior; shorter always-on instructions reduce recurring input tokens.
- A small, human-written instruction file beats a long AI-generated checklist.
- Directory-scoped instructions improve optimization further by applying heavy guidance only where it is needed.

## Step 4 — Re-anchor on a fresh chat

Close the Demo 05 Research phase chat. Open a new chat, switch to Claude Opus 4.7, and paste:

> Context re-anchor. We are building a CLI markdown link checker.
>
> State so far:
> - Research complete and summarized in research-notes.md
> - In scope: inline links, reference links, image links, autolinks
> - Out of scope: external URL checking, anchor links
>
> Current task: write the implementation plan. Read #file:demos/05-research-plan-implement/research-notes.md and #file:demos/05-research-plan-implement/test_linkcheck.py only.
>
> Start from here without re-explaining.

## What to notice

- The new chat starts oriented without any reconstruction conversation.
- The model doesn't ask "what have we discussed?" — the re-anchor tells it.
- This is also how you switch models mid-workflow: write the re-anchor, switch, paste.

## Reset before the next demo

Click **New chat** in Copilot Chat. Discard any sessions opened during Step 2 setup.
