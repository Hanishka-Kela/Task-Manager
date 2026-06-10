from pydantic import BaseModel
from enum import Enum
from datetime import date

class Priority(str, Enum):
    low_priority = "low"
    medium_priority = "medium"
    high_priority = "high"

class CreateTask(BaseModel):
    title:str
    priority:Priority
    due_date:date

class Status(str, Enum):
    to_do ="Pending"
    in_progress="In-progress"
    done = "completed"
    
class ResponseTask(BaseModel):
    id: int
    title:str
    priority:Priority
    due_date:date
    status:str

    class Config:
        from_attributes = True