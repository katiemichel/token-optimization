# Model cheatsheet
*Task → tier → model. One page. Hand this out or pin it next to the model picker.*

> **Default in VS Code: Auto.** Auto with task optimization (GA in VS Code) routes by intent and real-time system health, along cache boundaries. Override Auto only when you have a reason — the rest of this page is that reason.

---

## The three tiers

| Tier | What it's good at | What it's bad at | Pick when… |
| --- | --- | --- | --- |
| **Lightweight** | Speed, mechanical edits, small explanations, lookups | Multi-file reasoning, architectural calls | The change is local and the answer is "do this thing." |
| **General-purpose** | Implementing from a clear spec, agentic execution, edit-test loops | Open-ended "figure it out for me" | You have a plan and need it executed cleanly. |
| **Reasoning** | Architecture, subtle bugs, cross-file analysis, trade-off calls | One-line fixes, doc tweaks — over-thinks them | You're stuck, or you're choosing between two valid paths. |

---

## Task → tier → model

| Task | Tier | Try first |
| --- | --- | --- |
| Refactor a single function | Lightweight | **Claude Haiku 4.5**, **Gemini 3.5 Flash** |
| Rename across one file | Lightweight | **Claude Haiku 4.5** |
| Add docstrings / comments | Lightweight | **Claude Haiku 4.5**, **Gemini 3.5 Flash** |
| "What does this regex do?" | Lightweight | **Claude Haiku 4.5** |
| Implement a feature from a written spec | General-purpose | **GPT-5.3-Codex**, **GPT-5 mini**, **Claude Sonnet 4.6** |
| Add tests for an existing function | General-purpose | **GPT-5 mini**, **Claude Sonnet 4.5/4.6** |
| Wire a new endpoint into an existing route | General-purpose | **GPT-5.3-Codex** |
| Codebase exploration & grep-style work | General-purpose | **GPT-5.3-Codex** |
| Debug a subtle bug spanning multiple files | Reasoning | **Claude Opus 4.7/4.8**, **GPT-5.5** |
| Pick between two architectures | Reasoning | **Claude Opus 4.7**, **GPT-5.5** |
| Read a complex stack trace + logs | Reasoning | **GPT-5.5**, **Claude Sonnet 4.6** |
| Design a new system boundary | Reasoning | **Claude Opus 4.7**, **GPT-5.5** |

> Check the [official comparison](https://docs.github.com/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task) for more details.

---

## When to *override* Auto

| Situation | Override to | Why |
| --- | --- | --- |
| You're naming a system boundary or picking an architecture | Reasoning | You want depth, not turn time. |
| You're doing 30 nearly-identical edits | Lightweight | Auto may route safely; lightweight is cheaper and just as good here. |
| You need the exact same model across an entire long session for reproducibility | Pin a model | Auto can switch at cache boundaries. |
| You're benchmarking or A/B'ing model quality | Pin specific models | Auto is non-deterministic by design. |

## When to *trust* Auto

- Mixed-task sessions (one prompt is a refactor, the next is debugging).
- You're in flow and don't want to think about model choice.
- You want the **10% discount** on paid plans.
- You want routing to respond to real-time system health.

## Complex-task add-on (Copilot Coding / Cloud agent)

- Build a short context packet first (scope, files, stop condition, validation).
- Keep custom instructions task-scoped and under ~10 bullets.
- Split research, planning, and execution into separate runs when context gets large.
- Use custom agents only for repeated workflows with stable success criteria.

---

## Anti-patterns

- **"I'll just use the strongest model for everything."** It costs more *and* often produces worse execution diffs. Reasoning models over-engineer.
- **"I'll keep one chat open all day."** Context bloats. Old facts bias new turns. Start fresh between unrelated tasks.
- **"I'll write a long, generic `copilot-instructions.md`."** It bloats every prompt. Keep it short, specific, and grounded in observed behavior.
- **"I'll skip the linter — the agent's code is fine."** Without guardrails, small errors compound. A `ruff check` is cheaper than another agent turn.
