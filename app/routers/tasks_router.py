from app.core.security import get_current_user
from app.models import User
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

@router.post("", response_model=ResponseTask, status_code=201)
def create_task(task_data: CreateTask, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return TasksService.create_task(db, task_data,current_user.id)

@router.get("", response_model=List[ResponseTask])
def get_all_tasks(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return TasksService.get_all_tasks(db,current_user.id)

@router.get("/{task_id}", response_model=ResponseTask)
def get_task_by_id(task_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return TasksService.get_task_by_id(db, task_id,current_user.id)

@router.patch("/{task_id}", response_model=ResponseTask)
def update_task_status(task_id: int, new_status: str, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return TasksService.update_task_status(db, task_id, current_user.id, new_status=new_status)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return TasksService.delete_task(db, task_id,current_user.id)