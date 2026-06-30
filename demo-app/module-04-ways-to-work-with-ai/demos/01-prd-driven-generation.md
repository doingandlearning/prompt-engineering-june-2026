# Demo 1: PRD-driven generation — layered sequence

## Goal

Show delegates the full PRD-driven workflow: write a spec, then generate DTO → service → router → tests in sequence, with each layer referencing the previous output.

**When:** Mode 3 section (~10 minutes live). This is the highest-complexity demo in the course.

---

## Before the demo

- Open VS Code with Copilot Chat (or Codex / Claude sidecar).
- Have `prompts/update-task-priority-spec.md` ready to paste.
- Have `prompts/prd-generation-prompts.txt` open for the layer-by-layer prompts.
- Optional: show a blank file first to contrast "prompting without a spec" vs. with one.

---

## Steps

### 1. Set up the problem (2 min)

**Say:** "Inline gives you one line. Chat gives you one layer. A real feature spans DTO, service, router, and tests. Without a spec, each prompt guesses independently — you get inconsistent naming and missing error cases."

Walk through what PATCH `/api/tasks/{id}/priority` actually involves: request model, service method, router endpoint, unit tests.

---

### 2. Paste the spec (1 min)

Open `prompts/update-task-priority-spec.md`. Read the acceptance criteria aloud.

**Say:** "The acceptance criteria are what the tests will verify. If they're vague, the tests will be vague."

---

### 3. Layer 1 — Request model and validation (2 min)

Paste **Step 1** from `prd-generation-prompts.txt`.

Show the output. Point out:
- Field names match the spec
- Validation for allowed priority values
- Pydantic model, not a bare dict

**Say:** "I'm keeping this output — it goes into the next prompt."

---

### 4. Layer 2 — Service method (2 min)

Paste **Step 2** from `prd-generation-prompts.txt`, including the DTO from step 3.

Point out:
- Ownership check (403 vs 404 distinction from spec)
- Error cases match the behaviour list

---

### 5. Layer 3 — Router endpoint (2 min)

Paste **Step 3**. Show status codes and response shapes match the spec.

---

### 6. Layer 4 — Tests (2 min)

Paste **Step 4**. Show that each acceptance criterion has a corresponding test.

**Key moment:** "If a test is missing, that's not a model failure — it's a spec gap. Add the AC, re-run."

---

### 7. Handle divergence (1 min, if it happens)

If naming drifts (e.g. `TaskPriority` vs `Priority`):

> "The spec uses `Priority` throughout. Rename `TaskPriority` in the service to match."

**Say:** "Treat divergence as a spec refinement task. Update the spec so the next layer inherits the fix."

---

## If you run short on time

Cut the test layer — but **don't cut the spec + at least two layers**. Delegates need to see the sequence, not just hear about it.

---

## Debrief (30 sec)

- Spec defines shape before you prompt
- Each layer references the previous output
- Acceptance criteria become the review checklist
- Divergence = spec gap, not prompt failure

---

## Time allocation

| Section | Time |
|---------|------|
| Problem setup | 2 min |
| Paste spec | 1 min |
| DTO layer | 2 min |
| Service layer | 2 min |
| Router layer | 2 min |
| Tests layer | 2 min |
| Divergence (optional) | 1 min |
| **Total** | **~10–12 min** |
