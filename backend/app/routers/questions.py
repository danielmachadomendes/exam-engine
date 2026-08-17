from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionRead
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=QuestionRead, status_code=201)
def create_question(payload: QuestionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    question = Question(
        title=payload.title,
        text=payload.text,
        type=payload.type,
        choices=payload.choices,
        correct=payload.correct,
        category_id=payload.category_id,
        difficulty=payload.difficulty,
        tags=payload.tags,
        created_by=user.id,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

@router.get("/", response_model=list[QuestionRead])
def list_questions(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(Question).offset(skip).limit(limit).all()
