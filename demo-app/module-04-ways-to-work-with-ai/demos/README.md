# Module 4 — Demos

Facilitator notes and prompt scaffolds for the Module 4 live demos.

## Demo 1: PRD-driven generation sequence

**Purpose:** Show the layered generation pattern — spec first, then DTO → service → router → tests in sequence.

**Materials:**
- `01-prd-driven-generation.md` — facilitator walkthrough
- `prompts/update-task-priority-spec.md` — sample PRD (from slides)
- `prompts/prd-generation-prompts.txt` — copy-paste prompt scaffolds for each layer

**Setup:**
- VS Code with Copilot Chat, Codex, or Claude sidecar open
- Python/FastAPI project context (Module 3 code samples work well)
- Paste the spec once; generate each layer in sequence, referencing previous output

**When:** During Mode 3 (PRD-driven development) section (~10 minutes live)

---

## Presenter notes

- Use **synthetic examples** only (Library Management / task priority feature).
- Emphasize that the **spec is the source of truth** — divergence means a spec gap, not a prompt failure.
- After each layer, paste the generated code back into the next prompt so naming stays consistent.
- If output diverges, refine the spec and re-run — don't start from scratch.
