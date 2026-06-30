"""Task domain model.

Equivalent of TaskManagement/Models/TaskItem.cs. This is a plain in-memory
model (no ORM) — the repository layer is what would be swapped for
SQLAlchemy in a real project.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Status(str, Enum):
    TODO = "Todo"
    IN_PROGRESS = "InProgress"
    DONE = "Done"


@dataclass
class TaskItem:
    id: int
    title: str
    owner_id: int
    description: str | None = None
    priority: Priority = Priority.MEDIUM
    status: Status = Status.TODO
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
