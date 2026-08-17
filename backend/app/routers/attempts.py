from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.models.attempt import ExamAttempt
from app.schemas.attempt import AttemptCreate, AttemptRead
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=AttemptRead, status_code=201)
def start_attempt(payload: AttemptCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    attempt = ExamAttempt(
        exam_id=payload.exam_id,
        user_id=user.id,
    )
    db.add(attempt)
    db.commit()
    db.refresh(attempt)
    return attempt

@router.get("/{attempt_id}", response_model=AttemptRead)
def get_attempt(attempt_id: UUID, db: Session = Depends(get_db), user=Depends(get_current_user)):
    attempt = db.get(ExamAttempt, attempt_id)
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")
    return attempt
