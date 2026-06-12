from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tasks_router,auth_router

app = FastAPI(
    title="Task Manager API",
    description="A scalable, multi-layered Task Management API",
    version="1.0.0"
)

# Automatically create database tables on application startup
Base.metadata.create_all(engine)

@app.get("/")
def root():
    return {"Message": "Welcome to Task Manager"}

app.include_router(tasks_router.router)
app.include_router(auth_router.router_user)