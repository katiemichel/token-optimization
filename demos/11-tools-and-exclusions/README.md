# Demo 3 — Disable unneeded tools & exclude files from context

**Time:** ~5 minutes
**Recommended model:** Any. The lesson is about what you send to the model, not which model you pick.
**Prereq (optional):** Have the GitHub MCP server enabled, or any MCP server with multiple toolsets, so Step 1 has something visibly large to disable.

## Why this demo exists

Two invisible costs in every chat session:

1. **Every enabled tool definition** is input tokens, on every single turn.
2. **Every "interesting" file in the workspace** can show up as a search snippet — even if the agent never opens it — and that snippet counts toward the context window.

Both are easy to fix. Neither requires changing models.

## Step 1 — Tool surface area (90 sec)

Open a fresh chat. Click the **Configure Tools** button in the chat input.

Show the panel. Count out loud:

- How many tools are enabled by default?
- How many MCP toolsets are enabled? (If the GitHub MCP server is on, expand it — there are dozens of tools in there.)

Now ask the room: *"For the next prompt — refactor a single function — how many of those tools will actually fire?"* (Usually: 2–3 file tools.)

Disable everything except the file-reading and edit tools. Then paste:

> Rename the parameter `x` to `items` in #file:demos/01-lightweight/messy.py. Show the diff only. Do not run tests.

> Talking point: "We just removed dozens of tool definitions from every turn in this session. The model never needed them. Custom agents take this further with a hardcoded `tools:` list — see Demo 2."

**Important:** Toggling tools **invalidates the prompt cache** (Demo 1, Step 5). Configure tools at the **start** of a session, not mid-task.

## Step 2 — The workspace exclusions you probably need (90 sec)

Open [`example-vscode-settings.jsonc`](example-vscode-settings.jsonc) in the editor.

Walk through three different exclusion mechanisms — they behave differently:

| Setting | Hides from explorer | Excludes from workspace index | Excludes from agent text search |
| --- | --- | --- | --- |
| `.gitignore` | No | Yes | Yes |
| `files.exclude` | Yes | Yes | Yes |
| `search.exclude` | No | No | Yes |

Common patterns to exclude from agent context:

- `**/node_modules/**`, `**/.venv/**`, `**/dist/**`, `**/build/**` — build outputs
- `**/*.lock`, `**/package-lock.json`, `**/poetry.lock`, `**/uv.lock` — lockfiles
- `**/coverage/**`, `**/.pytest_cache/**`, `**/.ruff_cache/**` — generated artifacts
- `**/*.min.js`, `**/*.map` — bundled output
- Large fixture or snapshot files that aren't useful as agent context

> Talking point: "**Search match snippets count toward context even when the agent doesn't open the file.** A noisy workspace inflates every grep-style turn silently. Excluding the obvious paths is the single highest-leverage one-time edit you can make to a repo."

## Step 3 — Prove the difference (60 sec)

Optional but powerful if time allows.

Create a temporary file `/tmp/noise.txt` (or in a scratch directory in the workspace) with a few hundred lines of repeated content. Or just point at `.venv/`.

In a **fresh chat**, paste:

> Search the workspace for any reference to `process_data` and summarize where it's used.

Note the per-turn cost. Now add `**/.venv/**` and `**/*.lock` to `search.exclude`, **start a new chat** (settings changes that affect indexing are cleanest with a fresh session), and re-run the same prompt.

Compare the per-turn cost. The smaller search surface produces shorter responses and lower input-token counts.

## Step 4 — MCP toolset selection (30 sec)

If you use MCP servers with multiple toolsets (GitHub MCP is a good example), point out:

- Most MCP servers let you enable a subset of toolsets, not the whole server.
- For a code-review session, you probably need `repos` and `pull_requests`, not `actions` or `secret_scanning`.
- Each enabled toolset is more input tokens per turn — the same logic as in-VS-Code tools.

> Talking point: "Treat tools and MCP toolsets like dependencies — only what the current task needs."

## What to notice

- Configure Tools is the fastest no-code win in the room.
- File exclusions affect **search snippets**, which are the most underestimated input-token cost.
- All of this is set-it-once: edit your settings or `.gitignore` once, save tokens forever.

## Reset before the next demo

> Click **New chat**. Demo 4 starts clean.
