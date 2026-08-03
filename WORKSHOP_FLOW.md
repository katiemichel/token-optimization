# Agent Quality & Token Optimization

## Customer-facing workshop flow

This README documents the presentation flow as it is currently written in the
workshop deck. It includes only the slides that are intended to be presented.
The slide numbers below refer to the original PowerPoint deck, so the numbering
is intentionally non-contiguous.

## Flow at a glance

1. Introduce the relationship between agent quality, value, ROI, and token cost.
2. Explain how agents operate across multi-step loops, context windows, and
   model choices.
3. Present practical quality and token controls.
4. Show how persistent instructions, custom agents, skills, MCPs, subagents, and
   other agent configurations shape the harness.
5. Close with a concise set of actions participants can start using today.

## Detailed presentation flow

### 1. Opening and framing

**Slide 1 — Agent Quality & Token Optimization**

- Introduce the workshop and its focus on agent quality and token
  optimization.
- Position the session as a customer-facing GitHub workshop.

**Slide 2 — Overview**

Preview the three sections:

1. High-level overview
2. Quality and token controls, followed by practical optimization tips
3. Live demo

**Slide 3 — Agent gambling is no longer sustainable**

- When tokens are cheap, agent accuracy can appear less important.
- As token costs matter more, improving agent accuracy becomes engineering
  work rather than something to leave to chance.

**Slide 6 — Instead of counting tokens, make every token count**

Transition from cost awareness to deliberate use of context, prompts, tools,
and model capacity.

### 2. Agents, models, and context

**Slide 10 — Multi-step loops: Working with an Agent**

Explain the basic agent system:

- The user and project provide prompts, files, instructions, skills, and MCPs.
- The harness coordinates the interaction.
- The agent uses an LLM to reason and produce work.
- The same pattern applies across surfaces such as VS Code Chat, Copilot CLI,
  Copilot cloud agent, Claude Code, and OpenAI Codex.
- The system is not magic; it is text passed through a stateless loop.

**Slide 11 — Agents working with LLMs**

Introduce the context-window model:

- Each loop includes system instructions and tools, the prompt, files, and the
  model response.
- Input and output tokens accumulate across loops.
- Cached input tokens may help, but are not guaranteed.
- Every model has a specific context limit.

### 3. Quality and token controls

**Slide 13 — Quality & Token Controls**

Section divider introducing the main control techniques.

**Slide 14 — AI-assisted engineer vs. AI engineer**

Contrast:

- An AI-assisted engineer, who primarily works synchronously with one agent.
- An AI engineer, who orchestrates multiple agents asynchronously.

Use this distinction to show how workflow design affects the impact of
optimization choices.

**Slide 15 — The two biggest levers for optimizing quality & tokens**

Cover the two primary levers:

- **Model choice and Auto Mode**
  - Use reasoning models such as Opus or GPT-5.5 for synchronous work such as
    planning, architecture, and debugging.
  - Use mid-tier models such as Sonnet or GPT-5.4 for asynchronous
    implementation.
  - Use lower-tier models such as Haiku or GPT-mini for small refactors,
    repetitive work, and documentation updates.
  - Use Auto Mode as the default when the task does not justify a deliberate
    model selection.
- **Context engineering**
  - Provide as much context as required, but as little as necessary.
  - Treat context engineering as a source of guidance and team upskilling.
  - Compact sessions cautiously because valuable information can be lost.
  - Use `/clear` for a new task and provide only relevant context.

**Slide 16 — Guiding the agent**

Improve prompts by:

- Being precise.
- Adding descriptions.
- Defining stop signals, such as “Stop if X.”
- Providing known context up front, including relevant files, folders, and
  websites.

### 4. Workflow and harness configuration

**Slide 17 — Divide and conquer your work**

Recommend separating complex work into:

> Research → Plan → Implement

Use the appropriate model or agent for each stage. Start by asking which files
are relevant, create a precise specification, and then implement against that
specification.

**Slide 18 — Avoid compounding errors early**

Show how deterministic controls, especially unit tests, prevent repeated
mistakes:

- Without tests, a buggy change can lead to repeated buggy changes and
  debugging sessions.
- With tests, failing tests provide a correction signal and succeeding tests
  provide a deterministic stop condition.
- Earlier feedback reduces wasted CI/CD minutes, Copilot review cycles, and
  human time.

**Slide 19 — Persistent instructions**

Introduce the configuration surfaces that can provide durable guidance:

- `copilot-instructions.md`
- Custom agents in `.github/agents/*.agent.md`
- Skills in `.github/skills/*/SKILL.md`
- MCPs
- Subagents
- Scoped instructions in `.github/instructions/*.instructions.md`
- Prompt files in `.github/prompts/*.prompt.md`
- Copilot Memory
- Agent configs

**Slide 20 — Your always-on agent guidance**

Focus on persistent instructions:

- Put project non-negotiables and recurring agent misses in
  `.github/copilot-instructions.md` or `AGENTS.md`.
- Include concise directions such as “be concise” when useful.
- Keep the file small and human-written rather than AI-generated.
- Iterate, maintain, and recreate it as the project changes.

**Slide 21 — Design workflows & behaviors with custom agents**

Explain the custom-agent flow:

- The harness retrieves the custom-agent definition.
- The harness adds the definition to the available system instructions and
  adjusts the available tools.
- The user invokes the workflow with a prompt such as
  `/TDD-RED ADD API ENDPOINT`.
- The custom agent supplies the repeatable behavior.

**Slide 22 — Add conditional capabilities with skills**

Explain the skill flow:

- Skill descriptions are available to the harness.
- When a task matches a skill, the harness loads the full skill document into
  context.
- The user can request work such as “WORK ON API,” and the harness can select
  the relevant API skill.

**Slide 23 — Integrate with third-party tooling using MCPs**

Explain the MCP flow:

- The harness exposes tool descriptions, such as a tool that can retrieve an
  issue.
- The user asks to read a specific issue, such as “READ ISSUE #45.”
- The LLM selects the MCP tool.
- The harness calls the MCP API and returns the issue to the agent.

**Slide 24 — Offload task-specific context with subagents**

Explain how subagents reduce the amount of task-specific context held by the
main session:

- The main session delegates a focused request.
- The subagent receives its own instructions, prompt, and documents.
- The subagent returns a summary.
- The harness places that summary back into the main context.

Example use case: “FIND MY FEATURE.”

**Slide 25 — Other agent configurations**

Cover the remaining configuration options:

- **Scoped instructions:** conditional instructions based on file-path
  patterns; they are offered to the agent similarly to skills and are not
  deterministic.
- **Prompt files:** manually invoked prompts that can trim the toolset or
  invoke custom agents and skills; use them as a manual starting point.
- **Copilot Memory:** small, automated, always-on instructions shared across
  Copilot surfaces; review them regularly.

### 5. Close

**Slide 28 — Summary: five things you can start doing today**

Close with five practical actions:

1. Choose the right model for the right task.
2. Provide clear guidance in prompts.
3. Use a Research → Plan → Implement workflow.
4. Add deterministic guardrails such as tests, linters, and security scans.
5. Maintain a concise, human-written `copilot-instructions.md` file and use it
   as an agent-miss log and a way to trim output.

**Slide 29 — Thank you**

End the workshop with the closing Copilot/AI thank-you slide.

## Hidden slides intentionally excluded

The following slides are marked hidden in the PowerPoint and are not part of
this presentation flow:

- Slide 4 — Quality impacts value impacts ROI
- Slide 5 — The Compound Error Problem
- Slide 7 — LLM, Agent & Context Windows
- Slide 8 — How to think about it: LLMs and word probability
- Slide 9 — Provide as little context as possible, but as much as required
- Slide 12 — Lost in the Middle
- Slide 26 — Actions roadmap
- Slide 27 — Long term guidance

These slides remain in the source deck but should not be referenced as
presented content unless the deck's visibility settings change.
