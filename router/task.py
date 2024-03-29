from fastapi import APIRouter
from models.task import Task
from libs.db import session
from pydantic import BaseModel

router = APIRouter()

class TaskInput(BaseModel):
    name: str
    description: str | None = None

@router.get("/tasks")
async def index():
    tasks = session.query(Task).all()

    return {
        "success": True,
        "data": tasks
    }

@router.get("/tasks/{id}")
async def index(id: int):
    task = session.query(Task).filter(Task.id==id).first()

    return {
        "success": True,
        "data": task
    }

@router.post("/tasks")
async def store(body: TaskInput):
    task = Task(name=body.name, description=body.description)
    session.add(task)
    session.commit()

    return {
        "success": True,
        "message": "Task added"
    }

@router.put("/tasks/{id}")
async def update(id: int, body: TaskInput):
    task = session.query(Task).filter(Task.id==id).first()
    task.name = body.name
    task.description = body.description
    session.add(task)
    session.commit()

    return {
        "success": True,
        "message": "Task updated"
    }

@router.delete("/tasks/{id}")
async def destroy(id: int):
    task = session.query(Task).filter(Task.id==id).first()
    session.delete(task)
    session.commit()

    return {
        "success": True,
        "message": "Task deleted"
    }


