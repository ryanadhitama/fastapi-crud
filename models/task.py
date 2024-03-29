from sqlalchemy import Column, Integer, String, Text, DateTime, Table, func
from models.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=True, onupdate=func.now())
