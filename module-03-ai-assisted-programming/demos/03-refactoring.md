# Demo 3: Refactoring with AI — modernizing safely

## Goal

Show delegates how to refactor verbose procedural code to idiomatic Python (list comprehensions, type hints), with emphasis on safety (tests before/after).

---

## Before the demo

- AI chat tool available
- IDE with sample code and pytest ready
- Passing test before refactoring (critical)

---

## Steps

### 1. Set up the problem (2 min)

Verbose `get_active_user_emails` — nested loops, manual null checks. Same behaviour required after refactor.

### 2. Show the test first (2 min)

Run pytest — must pass before refactor.

### 3. Generate refactored code (4 min)

**Prompt:**

> Refactor this method to use a list comprehension and filter. Maintain exact behaviour — same inputs, same outputs. Python 3.11+.

```python
def get_active_user_emails(users: list[User | None]) -> list[str]:
    emails: list[str] = []
    for user in users:
        if user is not None and user.is_active and user.email and user.email.strip():
            emails.append(user.email)
    return emails
```

### 4. Apply and test (3 min)

Replace method, run pytest. If fail — diagnose and refine prompt.

### 5. Compare before/after (2 min)

Readability vs behaviour — diff review.

### 6. Safety checklist (2 min)

Tests before, review diff, tests after, behaviour unchanged.

---

## Sample test (pytest)

```python
def test_get_active_user_emails_returns_only_active_with_email():
    users = [
        User("John", "john@example.com", True),
        User("Jane", "jane@example.com", False),
        User("Bob", None, True),
        None,
    ]
    assert service.get_active_user_emails(users) == ["john@example.com"]
```

---

## Time Allocation

~15 minutes total
