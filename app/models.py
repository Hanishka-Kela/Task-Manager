from sqlalchemy import Column,String,Integer,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    due_date = Column(Date)
    status=Column(String,default="Pending")
    owner_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    owner = relationship("User", back_populates="tasks")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    username = Column(String, unique=True,nullable=False)
    hashed_password = Column(String , nullable=False)
    is_active = Column(Boolean, default=True)
    tasks = relationship("Task",back_populates="owner")
