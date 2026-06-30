"""Repository contract for task persistence.

Equivalent of TaskManagement/Repositories/ITaskRepository.cs.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from app.models.task import Priority, TaskItem


class TaskRepository(ABC):
    @abstractmethod
    async def get_by_id(self, task_id: int) -> TaskItem | None: ...

    @abstractmethod
    async def get_by_owner(
        self, owner_id: int, priority: Priority | None = None
    ) -> list[TaskItem]: ...

    @abstractmethod
    async def save(self, task: TaskItem) -> TaskItem: ...

    @abstractmethod
    async def update(self, task: TaskItem) -> TaskItem | None: ...

    @abstractmethod
    async def delete(self, task_id: int) -> bool: ...
