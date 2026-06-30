"""Tests for TaskService.

Equivalent of TaskManagement.Tests/TaskServiceTests.cs — pytest +
unittest.mock standing in for xUnit + Moq. The repository is mocked with
unittest.mock.AsyncMock since TaskRepository methods are async.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock

import pytest

from app.models.task import Priority, Status, TaskItem
from app.schemas.task import CreateTaskRequest, UpdateTaskRequest
from app.services.task_service import TaskService


@pytest.fixture
def mock_repository() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def sut(mock_repository: AsyncMock) -> TaskService:
    return TaskService(mock_repository)


# --- create -----------------------------------------------------------------


async def test_create_with_valid_request_returns_mapped_response(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    mock_repository.save.side_effect = lambda task: _assign_id(task, 1)

    request = CreateTaskRequest(title="Write tests", priority="High", owner_id=1)
    result = await sut.create(request)

    assert result.id == 1
    assert result.title == "Write tests"
    assert result.priority == "High"
    assert result.status == "Todo"
    assert result.completed_at is None
    mock_repository.save.assert_awaited_once()


async def test_create_with_empty_title_raises_value_error(sut: TaskService) -> None:
    request = CreateTaskRequest(title="", priority="Medium", owner_id=1)
    with pytest.raises(ValueError, match="Title is required"):
        await sut.create(request)


@pytest.mark.parametrize("title", ["", "   "])
async def test_create_with_whitespace_only_title_raises_value_error(
    sut: TaskService, title: str
) -> None:
    request = CreateTaskRequest(title=title, priority="Medium", owner_id=1)
    with pytest.raises(ValueError, match="Title is required"):
        await sut.create(request)


async def test_create_with_title_exceeding_max_length_raises_value_error(
    sut: TaskService,
) -> None:
    request = CreateTaskRequest(title="x" * 101, priority="Medium", owner_id=1)
    with pytest.raises(ValueError, match="cannot exceed"):
        await sut.create(request)


async def test_create_with_invalid_priority_raises_value_error(
    sut: TaskService,
) -> None:
    request = CreateTaskRequest(title="Write tests", priority="Urgent", owner_id=1)
    with pytest.raises(ValueError, match="Invalid priority"):
        await sut.create(request)


# --- update -------------------------------------------------------------


async def test_update_with_nonexistent_id_returns_none(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    mock_repository.get_by_id.return_value = None

    result = await sut.update(999, UpdateTaskRequest(title="New title"))

    assert result is None


async def test_update_when_status_set_to_done_sets_completed_at(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    existing = TaskItem(id=1, title="A task", owner_id=1)
    mock_repository.get_by_id.return_value = existing
    mock_repository.update.side_effect = lambda task: task

    result = await sut.update(1, UpdateTaskRequest(status="Done"))

    assert result is not None
    assert result.completed_at is not None


async def test_update_when_transitioning_to_done_and_completed_at_already_set_preserves_completed_at(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    already_completed = datetime.now(timezone.utc) - timedelta(days=1)
    existing = TaskItem(
        id=1,
        title="A task",
        owner_id=1,
        status=Status.IN_PROGRESS,
        completed_at=already_completed,
    )
    mock_repository.get_by_id.return_value = existing
    mock_repository.update.side_effect = lambda task: task

    result = await sut.update(1, UpdateTaskRequest(status="Done"))

    assert result is not None
    assert result.completed_at == already_completed


async def test_update_when_transitioning_from_done_to_non_done_clears_completed_at(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    existing = TaskItem(
        id=1,
        title="A task",
        owner_id=1,
        status=Status.DONE,
        completed_at=datetime.now(timezone.utc),
    )
    mock_repository.get_by_id.return_value = existing
    mock_repository.update.side_effect = lambda task: task

    result = await sut.update(1, UpdateTaskRequest(status="InProgress"))

    assert result is not None
    assert result.completed_at is None


async def test_update_with_non_null_title_updates_title_and_persists(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    existing = TaskItem(id=1, title="Old title", owner_id=1)
    mock_repository.get_by_id.return_value = existing
    mock_repository.update.side_effect = lambda task: task

    result = await sut.update(1, UpdateTaskRequest(title="New title"))

    assert result is not None
    assert result.title == "New title"
    mock_repository.update.assert_awaited_once()


@pytest.mark.parametrize("title", ["", "   "])
async def test_update_with_whitespace_title_raises_value_error(
    sut: TaskService, mock_repository: AsyncMock, title: str
) -> None:
    existing = TaskItem(id=1, title="Old title", owner_id=1)
    mock_repository.get_by_id.return_value = existing

    with pytest.raises(ValueError, match="Title cannot be empty"):
        await sut.update(1, UpdateTaskRequest(title=title))


async def test_update_with_valid_priority_updates_priority_and_persists(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    existing = TaskItem(id=1, title="A task", owner_id=1, priority=Priority.LOW)
    mock_repository.get_by_id.return_value = existing
    mock_repository.update.side_effect = lambda task: task

    result = await sut.update(1, UpdateTaskRequest(priority="High"))

    assert result is not None
    assert result.priority == "High"


async def test_update_with_invalid_priority_raises_value_error(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    existing = TaskItem(id=1, title="A task", owner_id=1)
    mock_repository.get_by_id.return_value = existing

    with pytest.raises(ValueError, match="Invalid priority"):
        await sut.update(1, UpdateTaskRequest(priority="Urgent"))


async def test_update_with_invalid_status_raises_value_error(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    existing = TaskItem(id=1, title="A task", owner_id=1)
    mock_repository.get_by_id.return_value = existing

    with pytest.raises(ValueError, match="Invalid status"):
        await sut.update(1, UpdateTaskRequest(status="Archived"))


# --- get_by_owner ------------------------------------------------------------


async def test_get_by_owner_with_priority_filter_only_returns_matching_tasks(
    sut: TaskService, mock_repository: AsyncMock
) -> None:
    matching = TaskItem(id=1, title="High priority", owner_id=1, priority=Priority.HIGH)
    mock_repository.get_by_owner.return_value = [matching]

    result = await sut.get_by_owner(1, priority="High")

    assert len(result) == 1
    assert result[0].priority == "High"
    mock_repository.get_by_owner.assert_awaited_once_with(1, Priority.HIGH)


def _assign_id(task: TaskItem, new_id: int) -> TaskItem:
    task.id = new_id
    return task


# DEMO GAPS — good for a TDD exercise
# TODO: Add tests for:
# - get_by_id() when the task does not exist (should return None)
# - delete() delegates to the repository and returns its result
# - create() when owner_id is missing/invalid (if that becomes a requirement)
