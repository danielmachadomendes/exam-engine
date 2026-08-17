import os

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from app.routers import auth, questions, exams, attempts


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


app = FastAPI(
    title="ServiceNow Exam Engine API",
    version="0.1.0",
)


app.include_router(auth.router)
app.include_router(questions.router, prefix="/questions", tags=["questions"])
app.include_router(exams.router, prefix="/exams", tags=["exams"])
app.include_router(attempts.router, prefix="/attempts", tags=["attempts"])


@app.get("/")
def root():
    return {
        "message": "ServiceNow Exam Engine API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/health/db")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected"
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )
