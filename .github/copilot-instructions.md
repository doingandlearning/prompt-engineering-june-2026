# GitHub Copilot Custom Instructions

## Scope
- Applies to all work under `demo-codebase/`.
- This repository is a teaching codebase. Avoid "helpful" changes that remove intentional demo scaffolding unless explicitly requested.

## Source of truth
- Course context: [`readme.md`](../../readme.md)
- Demo flow and constraints: [`TEACHING_NOTES.md`](../TEACHING_NOTES.md)

## Build and test
- Install deps: from `demo-codebase/`, use `pip install -r requirements.txt`
- Run API: from `demo-codebase/`, use `uvicorn app.main:app --reload` (docs at `/docs`)
- Run tests: from `demo-codebase/`, use `pytest`

## Stack
- Python 3.11+, FastAPI, Pydantic v2
- pytest + unittest.mock
- In-memory repository (no external database)

## Architecture and coding rules
- Keep layering strict: Routers -> Services -> Repositories.
- Keep business logic out of routers.
- Use constructor injection (pass dependencies in, don't reach for globals).
- Use Pydantic models for request/response schemas.
- Keep async end-to-end; don't mix in blocking calls.

## Error handling rules
- Services raise `ValueError` for invalid input.
- Routers translate service validation errors to `HTTPException(status_code=400, detail=message)`.
- Return `HTTPException(status_code=404)` for missing resources.

## Testing conventions
- Use `sut` as the fixture name for the system under test.
- Use `test_method_condition_expected_behavior` naming.
- Mock the repository with `unittest.mock.AsyncMock`.
- Verify repository side effects with `assert_awaited_once`/`assert_awaited_once_with`.

## Teaching safeguards
- Do not proactively implement the missing DELETE endpoint in `app/routers/tasks.py` unless asked — `TaskService.delete()` and the repository already support it; only the route is missing.
- Do not proactively fill in the TODO tests at the bottom of `tests/test_task_service.py` unless asked.
