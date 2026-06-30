## Feature: Update task priority

**Stack:** Python 3.11, FastAPI, SQLAlchemy 2.0. Constructor injection throughout.

**Endpoint:** PATCH /api/tasks/{id}/priority

**Request:** priority (string — low, medium, high)

**Behaviour:**
- Validate priority is one of the allowed values
- Check the task belongs to the requesting user (owner_id)
- Update and save
- Return 200 with updated task on success
- Return 404 if task not found
- Return 403 if task belongs to a different user
- Return 400 if priority value is invalid

**Acceptance criteria:**
- [ ] Invalid priority returns 400 with a descriptive error
- [ ] Task not found returns 404
- [ ] Task owned by another user returns 403, not 404
- [ ] Successful update returns 200 with the updated TaskResponse
