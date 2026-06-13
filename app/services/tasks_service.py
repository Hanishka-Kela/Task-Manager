from app import database
from sqlalchemy.orm import Session
from app.repositories.tasks_repository import TasksRepository
from app.schemas import CreateTask
from fastapi import HTTPException

class TasksService:
    @staticmethod
    def get_all_tasks(db: Session, user_id: int):
        return TasksRepository.get_all(db, user_id)

    @staticmethod
    def get_task_by_id(db: Session, task_id: int, user_id: int):
        task = TasksRepository.get_by_id(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task Not Found")
        if task.owner_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to access this task")
        return task

    @staticmethod
    def create_task(db: Session, task_data: CreateTask, user_id: int):
        task_dict = task_data.model_dump()
        task_dict["owner_id"] = user_id
        return TasksRepository.create(db, task_dict)

    @staticmethod
    def update_task_status(db: Session, task_id: int, user_id: int, new_status: str):
        task = TasksRepository.get_by_id(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        if task.owner_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this task")
        task.status = new_status
        return TasksRepository.save_changes(db, task)

    @staticmethod
    def delete_task(db: Session, task_id: int, user_id: int):
        task = TasksRepository.get_by_id(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        if task.owner_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this task")
        TasksRepository.delete(db, task)
        return {"Message": "Task Deleted"}