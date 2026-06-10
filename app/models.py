from sqlalchemy import Column,String,Integer,Date
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    due_date = Column(Date)
    status=Column(String,default="Pending")

