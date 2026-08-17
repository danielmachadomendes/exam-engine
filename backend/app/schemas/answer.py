from pydantic import BaseModel
from typing import Optional, Dict, Any
from uuid import UUID

class AnswerCreate(BaseModel):
    attempt_id: UUID
    question_id: UUID
    answer: Optional[Dict[str, Any]] = None

class AnswerRead(AnswerCreate):
    id: UUID
    correct: Optional[bool]
    score_given: Optional[float]
