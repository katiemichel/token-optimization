# The Right Model for the Job
*Model Selection & Token Efficiency with GitHub Copilot — workshop demo repo*

This repository accompanies a ~60-minute workshop: ~5–10 minutes of slides, 40–50 minutes of live demo, and ~10 minutes of Q&A. The demos are intentionally small, runnable, and structured so each one isolates a single decision: **which model fits this work?**

Link to relevant GitHub blog post: [Improving token efficiency in GitHub Agentic Workflows](https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/) 

## Workshop outcomes

By the end of the session participants can:
- Match a task to one of three model tiers (reasoning, general-purpose, lightweight) on purpose, not by habit.
- Identify when **Auto** (with task-optimized, intent-based routing in VS Code) is the right default and when to override it.
- Apply five token-efficiency practices from the source doc to their own workflow.
- Recognize the cost of "default to the most powerful model" in execution-heavy work.
- Handle moderately complex scenarios by shaping context deliberately (what to include, what to exclude, and when to reset).
- Write short, optimized custom instructions and understand when custom agents are worth the setup cost.
- Run a final handoff-style workflow that maps cleanly to Copilot Coding and Cloud agent usage.

## What's in here

| Path | Purpose |
| --- | --- |
| [docs/model-cheatsheet.md](docs/model-cheatsheet.md) | One-page reference: task → recommended tier → model |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Example of the concise, repo-scoped instructions advocated in §5 |
| [demos/00-token-efficiency/](demos/00-token-efficiency/) | Supplemental: token cost awareness, math, and five efficiency practices (use during intro slides) |
| [demos/01-lightweight/](demos/01-lightweight/) | Refactor & document a messy module — lightweight tier shines |
| [demos/02-execution/](demos/02-execution/) | Implement from a clear spec — general-purpose / Codex tier sweet spot |
| [demos/03-reasoning/](demos/03-reasoning/) | Diagnose a subtle bug across files — reasoning tier earns its cost |
| [demos/04-auto-vs-manual/](demos/04-auto-vs-manual/) | Run the same three tasks through Auto and compare to manual picks |
| [demos/05-research-plan-implement/](demos/05-research-plan-implement/) | Full R→P→I walkthrough on a small CLI (markdown link checker) |
| [demos/06-copilot-coding-cloud/](demos/06-copilot-coding-cloud/) | Complex-scenario finale: context packet + optimized instructions + custom agent handoff (Copilot Coding / Cloud agent) |
| [demos/07-context-management/](demos/07-context-management/) | Managing context in local IDE: when to reset, compact, re-anchor, and override instructions |
| [demos/08-usage-optimization-commands/](demos/08-usage-optimization-commands/) | Slash command mini-demo: `/chronicle:cost-tips`, `/chronicle:tips`, `/compact`, and `/fork` |
| [demos/09-monitor-and-cache/](demos/09-monitor-and-cache/) | Operations demo: monitor real usage, preserve cache, avoid invalidators |
| [demos/10-reasoning-and-subagents/](demos/10-reasoning-and-subagents/) | Operations demo: reasoning effort defaults vs high; subagents on cheaper models |
| [demos/11-tools-and-exclusions/](demos/11-tools-and-exclusions/) | Operations demo: keep tool/MCP surface minimal; exclude noisy files from context |
| [demos/12-repo-map-and-guardrails/](demos/12-repo-map-and-guardrails/) | Operations demo: `AGENTS.md`, deterministic guardrails, and `/chronicle` loop |
| [demos/13-slash-commands/](demos/13-slash-commands/) | Operations demo: `/compact`, `/fork`, and `/chronicle` as context controls |
| [docs/operations-optimization-checklist.md](docs/operations-optimization-checklist.md) | One-page operations checklist (cache, tools, instructions, chronicle loop) |

## Setup (one-time, before the workshop)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

Sanity check:
```bash
pytest
ruff check .
```

You'll also want:
- VS Code with the GitHub Copilot and Copilot Chat extensions, signed in to an account that has access to **Auto**, **Claude Haiku 4.5**, **Claude Sonnet 4.6** (or Opus 4.7), and **GPT-5 mini** (or GPT-5.3-Codex).
- The model picker in Copilot Chat handy — you'll be switching often.

## How to Use This Workshop

**Opening (5–8 min):** Reference [demos/00-token-efficiency/](demos/00-token-efficiency/README.md) while presenting slides. The README includes:
- Talking points on cost awareness and token math
- Three concrete "bad vs. good prompt" examples with token breakdowns
- Notes for instructors on showing real token counts live in VS Code

**Hands-on (40–50 min):** Run through demos 01–05. Between demos, pause and point out how tight prompting leads to one-shot success (reinforce Demo 00 lessons).

**Complex finale (8–12 min):** Choose based on your audience:
- **With CCA access:** Run Demo 06. Shows context shaping for Copilot Coding / Cloud agent; the context packet and instruction patterns apply to local Chat too.
- **Without CCA access:** Run Demo 07 instead. Covers the same principles (compact, re-anchor, new-chat signals, instruction scoping) entirely in local Copilot Chat. Same time budget.

If time permits and the audience has CCA access, you can run both — Demo 07 is a fast conceptual primer (~10 min) that makes Demo 06's context packet feel immediately useful.

**Optional add-on (6-8 min):** Run [demos/08-usage-optimization-commands/](demos/08-usage-optimization-commands/README.md) to show how slash commands improve token and credit efficiency without code changes.

**Operations track add-on (20-30 min):** Run demos [09](demos/09-monitor-and-cache/README.md) through [13](demos/13-slash-commands/README.md) as a seamless continuation focused on cache discipline, reasoning effort, tool/instruction minimization, and the `/chronicle` feedback loop.

**Q&A (10 min):** Use the model cheatsheet as a reference for common questions.
