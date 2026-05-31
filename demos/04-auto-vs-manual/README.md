# Demo 04 — Auto vs. manual, head-to-head

**Time:** ~10 minutes
**This demo runs no new code.** It re-runs the prompts from demos 01–03 through **Auto** and compares results to the deliberate manual picks.

## Why this matters

Auto in VS Code Copilot Chat is **task-optimized and intent-based** — it evaluates the complexity of each turn and routes to the model best suited for that intent, while also accounting for real-time system health. It even routes along **cache boundaries** to avoid the cost of mid-session model swaps.

So the question is no longer "is Auto good enough?" It's: **for a mixed-task day, does Auto match or beat what I'd pick by hand — without me having to think about it?**

## How to run it

You'll re-run three of the prompts you already used. Each one starts from a clean state.

> Tip: if your VS Code layout supports it, open two chat panes side-by-side and run Auto on the left, manual pick on the right.

### Round 1 — lightweight task (Demo 01 prompt)

1. **Reset Demo 01.** From a terminal:
   ```bash
   git checkout demos/01-lightweight/messy.py
   ```
2. Start a new chat. Set the model to **Auto**.
3. Paste the prompt from [demos/01-lightweight/README.md](../01-lightweight/README.md#the-exact-prompt-to-paste).
4. Note: which model did Auto route to? (Hover over the assistant response in Copilot Chat.) How does the diff compare to the lightweight-model run from Demo 01?

### Round 2 — execution task (Demo 02 prompt)

1. **Reset Demo 02.**
   ```bash
   git checkout demos/02-execution/cart.py
   ```
2. Start a new chat. Set the model to **Auto**.
3. Paste the prompt from [demos/02-execution/README.md](../02-execution/README.md#the-exact-prompt-to-paste).
4. Note: did Auto pick the same tier as you did manually in Demo 02? How does turn time / number of tool calls compare?

### Round 3 — reasoning task (Demo 03 prompt)

1. **Reset Demo 03.**
   ```bash
   git checkout demos/03-reasoning/inventory.py
   ```
2. Start a new chat. Set the model to **Auto**.
3. Paste the prompt from [demos/03-reasoning/README.md](../03-reasoning/README.md#step-2--switch-to-a-reasoning-model).
4. Note: did Auto pick a reasoning-tier model? Did it find the root cause, or fix the symptom?

## Scorecard

Use [`scorecard.md`](scorecard.md) as a template — fill it in live and project it. The participants see Auto vs. manual scored on the same three tasks in the same room. That's the demo.

## What to point out

- Auto's routing depends on **intent**, not just availability — so the same prompt structure can be routed to different tiers across rounds. That's the feature, not a bug.
- On the **execution** round, you should see Auto stay in the general-purpose tier even if you've been pushing it through harder tasks all session. **Cache-boundary routing** keeps it from thrashing.
- The **10% Auto discount** on paid plans applies to all of these turns. Note that out loud.
- Where Auto *doesn't* match your manual pick, ask: was my manual pick actually better, or was I just defaulting to a habit?

## When to override Auto (recap)
- Architecture / naming / boundary decisions → pin a reasoning model.
- Long sequences of nearly-identical edits → pin a lightweight model.
- Benchmarks / reproducibility / regression bisects → pin a specific model.
- Everything else → trust Auto.

## Reset before the next demo

> Click "New chat", and run `git checkout demos/` from the terminal to reset all demo files to their starting state.
