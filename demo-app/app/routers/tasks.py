"""Task API router.

Equivalent of TaskManagement/Controllers/TasksController.cs.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies import get_task_service
from app.schemas.task import CreateTaskRequest, TaskResponse, UpdateTaskRequest
from app.services.task_service import TaskService

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskResponse])
async def get_all(
    owner_id: int = Query(..., alias="ownerId"),
    priority: str | None = Query(None),
    service: TaskService = Depends(get_task_service),
) -> list[TaskResponse]:
    """Get all tasks for a user, optionally filtered by priority."""
    try:
        return await service.get_by_owner(owner_id, priority)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/{task_id}", response_model=TaskResponse)
async def get_by_id(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> TaskResponse:
    """Get a single task by ID."""
    task = await service.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("", response_model=TaskResponse, status_code=201)
async def create(
    request: CreateTaskRequest, service: TaskService = Depends(get_task_service)
) -> TaskResponse:
    """Create a new task."""
    try:
        return await service.create(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.patch("/{task_id}", response_model=TaskResponse)
async def update(
    task_id: int,
    request: UpdateTaskRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    """Update an existing task."""
    try:
        updated = await service.update(task_id, request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


# NOTE FOR DEMO: DELETE endpoint is missing.
# Good PRD-driven demo: give delegates a user story and ask them to add it.
# TaskService.delete() and the repository already support it end-to-end —
# only the route is missing.
