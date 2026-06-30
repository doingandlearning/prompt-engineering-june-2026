"""In-memory task repository.

Equivalent of TaskManagement/Repositories/InMemoryTaskRepository.cs. Keeps
state in a dict so the project runs with no database — a real project would
swap this for a SQLAlchemy-backed repository implementing the same
TaskRepository contract.
"""
from __future__ import annotations

from app.models.task import Priority, TaskItem
from app.repositories.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self._tasks: dict[int, TaskItem] = {}
        self._next_id = 1

    async def get_by_id(self, task_id: int) -> TaskItem | None:
        return self._tasks.get(task_id)

    async def get_by_owner(
        self, owner_id: int, priority: Priority | None = None
    ) -> list[TaskItem]:
        tasks = [t for t in self._tasks.values() if t.owner_id == owner_id]
        if priority is not None:
            tasks = [t for t in tasks if t.priority == priority]
        return sorted(tasks, key=lambda t: t.created_at, reverse=True)

    async def save(self, task: TaskItem) -> TaskItem:
        task.id = self._next_id
        self._next_id += 1
        self._tasks[task.id] = task
        return task

    async def update(self, task: TaskItem) -> TaskItem | None:
        if task.id not in self._tasks:
            return None
        self._tasks[task.id] = task
        return task

    async def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None
