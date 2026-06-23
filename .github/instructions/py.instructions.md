---
description: Python best practices
applyTo: "**/*.py"
---

# General Guidelines

- **Use pytest**, not unittest
- **Pass `ruff` lint** and **`pytest`** tests before commit
- **Type hints on public functions** (skip internal helpers)
- **Comment the why, not the what**

# Core Principles

- Functions over classes (unless state is required)
- Standard library first
- Comprehensions over loops
- Clear, concise names

