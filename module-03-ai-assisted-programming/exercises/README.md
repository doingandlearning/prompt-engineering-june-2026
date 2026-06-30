# Module 3 — Exercises

**For delegates.** These exercises run during the Module 3 session. Your facilitator will manage timing and breakout rooms.

**Audience:** Python is the default hands-on language. Frontend developers may complete Exercise 4 using the Jest variant in `demos/06-frontend-worked-example.md`. Business analysts observe the Jira demonstration (Demo 5) and participate in debrief — no IDE required.

---

## Objective

By the end of these exercises you will be able to:

- Generate Python code incrementally and evaluate each layer before proceeding
- Use layered explanation prompts to build understanding of unfamiliar code
- Refactor safely — with tests before and after — and verify behaviour is unchanged
- Generate pytest tests, run them, and diagnose failures as prompt refinement opportunities

---

## Scenario

You're working on a Library Management System — a Python/FastAPI service managing books, authors, and loans. A colleague has been using AI to accelerate their work, and you're reviewing their output before it goes into the codebase.

**Remember:** Use only synthetic examples or generic patterns — not proprietary code or internal APIs.

---

## Exercise 1: Generate incrementally — and catch the mistake

**Individual (10 minutes), then breakout (5 minutes)**

Generate a `Loan` model layer using AI in stages. At least one stage should produce output you shouldn't accept.

**Stage 1:** Generate the SQLAlchemy model.

The `Loan` model needs:
- `id`: int, primary key, auto-generated
- `book_id` and `user_id`: int, foreign keys
- `loan_date`: date
- `return_date`: date | None
- `status`: str — values `ACTIVE`, `RETURNED`, `OVERDUE`

Apply the evaluation checklist before stage 2. **Write down one thing you had to fix.**

**Stage 2:** Add repository abstraction (feed stage 1 output as context).

**Stage 3:** Add `LoanService.find_active_loans()` returning loans with status `ACTIVE`.

**Breakout:** Which checklist item — correctness, version, style, security, testability — is most likely to catch a real problem in your codebase?

---

## Exercise 2: Explain legacy code in layers

**Individual (10 minutes), then whole group**

```python
class OrderProcessor:
    def __init__(self) -> None:
        self._orders: list[Order] = []
        self._totals: dict[str, float] = {}

    def process_orders(self) -> None:
        for order in self._orders:
            if order is not None and order.status == "PENDING" and order.customer_id:
                current = self._totals.get(order.customer_id, 0.0)
                self._totals[order.customer_id] = current + order.amount

    def get_total_for_customer(self, customer_id: str) -> float:
        return self._totals.get(customer_id, 0.0)
```

Run four prompts in order:

1. What does this code do?
2. Why might it have been written this way?
3. What would the modern Python 3.11+ equivalent look like?
4. What would break if you changed it?

**For prompt 4:** What does the model tell you to check — and what only you can answer from the real codebase?

**Type in chat:** one thing the model surfaced that you wouldn't have noticed reading alone.

---

## Exercise 3: Refactor safely

**Breakout — 15 minutes**

Refactor `process_orders()` to idiomatic Python (comprehensions, clearer structure). **Safe sequence:**

**Step 1:** Ask AI for pytest tests: happy path (two pending orders), order with empty `customer_id`, empty order list.

**Step 2:** Run tests against original code. Fix until green.

**Step 3:** Refactor with AI — behaviour must be identical.

**Step 4:** Run tests again.

**Key question:** Original skips `order is None` via `order is not None`. Does the refactored version skip `None` orders the same way? **If your pair disagrees, that's the most important feedback for the room.**

---

## Exercise 4: Generate and interrogate tests

**Individual (10 minutes), then breakout (5 minutes)**

```python
class BookService:
    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    def find_book_by_isbn(self, isbn: str | None) -> Book | None:
        if isbn is None or not isbn.strip():
            return None
        return self._repository.find_by_isbn(isbn)
```

**Step 1:** Prompt for pytest + mock: valid ISBN, `None`, `""`, not found.

**Step 2:** Run tests. Note failures.

**Step 3:** Find the gap. Guard uses `not isbn.strip()`. Does the model test whitespace-only `"   "` separately from `""`? Add that test.

**Breakout:** What categories does AI reliably cover vs consistently miss?

---

## Cross-functional: Jira-to-code (whole group)

**Facilitator-led — 10 minutes.** See `demos/05-jira-to-code.md`.

BAs: note how acceptance criteria became test cases. Developers: note what the ticket still didn't specify.

---

## Extensions

1. **FastAPI route:** Add `GET /loans/active` calling `find_active_loans()`.
2. **Constraint stress-test:** Remove one constraint from a good prompt; compare output degradation.
3. **Frontend track:** Run Exercise 4 with Jest on `findBooksByAuthor` (see `demos/06-frontend-worked-example.md`).
4. **Integration tests:** Ask for a FastAPI `TestClient` test — how does the prompt differ from unit tests?

---

## Before you move to Module 4

- [ ] Generated a model layer incrementally and caught at least one fix (Exercise 1)
- [ ] Ran four explanation layers and identified what layer 4 can't answer without your codebase (Exercise 2)
- [ ] Refactored with tests before/after and verified `None` order handling (Exercise 3)
- [ ] Found a test scenario the model missed and added it (Exercise 4)
- [ ] *(BAs)* Can name one ticket field that would improve AI-assisted implementation

In Module 4: sidecar vs inline workflows, context headers, and team standards. The evaluation checklist applies to all modes.
