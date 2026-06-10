from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import CreateTask, ResponseTask
from app.services.tasks_service import TasksService

# Initialize the router with a clean prefix and documentation tags
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("", response_model=ResponseTask, status_code=21)
def create_task(task_data: CreateTask, db: Session = Depends(get_db)):
    return TasksService.create_task(db, task_data)

@router.get("", response_model=List[ResponseTask])
def get_all_tasks(db: Session = Depends(get_db)):
    return TasksService.get_all_tasks(db)

@router.get("/{task_id}", response_model=ResponseTask)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    return TasksService.get_task_by_id(db, task_id)

@router.patch("/{task_id}", response_model=ResponseTask)
def mark_task_as_done(task_id: int, db: Session = Depends(get_db)):
    return TasksService.mark_task_as_done(db, task_id)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return TasksService.delete_task(db, task_id)