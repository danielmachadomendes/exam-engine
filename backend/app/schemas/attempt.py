from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from uuid import UUID

class AttemptCreate(BaseModel):
    exam_id: UUID

class AttemptRead(BaseModel):
    id: UUID
    exam_id: UUID
    user_id: UUID
    status: str
    score: Optional[float]
