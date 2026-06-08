# Demo 07 — Managing Context in Local IDE

**Time:** ~10 minutes  
**Recommended model:** Any — the lesson applies regardless of model  
**No code required.** This demo runs entirely in Copilot Chat.

## Why this demo exists

Token cost isn't just about prompt length. Accumulated context — stale history, irrelevant file references, prior task artifacts — silently inflates every subsequent turn. This demo teaches four concrete signals for shaping context deliberately, and what to do when you notice each one.

Use this demo in place of Demo 06 if participants don't have Copilot Coding or Cloud agent access.

## The four signals

| Signal | Symptom | Response | Token impact |
|---|---|---|---|
| **1. Topic shift** | You're starting a genuinely new task in the same chat | Start a new chat | Avoids injecting all prior history into an unrelated task; can eliminate hundreds of stale lines per turn |
| **2. Context drift** | The model starts hedging, repeating old decisions, or re-asking questions you already answered | Compact and re-anchor mid-session | Collapses N turns of noisy history into one clean summary |
| **3. Stale instructions** | Repo-scoped instructions contradict the current task or are too broad to constrain correctly | Override locally or narrow scope explicitly in your prompt | Prevents the model from pattern-matching to wrong prior context |
| **4. Cold re-entry** | You or a teammate returns to a task after a break with no shared context | Paste a re-anchor prompt before anything else | Avoids a multi-turn reconstruction round that wastes both tokens and time |

See [`context-signals.md`](context-signals.md) for the one-page reference card.

---

## Signal 1 — When to start a new chat

**Rule:** Start a new chat when the topic, goal, or model changes.

The session history is injected into every subsequent prompt. When you switch from "debug this function" to "write docs for this module," the debug trace is noise — and it costs tokens whether it's relevant or not.

**Live demo:**

> Paste the bad prompt (left chat) and the good prompt (right chat). Both should produce a working result, but compare response length and whether the model re-explains things from the prior "task."

Bad: continue the Demo 03 debug chat and ask for docs in the same session.

Good: open a new chat, ask for docs with a clean scoped prompt.

**Point out:** Response length shrinks. The model doesn't hedge with "as we discussed earlier…"

**Reset signal:** Start a new chat whenever you'd say "actually, forget all that — I want to do something different."

---

## Signal 2 — Compact and continue

**Setup (run this before the demo):** Build a noisy chat state first so the contrast is real.

1. Open a new Copilot Chat.
2. Paste these turns in sequence — wait for a response to each before pasting the next:

   > Turn 1: "I'm working on a Python CLI that checks markdown links. What libraries are available for parsing markdown in the standard library?"
   
   > Turn 2: "OK, let's use re and pathlib. Write a function that extracts all local file links from a markdown string."
   
   > Turn 3: "That works but I also want to check if the files actually exist. Can you extend it?"
   
   > Turn 4: "Now I want to add a --verbose flag. Actually, wait — can we make the output format configurable? Like JSON or plain text?"

3. Now you have a realistically noisy session: a scope change mid-flight, prior decisions, and accumulated output.

**The compact prompt (paste this as Turn 5):**

> Summarize what we've built so far in bullet form: what the function does, what arguments it takes, and what's still unresolved. Keep it under 10 lines.
>
> After the summary, continue with: add a `--format` flag that accepts `json` or `plain` (default: `plain`). Do not repeat context from the summary.

**Point out:** The summary collapses four turns of history into ~10 lines. The continuation prompt builds cleanly on that without the model needing to re-read everything.

---

## Signal 3 — When repo instructions become a liability

Persistent instructions in `.github/copilot-instructions.md` are always-on. That's powerful when they're current and well-scoped — and a liability when they're not.

**When repo instructions hurt:**

- They describe a convention you've since changed.
- They're written for one team's workflow and you're doing something outside that workflow.
- They're too broad ("always add comments") and contradict your task ("return only the corrected code, no comments").

**Live demo:** Look at the repo's [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) together.

Ask: "If I were doing a quick one-off script, which of these instructions would get in my way?" (Usually: type hints on one-liners, ruff enforcement when you're iterating fast.)

**The fix:** Override locally in the prompt.

> Ignore repo style instructions for this task only. Return a quick script with no type hints, no docstrings. Optimize for speed, not polish.

**Point out:** You don't need to edit `copilot-instructions.md`. A local override in the prompt takes precedence for that turn. Edit the repo instructions only when the override is permanent.

---

## Signal 4 — Clear and re-anchor

When you return to a task after a break — or hand off to a teammate — the context is gone. Don't reconstruct it through conversation turns. Write a re-anchor prompt once and paste it at the top of a fresh chat.

**Re-anchor prompt template:**

```
Context re-anchor. We are working on [one-sentence description].

State so far:
- [Decision 1 already made]
- [Decision 2 already made]
- [What's passing, what's failing]

Current task: [exactly what we're doing next]

In scope: [files or areas]
Out of scope: [explicit non-goals]

Start from here without re-explaining.
```

**Live demo:** Use the Demo 05 scenario. After the Research phase, close the chat and open a new one. Paste a re-anchor prompt that summarizes the research output, then continue into the Plan phase — with a different model — without repeating yourself.

**Point out:** This is also how you change models mid-workflow without re-explaining everything. Write the re-anchor, switch the model, paste it in. The new model starts informed.

---

## What to point out live

- Context is not free — every turn injects the full history.
- The model doesn't tell you when context is hurting it. You have to notice.
- Compacting, re-anchoring, and new-chat signals are the same skill: **deliberately managing what the model sees**.
- These techniques work identically in local Copilot Chat and in Copilot Coding / Cloud agents — the principle is model-agnostic.

## Reset before the next demo

Click **New chat** in Copilot Chat. If you ran the Signal 2 setup sequence, discard that session.
