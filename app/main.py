from fastapi import FastAPI, HTTPException, Depends
from app.schemas import ResponseTask,CreateTask
from app.database import engine, Base, SessionLocal, Session,get_db
from app.models import Task
from typing import List


app=FastAPI()

Base.metadata.create_all(engine)


@app.get("/")
def root():
    return {"Message":"Welcom to Task Manager"}

@app.post("/task",response_model=ResponseTask)
def create_task(task:CreateTask, db:Session = Depends(get_db)):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.get("/tasks/{task_id}",response_model=ResponseTask)
def get_task(task_id:int, db:Session = Depends(get_db)):
    task = (db.query(Task).filter(Task.id==task_id).first())
    if not task:
        raise HTTPException (status_code=404, detail="Task Not Found")
    return task

@app.get("/tasks", response_model=List[ResponseTask])
def get_all_task(db:Session = Depends(get_db)):
    task = (db.query(Task).all())
    for row in task:
        return task
    
