from datetime import datetime
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import QuestionDifficulty, QuestionType
from app.db.base import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    topic_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("topics.id"),
        nullable=False,
        index=True,
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    question_type: Mapped[QuestionType] = mapped_column(
        Enum(QuestionType),
        nullable=False,
    )

    difficulty: Mapped[QuestionDifficulty] = mapped_column(
        Enum(QuestionDifficulty),
        nullable=False,
        default=QuestionDifficulty.MEDIUM,
        server_default=QuestionDifficulty.MEDIUM.value,
    )

    explanation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    reference: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
        server_default="true",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    topic = relationship(
        "Topic",
        back_populates="questions",
    )

    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan",
    )