from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TopicCreate(BaseModel):
    name: str
    description: str | None = None


class TopicUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class TopicResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )