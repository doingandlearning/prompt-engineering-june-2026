"""Pydantic v2 request/response schemas.

Equivalent of TaskManagement/DTOs/TaskDtos.cs.
"""
from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    title: str
    description: str | None = None
    priority: str
    owner_id: int


class UpdateTaskRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    status: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: str
    status: str
    created_at: datetime
    completed_at: datetime | None
    owner_id: int
