"""Task service — validation and business logic.

Equivalent of TaskManagement/Services/TaskService.cs.
"""
from __future__ import annotations

from datetime import datetime, timezone

from app.models.task import Priority, Status, TaskItem
from app.repositories.task_repository import TaskRepository
from app.schemas.task import CreateTaskRequest, TaskResponse, UpdateTaskRequest

MAX_TITLE_LENGTH = 100


def _parse_priority(value: str) -> Priority:
    try:
        return Priority(value)
    except ValueError as exc:
        raise ValueError(f"Invalid priority: {value}") from exc


def _parse_status(value: str) -> Status:
    try:
        return Status(value)
    except ValueError as exc:
        raise ValueError(f"Invalid status: {value}") from exc


def _to_response(task: TaskItem) -> TaskResponse:
    return TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        priority=task.priority.value,
        status=task.status.value,
        created_at=task.created_at,
        completed_at=task.completed_at,
        owner_id=task.owner_id,
    )


class TaskService:
    """Coordinates task validation and persistence via a TaskRepository."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    async def create(self, request: CreateTaskRequest) -> TaskResponse:
        if not request.title or not request.title.strip():
            raise ValueError("Title is required")
        if len(request.title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title cannot exceed {MAX_TITLE_LENGTH} characters")

        priority = _parse_priority(request.priority)

        task = TaskItem(
            id=0,
            title=request.title,
            description=request.description,
            priority=priority,
            owner_id=request.owner_id,
        )
        saved = await self._repository.save(task)
        return _to_response(saved)

    async def get_by_owner(
        self, owner_id: int, priority: str | None = None
    ) -> list[TaskResponse]:
        priority_filter = _parse_priority(priority) if priority is not None else None
        tasks = await self._repository.get_by_owner(owner_id, priority_filter)
        return [_to_response(t) for t in tasks]

    async def get_by_id(self, task_id: int) -> TaskResponse | None:
        task = await self._repository.get_by_id(task_id)
        return _to_response(task) if task is not None else None

    async def update(
        self, task_id: int, request: UpdateTaskRequest
    ) -> TaskResponse | None:
        existing = await self._repository.get_by_id(task_id)
        if existing is None:
            return None

        if request.title is not None:
            if not request.title.strip():
                raise ValueError("Title cannot be empty")
            existing.title = request.title

        if request.description is not None:
            existing.description = request.description

        if request.priority is not None:
            existing.priority = _parse_priority(request.priority)

        if request.status is not None:
            new_status = _parse_status(request.status)
            previous_status = existing.status
            existing.status = new_status

            if previous_status != Status.DONE and new_status == Status.DONE:
                existing.completed_at = existing.completed_at or datetime.now(timezone.utc)
            elif previous_status == Status.DONE and new_status != Status.DONE:
                existing.completed_at = None

        updated = await self._repository.update(existing)
        return _to_response(updated) if updated is not None else None

    async def delete(self, task_id: int) -> bool:
        # NOTE FOR DEMO: implemented here and in the repository, but there is
        # no DELETE route wired up in app/routers/tasks.py. Good PRD-driven
        # demo: give delegates a user story ("As a user I want to delete a
        # task") and ask them to add the missing endpoint.
        return await self._repository.delete(task_id)
