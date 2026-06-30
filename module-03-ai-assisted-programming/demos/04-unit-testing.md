# Demo 4: Unit test generation — tests that work

## Goal

Show delegates how to generate pytest tests with `unittest.mock`, run them, and refine when tests fail.

---

## Steps

### 1. Set up the problem (2 min)

Manual test writing pain for `find_books_by_author`.

### 2. Generate basic tests (3 min)

**Prompt:**

> Generate pytest tests for this service method. Use unittest.mock. Cover happy path, None input, empty string, whitespace-only author. Python 3.11+.

```python
class BookService:
    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    def find_books_by_author(self, author: str | None) -> list[Book]:
        if author is None or not author.strip():
            return []
        return self._repository.find_by_author_containing_ignore_case(author)
```

### 3. Run tests (3 min)

`pytest` — pass or fail drives learning.

### 4. Refine (3 min)

Fix mock setup or whitespace case via prompt refinement.

### 5. Add edge cases (2 min)

Repository throws, author not found, etc.

### 6. Test quality checklist (2 min)

Coverage, mocks, assertions, actually run.

---

## Time Allocation

~15 minutes total
