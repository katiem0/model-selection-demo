# Demo 07 — Managing Context in Local IDE

**Time:** ~10 minutes
**Recommended model:** Any — the lesson is model-agnostic
**No code required.** This demo runs entirely in Copilot Chat.

> Use this demo in place of Demo 06 if participants don't have Copilot Coding or Cloud agent access.

## The setup

Token cost isn't just about prompt length. Every turn injects the full session history — stale decisions, topic changes, and prior task artifacts inflate every subsequent turn silently. This demo walks through four concrete signals and what to do when you notice each one.

Reference card: [`context-signals.md`](context-signals.md)

## Signal 1 — Start a new chat

Continue the Demo 03 debug chat and ask for docs in the same session. Then open a fresh chat and ask for the same docs.

## What to notice

- The fresh-chat response is shorter and doesn't reference the prior debug session.
- Old context was injecting itself into an unrelated task.
- **Rule:** new task or new model = new chat.

## Signal 2 — Compact and continue

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

## Signal 3 — Override stale instructions

Open [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) with the audience. Ask which instructions would get in the way of a quick one-off script.

Paste a local override:

> Ignore repo style instructions for this task only. Return a quick script with no type hints, no docstrings. Optimize for speed, not polish.

## What to notice

- The response follows the local override, not the repo instructions.
- No file edits needed for a one-off exception.
- Look at how much shorter the output is when the style constraints are lifted for this task.

## Signal 4 — Re-anchor on a fresh chat

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

Click **New chat** in Copilot Chat. Discard any sessions opened during Signal 2 setup.
