# Module 3: AI-Assisted Development in Python (and Beyond)

## Learning objectives

- Use AI to generate models, repositories, and services in Python (SQLAlchemy, FastAPI patterns).
- Use AI to explain legacy Python, PHP, or JavaScript and unfamiliar codebases.
- Apply refactoring strategies with AI: type hints, comprehensions, readability — with tests before and after.
- Generate unit tests (pytest, `unittest.mock`; Jest for frontend track) with AI assistance.
- Evaluate AI output for correctness, style, and fit before applying it.
- *(BAs)* See how structured Jira tickets become effective prompt context.

## Suggested talking points

- Code generation: incremental layers; when to generate vs write manually.
- Code explanation: four layers (what, why, modern equivalent, risks).
- Refactoring: constraints in the prompt; never without tests.
- Unit testing: name scenarios explicitly; run before trusting.
- Review before paste: wrong APIs, outdated patterns, security.
- Frontend parallel: React/Node/PHP worked example (`demos/06-frontend-worked-example.md`).
- Jira-to-code: cross-functional demo (`demos/05-jira-to-code.md`).

## Suggested demos

| Demo | File | Focus |
|------|------|--------|
| 1 | `01-python-generation.md` | Model → repository → service |
| 2 | `02-legacy-explanation.md` | Layered explanation |
| 3 | `03-refactoring.md` | Safe refactor with pytest |
| 4 | `04-unit-testing.md` | pytest + mock, refine on failure |
| 5 | `05-jira-to-code.md` | **BA + dev** — ticket as prompt |
| 6 | `06-frontend-worked-example.md` | React/Node/PHP parallel |

## Suggested exercises

See `exercises/README.md` — generate, explain, refactor, test, plus Jira debrief.

## Suggested running time

90–120 minutes (anchor module; includes Jira demonstration)

## BA track

Fully participate in Modules 1–2. Module 3: hands-on optional; **must attend Demo 5 (Jira-to-code)**. Evaluation checklist language applies to requirements quality, not only code.
