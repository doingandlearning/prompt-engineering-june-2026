# Module 4 — Exercises

**For delegates.** Run in VS Code with Copilot, Codex, and/or Claude active.

---

## Objective

By the end of these exercises you will be able to:

- Read inline suggestions critically before accepting them
- Use `/explain`, `/fix`, and `/tests` and notice what each misses
- Generate a multi-layer feature from a spec and find where output diverges
- Write a spec usable in real code review
- Draft a context header and test it against a generation task

---

## Exercise 1: Inline — signal and what it changes

**Individual (10 minutes)**

Open a new Python file. Generate a simple model class three times with increasing signal.

**Round 1 — minimal signal:**

```python
class Task:
```

**Round 2 — named intent:**

```python
# SQLAlchemy model: task in a project management system.
# Fields: id, title (required, max 100), description (optional),
# priority (enum: low, medium, high), created_at (UTC), owner_id (int).
class TaskItem:
```

**Round 3 — pattern started:**

```python
class TaskItem(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
```

**Decision:** For each situation below, would you use **inline** or **chat**?

- A Pydantic request model with eight known fields
- A service method with non-obvious null/whitespace handling
- Completing a `match`/`case` over a known enum you've started
- A repository interface before the entity exists

Type answers in chat and defend one you're unsure about.

---

## Exercise 2: Chat — slash commands

**Individual (15 minutes), then breakout (5 minutes)**

```python
class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    async def create_async(self, request: CreateTaskRequest) -> TaskItem:
        if not request.title or not request.title.strip():
            raise ValueError("Title is required")
        if len(request.title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        task = TaskItem(
            title=request.title,
            description=request.description,
            priority=request.priority,
            created_at=datetime.now(timezone.utc),
            owner_id=request.owner_id,
        )
        return await self._repository.save_async(task)

    async def get_by_owner_async(
        self, owner_id: int, priority_filter: Priority | None = None
    ) -> list[TaskItem]:
        tasks = await self._repository.get_by_owner_async(owner_id)
        if priority_filter is not None:
            tasks = [t for t in tasks if t.priority == priority_filter]
        return sorted(tasks, key=lambda t: t.created_at, reverse=True)
```

**Part A — `/explain`:** Select `get_by_owner_async`. Does the explanation correctly describe when filtering happens relative to the DB call?

**Part B — `/fix`:** Add:

```python
async def delete_async(self, task_id: int, requesting_user_id: int) -> None:
    task = await self._repository.get_by_id_async(task_id)
    task.deleted_at = datetime.now()
    await self._repository.save_async(task)
```

Problems: no null check on `task`, naive `datetime.now()`, no ownership check. Does `/fix` catch all three?

**Part C — `/tests`:** Run `/tests` on the class. Cover empty title, title too long, and each priority filter value.

**Breakout:** Which `delete_async` problem is most dangerous if missed?

---

## Exercise 3: Spec-driven — generate and find divergence

**Individual (20 minutes), then whole group**

```markdown
## Feature: Update task priority

**Stack:** Python 3.11, FastAPI, SQLAlchemy 2.0. Constructor injection. Errors as HTTPException with consistent JSON shape.

**Endpoint:** PATCH /api/tasks/{id}/priority

**Request:** priority (string — Low, Medium, High)

**Behaviour:**
- Validate priority is allowed
- Check task belongs to requesting user (owner_id)
- Update and save
- 200 with TaskDto on success
- 404 if not found
- 403 if owned by another user
- 400 with field error if invalid priority

**Acceptance criteria:**
- [ ] Invalid priority → 400 with field error
- [ ] Not found → 404
- [ ] Wrong owner → 403, not 404
- [ ] Success → 200 with updated TaskDto
```

Generate in layers: request schema → service → route → pytest.

**Answer:** Where did output diverge? (403 vs 404, error shape, naming.)

Type in chat: the most important divergence and the one-line spec addition that would have prevented it.

---

## Exercise 4: Write a spec for production

**Breakout — 15 minutes**

Feature from your work spanning at least two layers. Use markdown spec or user story format (see Module 4 slides).

Partner review:
1. Implementable without clarifying questions?
2. Every acceptance criterion testable?
3. Ownership/auth edge case covered?

Give one specific rewrite of the weakest criterion.

---

## Exercise 5: Context header — draft and test

**Individual (15 minutes)**

Draft a **context header** (10–20 lines) for your area of the codebase:

```markdown
## Context for AI assistance — [team/area name]

**Stack:** Python 3.11, FastAPI, SQLAlchemy 2.0, MySQL, pytest
**Patterns:** Constructor injection; repositories in `repositories/`; no bare except
**Naming:** snake_case; suffix services with `_service`
**Do not:** Generate Django code; use sync session in async routes; log PII
**Review:** Run pytest for changed modules before suggesting merges
```

Paste the header + a small generation task (e.g. "add `find_overdue_loans` to LoanService") into chat.

**Evaluate output** against your header. What conformed? What didn't? Refine one line in the header to fix the biggest gap.

**Optional:** Compare the same task without the header — what changed?

---

## Before you finish

- [ ] Inline signal observed (Exercise 1)
- [ ] Slash commands — noted misses (Exercise 2)
- [ ] Spec divergence found (Exercise 3)
- [ ] Partner-reviewed spec (Exercise 4)
- [ ] Context header drafted and tested (Exercise 5)

Keep Exercise 4's spec and your context header — refine them on first real use.
