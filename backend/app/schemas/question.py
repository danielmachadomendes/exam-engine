from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class QuestionCreate(BaseModel):
    title: Optional[str]
    text: str
    type: str
    choices: Optional[dict] = None
    correct: Optional[dict] = None
    category_id: Optional[UUID] = None
    difficulty: Optional[str] = None
    tags: Optional[List[str]] = None

class QuestionRead(QuestionCreate):
    id: UUID

