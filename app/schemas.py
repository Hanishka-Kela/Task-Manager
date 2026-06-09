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
    due_date:str
    
class ResponseTask(BaseModel):
    id: int
    title:str
    priority:Priority
    due_date:date
    done:bool

    class Config:
        from_attributes = True