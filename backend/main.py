from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.todos import router as todos_router
from src.db import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(todos_router)
