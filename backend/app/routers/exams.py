from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.models.exam import Exam, ExamQuestion
from app.schemas.exam import ExamCreate, ExamRead, ExamQuestionAssign
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=ExamRead, status_code=201)
def create_exam(payload: ExamCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    exam = Exam(
        title=payload.title,
        description=payload.description,
        config=payload.config,
        created_by=user.id,
    )
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam

@router.post("/{exam_id}/questions", status_code=201)
def add_question_to_exam(exam_id: UUID, payload: ExamQuestionAssign, db: Session = Depends(get_db), user=Depends(get_current_user)):
    eq = ExamQuestion(exam_id=exam_id, question_id=payload.question_id, weight=payload.weight, order=payload.order)
    db.add(eq)
    db.commit()
    db.refresh(eq)
    return {"id": eq.id}

@router.get("/", response_model=list[ExamRead])
def list_exams(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(Exam).offset(skip).limit(limit).all()
