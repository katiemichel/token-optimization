# Context signals — one-page reference

Use this during the workshop or keep it open during day-to-day Copilot Chat sessions.

| Signal | What you notice | Wrong response | Right response | Token impact |
|---|---|---|---|---|
| **Topic shift** | You're starting a genuinely new task | Keep chatting in the same session | Start a new chat | Eliminates prior history from every subsequent turn; avoids injecting hundreds of irrelevant lines |
| **Context drift** | Model hedges, re-asks answered questions, or repeats old decisions | Add another clarifying turn | Compact: summarize what's done, then continue | Collapses N turns into ~10 lines; all future turns are cheaper |
| **Stale instructions** | Repo instructions contradict your current task or are too broad | Use only local overrides and assume token cost is fixed | For one-off behavior, use explicit local overrides. For token savings, keep always-on instructions short and human-written, and move task-specific rules to directory-scoped instruction files | Reduces correction churn and lowers recurring input tokens from always-on context |
| **Cold re-entry** | You or a teammate returns after a break with no shared context | Reconstruct context through conversation | Write and paste a re-anchor prompt before anything else | Avoids a multi-turn reconstruction round (typically 2–4 wasted turns) |
| **Model swap** | You need to change models mid-workflow | Start from scratch | Write a re-anchor, switch model, paste it in | Re-anchor costs ~1 turn; reconstruction costs 3–5+ |
| **Scope creep in-flight** | Task grew beyond original intent mid-session | Let it grow | Compact current state, restate scope, continue | Keeps the model's working window tight; prevents drift-driven over-generation |

---

## Compact prompt template

Paste this when the session has become noisy:

```
Summarize what we've built so far:
- What it does
- Key decisions already made
- What's still unresolved

Keep it under 10 lines. After the summary, continue with: [next task].
Do not repeat context from the summary.
```

---

## Re-anchor prompt template

Paste this at the top of a new chat when returning to a task or switching models:

```
Context re-anchor. We are working on [one-sentence description].

State so far:
- [Decision already made]
- [What's passing / failing]

Current task: [exactly what we're doing next]

In scope: [files or areas]
Out of scope: [explicit non-goals]

Start from here without re-explaining.
```

---

## Rule of thumb

> If you'd preface your next prompt with "as I mentioned earlier…" — compact or re-anchor instead.

> If you'd preface your next prompt with "actually, let's switch to…" — start a new chat.
