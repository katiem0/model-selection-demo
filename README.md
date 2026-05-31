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

## What's in here

| Path | Purpose |
| --- | --- |
| [docs/model-cheatsheet.md](docs/model-cheatsheet.md) | One-page reference: task → recommended tier → model |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Example of the concise, repo-scoped instructions advocated in §5 |
| [demos/01-lightweight/](demos/01-lightweight/) | Refactor & document a messy module — lightweight tier shines |
| [demos/02-execution/](demos/02-execution/) | Implement from a clear spec — general-purpose / Codex tier sweet spot |
| [demos/03-reasoning/](demos/03-reasoning/) | Diagnose a subtle bug across files — reasoning tier earns its cost |
| [demos/04-auto-vs-manual/](demos/04-auto-vs-manual/) | Run the same three tasks through Auto and compare to manual picks |
| [demos/05-research-plan-implement/](demos/05-research-plan-implement/) | Full R→P→I walkthrough on a small CLI (markdown link checker) |

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
