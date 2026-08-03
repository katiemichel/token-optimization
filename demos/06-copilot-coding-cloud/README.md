# Demo 06 - Copilot Coding / Cloud agent finale

**Time:** ~8-12 minutes
**Recommended model mode:** **Auto** first, then pin a model only if needed for reproducibility
**Goal:** show a realistic, moderately complex workflow where quality depends on context shaping and instruction quality, not just model size.

This demo works in local Copilot Chat, Copilot Coding, or Cloud agent — the context packet and instruction patterns are the same regardless of surface.

> **No CCA access?** Run [Demo 07](../07-context-management/README.md) instead. It covers the same context-shaping principles using only local Copilot Chat.

## Why this demo exists

Demos 01-05 prove model-selection basics. This demo shows the "real world" layer:
- You rarely start with a clean one-file task.
- Context can become noisy fast.
- Reusable instructions and custom agents can reduce retries when the task repeats.

## Complex scenario (safe and bounded)

Use a "cross-demo consistency" request instead of adding new product code:

- Standardize prompt formatting in demo READMEs.
- Preserve workshop intent and order.
- Keep command examples runnable.
- Require a validation pass (`pytest -q`, `ruff check .`) and stop.

This gives multi-file complexity without risky domain changes.

## Step 1 - Build a context packet (2-3 min)

Create a short packet from files that matter right now. Copy `context-packet-template.md` to `context-packet.md` and fill it in.

Good packet rules:
- Max ~30 lines.
- Facts only (no guesses).
- Explicit in-scope and out-of-scope lists.
- Include stop condition and validation commands.

## Step 2 - Add optimized custom instructions (2 min)

Copy `custom-instructions-template.md` to `custom-instructions.md` and edit it for the current task.

Keep it lean:
- 5-10 bullets
- Actionable constraints only
- No generic style rules that are already in repo policy

## Step 3 - (Optional) define a custom agent brief (1-2 min)

Use `custom-agent-brief-template.md` when the same workflow is repeated often (for example, docs normalization or dependency hygiene).

Custom agents are worth it when:
- The task repeats weekly.
- Inputs are consistent.
- Success criteria are stable.

Skip custom agents for one-off work.

## Step 4 - Run the final prompt (3-5 min)

**Option A — Copilot Coding or Cloud agent:**

Paste this into Copilot Coding or Cloud agent:

> Execution mode. Follow repository instructions and this task packet.
>
> Read ONLY:
> - #file:demos/06-copilot-coding-cloud/context-packet.md
> - #file:demos/06-copilot-coding-cloud/custom-instructions.md
> - files explicitly listed in the context packet
>
> Do the work in minimal diffs, run validation commands from the packet, and stop as soon as all checks are green.
> If any requirement conflicts, report the conflict before making additional edits.

**Option B — local Copilot Chat:**

Open a new chat, attach files with `#file:`, then paste:

> Follow the instructions in #file:demos/06-copilot-coding-cloud/custom-instructions.md and the task defined in #file:demos/06-copilot-coding-cloud/context-packet.md.
>
> Do not read any other files unless they are listed in the context packet.
> Make minimal diffs. Run the validation commands from the packet. Stop as soon as all checks pass.
> If any requirement conflicts, report the conflict before editing further.

The key lesson is identical in both surfaces: **a tight context packet and lean instructions reduce retries more reliably than a larger model.**

## What to notice

- The agent works only within the files listed in the context packet — it doesn't expand scope on its own.
- Short, specific instructions produce more reliable output than long generic ones.
- The agent stops at the defined condition after validation passes.
- If the run drifts, the packet or instructions are usually the cause — not model capability.
