from sqlalchemy.orm import Session
from app.models import Task

class TasksRepository:
    @staticmethod
    def get_all(db: Session, user_id: int):
        return db.query(Task).filter(Task.owner_id == user_id).all()

    @staticmethod
    def get_by_id(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def create(db: Session, task_data: dict):
        new_task = Task(**task_data)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    @staticmethod
    def delete(db: Session, task: Task):
        db.delete(task)
        db.commit()

    @staticmethod
    def save_changes(db: Session, task: Task):
        db.commit()
        db.refresh(task)
        return task