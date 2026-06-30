"""Application entry point.

Equivalent of TaskManagement/Program.cs. Run with:

    uvicorn app.main:app --reload

Interactive docs (Swagger UI equivalent) at http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI

from app.routers import tasks

app = FastAPI(title="Task Management API")
app.include_router(tasks.router)
