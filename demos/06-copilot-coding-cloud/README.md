# Demo 06 - Copilot Coding / Cloud agent finale

**Time:** ~8-12 minutes
**Recommended model mode:** **Auto** first, then pin a model only if needed for reproducibility
**Goal:** show a realistic, moderately complex workflow where quality depends on context shaping and instruction quality, not just model size.

This finale is designed to be run in either:
- VS Code Copilot Coding flow
- GitHub Copilot Cloud agent flow

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

## What to point out live

- Better context beats bigger model once tasks become multi-file.
- Short custom instructions improve reliability more than long instruction documents.
- Cloud agent and local Copilot Coding both benefit from the same handoff packet pattern.
- If the run drifts, the packet or instructions are usually the issue (not model capability).

## Exit criteria

- The audience sees a complete run with a bounded context packet.
- Instructions are concise and task-specific.
- The agent stops at the defined stop condition after validation.
