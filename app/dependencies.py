"""Shared FastAPI dependencies.

The repository is a process-wide singleton (equivalent of the C# project's
`AddSingleton<ITaskRepository, InMemoryTaskRepository>()`); the service is
constructed per-request from it (equivalent of `AddScoped<ITaskService,
TaskService>()`).
"""
from __future__ import annotations

from functools import lru_cache

from app.repositories.in_memory_task_repository import InMemoryTaskRepository
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


@lru_cache
def get_task_repository() -> TaskRepository:
    return InMemoryTaskRepository()


def get_task_service() -> TaskService:
    return TaskService(get_task_repository())
