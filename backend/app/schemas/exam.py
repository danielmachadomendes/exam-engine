from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from uuid import UUID

class ExamCreate(BaseModel):
    title: str
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None

class ExamRead(ExamCreate):
    id: UUID

class ExamQuestionAssign(BaseModel):
    question_id: UUID
    weight: Optional[int] = 1
    order: Optional[int] = None
