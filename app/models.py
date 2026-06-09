from sqlalchemy import Column,String,Integer,Boolean,Date
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    due_date = Column(Date)
    done=Column(Boolean, default=False)

