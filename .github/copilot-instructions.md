# Copilot instructions for this repo

This is a **workshop demo** for model selection and token efficiency. Code here is intentionally small and didactic; do not refactor demos to make them "more realistic."

## Conventions
- Python 3.11+, standard library only unless a demo's `README.md` says otherwise.
- Use `ruff` for lint, `pytest` for tests. Both must pass before commits.
- Functions over classes unless state is genuinely required.
- Type hints on public functions; skip on one-line helpers.

## Demo discipline
- Each `demos/NN-name/` directory is self-contained. Do not import across demos.
- Each demo has a `README.md` with the **exact prompt** to paste during the workshop. Do not edit the prompt without testing the demo end-to-end.
- Tests in a demo describe the intended final behavior. They may start failing on purpose — that's the demo.

## Output expectations
- Be concise. No preamble like "Sure, I can help with that."
- Show diffs, not whole files, unless the file is new.
- If you're unsure which model the user is on, ask before doing multi-file work.
