from fastapi import FastAPI

from app.database import Base, engine
from app.routes.base import api_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management & Local AI API",
    description=(
        "FastAPI + SQLite CRUD application with an optional local Ollama AI "
        "extension for natural-language questions over student records."
    ),
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Student Management API. Visit /docs for Swagger UI."
    }
