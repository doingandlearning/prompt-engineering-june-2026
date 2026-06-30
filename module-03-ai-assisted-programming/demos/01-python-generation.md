# Demo 1: Python generation — from spec to working code

## Goal

Show delegates how to generate a complete application layer (SQLAlchemy model, repository, service) from a simple specification, then refine iteratively.

**Teaching style**: Problem-first approach, progressive building

**Stack note:** Python backend is the primary demo. Mention that the same incremental pattern applies to React/Node/PHP — one layer at a time, review each checkpoint.

---

## Before the demo

- Ensure you have access to an AI chat tool (Copilot Chat, Claude, or Codex in VS Code).
- Use only **synthetic** examples (no real internal code or APIs).
- Have an IDE ready to show the generated code is syntactically valid (optional but helpful).

---

## Steps

### 1. Set up the problem (2 min)

**Say:** "Imagine you need a Book model with SQLAlchemy mappings, a repository abstraction, and a service method. How long does this take manually?"

**Show the pain:**
- Write model class: 5 minutes
- Add SQLAlchemy mappings: 2 minutes
- Create repository abstraction: 3 minutes
- Write service class: 5 minutes
- **Total: 15+ minutes** of repetitive boilerplate

---

### 2. Show the initial prompt (2 min)

**Display the prompt** (from `prompts/01-python-generation-prompts.txt`, Prompt 1):

> Generate a SQLAlchemy 2.0 declarative model for a Book with id, title, author, isbn, published_year. Python 3.11+, Mapped[] style, MySQL.

**What to say:**
- Clarity: what we want (model)
- Context: SQLAlchemy 2.0, Python 3.11, MySQL
- Constraints: specific fields and types
- This follows the 3Cs from Module 2

---

### 3. Generate the model (3 min)

Run the prompt. Point out:
- Complete model with type hints
- Proper SQLAlchemy 2.0 `Mapped[]` style
- Field constraints reflected in column definitions

**Say:** "30 seconds instead of 15 minutes — but review before you paste."

---

### 4. Add repository and service (3 min)

**Refine** (Prompt 2): repository + service with constructor injection.

Point out:
- Repository exposes query methods
- Service uses constructor injection
- Clear return shape for API layer

**Say:** "Build incrementally — model first, then repository, then service."

---

### 5. Refine for team style (3 min)

**Refine** (Prompt 3): PEP 8, explicit types, empty-result handling, no bare except.

**Say:** "Iterative refinement — review, identify gaps, refine the prompt."

---

### 6. Review checklist (2 min)

- **Correctness:** Does it run / type-check?
- **Version:** Python 3.11+, SQLAlchemy 2.0?
- **Style:** Constructor injection? Team naming?
- **Security:** Obvious issues? (SQL injection via raw strings, etc.)
- **Tests:** Can we test this? (Demo 4)

**Say:** "Always review before pasting into your codebase."

---

## Time Allocation

~15 minutes total
