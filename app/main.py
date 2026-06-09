from fastapi import FastAPI, HTTPException, Depends
from app.schemas import ResponseTask,CreateTask
from app.database import engine, Base, SessionLocal, Session,get_db
from app.models import Task


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