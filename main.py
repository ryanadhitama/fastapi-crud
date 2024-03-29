from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.task import router as task_router

app = FastAPI()

app.include_router(task_router)

@app.get("/")
def root():
    return {"ping": "pong!"}
