# Demo 1 — Monitor real cost & preserve the cache

**Time:** ~5 minutes
**Recommended model:** Any model you would use for normal work — the lesson is model-agnostic. Best demoed on a model that supports configurable reasoning (e.g. **GPT-5.5** or **Claude Sonnet 4.6**) so Step 4 has something to flip.
**No code changes required.** This demo runs entirely in Copilot Chat + VS Code UI.

## Why this is first

Most participants have never seen the real per-turn cost in VS Code. Once they see it, every other lesson in this session lands harder. Then we show the single most expensive habit — **invalidating the prompt cache** — and how to avoid it.

## What you'll see

1. Cost per turn (hover the response).
2. Cumulative session cost + context window usage (chat input popover).
3. Monthly allowance (Copilot status dashboard in the status bar).
4. Aggregate token usage and **cache hit rates** (Agent Debug Logs → Summary + Cache Explorer).
5. What invalidates the cache, live.

## Step 1 — Show per-turn cost (45 sec)

Open a fresh chat. Paste:

> Summarize the purpose of #file:demos/02-execution/SPEC.md in three bullets. No code.

When the response arrives, **hover over the response message**. Point out the credit consumption for that single turn.

> Talking point: "This is the only number that's visible by default. Most people stop here. We're not going to."

## Step 2 — Show cumulative session cost (45 sec)

In the same chat, click (or hover) the **context window control** in the chat input box.

Point out:

- Cumulative cost in credits for the session so far.
- Cumulative input + output token usage and how much of the context window is occupied.

> Talking point: "Per-turn cost lies to you about long sessions. The session number tells the truth."

## Step 3 — Show monthly allowance (30 sec)

Click the Copilot icon in the VS Code **status bar** to open the status dashboard. Point out:

- Percentage of monthly AI credits used.
- Link out to the GitHub usage page for the full breakdown.

> Talking point: "This is the number you should glance at once a day, not once a month."

## Step 4 — Inspect the cache (90 sec)

Open the **Agent Debug Logs** (Command Palette → "Chat: Open Chat Debug View" or similar).

Show:

- **Summary view** — total tokens consumed, total tool calls, total duration for the session.
- **Cache Explorer view** — prompt cache hit rate, input tokens reused vs. fresh.

Now, in the same chat, **switch models** in the model picker and paste any small follow-up:

> Now list three risks in that spec.

Re-open Cache Explorer. The hit rate just collapsed for that turn — the new model could not reuse the previous model's cache.

> Talking point: "That model switch wasn't free. Every cached token just became a fresh input token. Watch the rate climb back up only as the new model rebuilds its own cache."

## Step 5 — The four cache invalidators (60 sec)

State them out loud, and (optionally) demonstrate one or two more live:

1. **Switching models mid-session** (just demonstrated in Step 4).
2. **Changing reasoning effort mid-session.** If your model supports it, change the effort slider and send another turn — watch the cache reset.
3. **Enabling or disabling tools / MCP servers mid-session.** Open Configure Tools, toggle one, send a turn — cache reset.
4. **Coming back to an old session.** Caches expire (1 hr for most providers, 24 hr for OpenAI). Yesterday's chat is no longer cheap to resume.

> The fix is the same in all four cases: **decide model + reasoning + tools before you start, then leave them alone**. If you need to change one, start a new chat or run `/compact` first.

## What to notice

- The numbers are concrete, not theoretical. Cache hit rates of 80–90%+ are normal in a well-run session; below 40% is a smell.
- Mid-session model switching is the most common preventable cost in the room.
- Auto's value isn't just "picks a good model" — it's "switches **only at cache boundaries**." That alone justifies it for paid plans.

## Reset before the next demo

> Click **New chat** in Copilot Chat. Demo 2 starts clean.
