# Optimization checklist — Session 2 take-home

*Pin this next to your model picker. One page. Habits, not theory.*

---

## Before you start a session

- [ ] **Pick model + reasoning effort + tools once.** Don't change them mid-session — every change invalidates the prompt cache.
- [ ] Default to **Auto** unless you have a specific reason to pin a model. Auto switches only at cache boundaries and gets a 10% discount on paid plans.
- [ ] Open **Configure Tools** in the chat input. Disable tools and MCP toolsets you don't need for this task.
- [ ] If your model supports configurable reasoning effort, **leave it on the default**. Raise only for genuine architecture / multi-step-debug work.

## While you work

- [ ] **New task = new chat.** Old history is input tokens on every turn.
- [ ] If a session has grown noisy but you want to continue, run **`/compact`** with a focus string (e.g. `/compact focus on decisions and open TODOs`).
- [ ] Hover any response to see its **per-turn cost**. Look for outliers.
- [ ] Click the **context window control** in the chat input to see cumulative session cost.
- [ ] Use **`/fork`** for side explorations instead of polluting the main thread.
- [ ] Need a different capability for a sub-task? Use a **custom agent** with a pinned cheaper model — don't switch the main session's model.

## Cache discipline (the biggest single lever)

Cache hits are billed at ~10% of fresh input tokens. **These invalidate it:**

- Switching models mid-session
- Changing reasoning effort mid-session
- Toggling tools or MCP servers mid-session
- Returning to an old session (1 hr for most providers, 24 hr for OpenAI)

If you need one of those changes, **start a new chat or `/compact` first.**

Check your cache hit rate in **Agent Debug Logs → Cache Explorer**. Below 40% is a smell.

## Workspace setup (set once, save forever)

- [ ] Repo has an `AGENTS.md` (or `.github/copilot-instructions.md`) — short, grounded, human-written. **Under 50 lines.**
- [ ] `.gitignore` covers all build outputs.
- [ ] `files.exclude` hides large generated paths (`node_modules`, `dist`, `.venv`, etc.).
- [ ] `search.exclude` covers lockfiles, snapshots, minified output, large fixtures. **Search snippets count toward context even when the file is never opened.**
- [ ] MCP servers enable only the toolsets the team actually uses.

## Custom agents and subagents

Use a custom agent when:

- The same workflow repeats 3+ times per week.
- The inputs and success criteria are stable.
- A cheaper model + restricted tool list would do the work.

Each custom agent should declare:

- A pinned `model:` (prefer lightweight tier for routine sub-work).
- A `tools:` allowlist — read-only when possible.
- A narrow scope with an explicit stop condition.

Skip custom agents for genuinely one-off work.

## Guardrails (counter-intuitive cost reduction)

- Unit tests catch wrong direction in 1 turn instead of 5.
- Lint catches style thrash before it becomes a retry loop.
- Security scans catch risky patterns before unwinding is expensive.

End agent prompts with the validation command and a stop condition:

> When done, run `pytest -q` and `ruff check .`. Stop as soon as both are green.

## Feedback loop

- Run **`/chronicle:cost-tips`** and **`/chronicle:tips`** weekly.
- When a recurring miss appears, encode the fix in `AGENTS.md` or `copilot-instructions.md` directly. One-time observation → standing rule for every future run.
- Keep instruction files **short**. They are input tokens on every turn — bloat there is recurring cost.

## Smells that mean something is wrong

| Smell | Likely cause | First fix |
| --- | --- | --- |
| Per-turn cost climbing across a session | Cache being invalidated repeatedly | Stop changing model / tools / effort mid-session |
| Agent reads many files before answering anything | No repo map | Write a short `AGENTS.md` |
| Agent keeps "improving" code you didn't ask about | No stop condition | Add validation commands + "stop when green" |
| Big credit hit when you barely typed anything | Noisy MCP toolset or huge tool surface | Disable unused tools in Configure Tools |
| Search responses include irrelevant files | Index includes generated content | Update `search.exclude` and `.gitignore` |
| Returning to yesterday's chat feels expensive | Cache expired | Start a new chat or `/compact` first |

---

> Rule of thumb: **the model picker is one decision per session; everything else on this page is once-per-repo or once-per-day.** That's why this is where most credit savings live.
