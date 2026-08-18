from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.core.enums import QuestionDifficulty, QuestionType


class AnswerCreate(BaseModel):
    answer_text: str = Field(min_length=1)
    is_correct: bool = False
    display_order: int = Field(ge=0)


class AnswerResponse(BaseModel):
    id: UUID
    question_id: UUID
    answer_text: str
    is_correct: bool
    display_order: int

    model_config = ConfigDict(
        from_attributes=True
    )


class QuestionCreate(BaseModel):
    topic_id: UUID
    question_text: str = Field(min_length=1)
    question_type: QuestionType
    difficulty: QuestionDifficulty = QuestionDifficulty.MEDIUM
    explanation: str | None = None
    reference: str | None = None
    answers: list[AnswerCreate] = Field(min_length=2)


class QuestionUpdate(BaseModel):
    topic_id: UUID | None = None
    question_text: str | None = None
    question_type: QuestionType | None = None
    difficulty: QuestionDifficulty | None = None
    explanation: str | None = None
    reference: str | None = None
    is_active: bool | None = None
    answers: list[AnswerCreate] | None = None


class QuestionResponse(BaseModel):
    id: UUID
    topic_id: UUID
    question_text: str
    question_type: QuestionType
    difficulty: QuestionDifficulty
    explanation: str | None
    reference: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    answers: list[AnswerResponse]

    model_config = ConfigDict(
        from_attributes=True
    )