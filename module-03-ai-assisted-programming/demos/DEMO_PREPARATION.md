# Module 3 Demo Preparation Guide

**CRITICAL:** Module 3 is the anchor module. These demos must work.

---

## Pre-Demo Setup Checklist

### Python environment

1. Python 3.11+ with venv optional
2. `pip install sqlalchemy pytest` (mock is stdlib)
3. Folder layout for live coding (optional):

```
library_demo/
├── models/
│   ├── book.py
│   └── user.py
├── repositories/
│   └── book_repository.py
├── services/
│   ├── book_service.py
│   └── user_service.py
└── tests/
    ├── test_book_service.py
    └── test_user_service.py
```

4. Use `demos/code-samples/` as templates
5. Verify `pytest` runs (even empty tests)

### Jira demo

- [ ] `prompts/jira-ticket-sample.md` ready to paste
- [ ] Weak ticket example in facilitator notes (`05-jira-to-code.md`)

### Frontend handout

- [ ] `06-frontend-worked-example.md` printed or linked for React/Node/PHP delegates

---

## Demo-by-Demo

| Demo | File | Verify |
|------|------|--------|
| 1 Python generation | `01-python-generation.md` | Prompts in `01-python-generation-prompts.txt` |
| 2 Legacy explanation | `02-legacy-explanation.md` | `legacy_user_bean.py` |
| 3 Refactoring | `03-refactoring.md` | Test passes before/after |
| 4 Unit tests | `04-unit-testing.md` | pytest green after refine |
| 5 Jira-to-code | `05-jira-to-code.md` | Strong ticket → service + tests |
| 6 Frontend | `06-frontend-worked-example.md` | Optional 5–10 min |

---

## Timing (suggested)

- Demos 1–4: ~15 min each
- Exercises 1–4: per `exercises/README.md`
- Demo 5 Jira: ~10 min (whole group)
- Demo 6 or handout: as needed

---

## Notes

- Synthetic code only in live demos
- `demo-codebase/` (C# TaskManagement) is **legacy** — not used for this delivery
- Review-before-paste checklist is language-agnostic
