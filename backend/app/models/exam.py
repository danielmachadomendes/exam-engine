from datetime import datetime
import uuid

from sqlalchemy import Boolean, DateTime, Integer, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    time_limit_minutes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    question_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    passing_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    exam_questions = relationship(
        "ExamQuestion",
        back_populates="exam",
        cascade="all, delete-orphan",
    )

    attempts = relationship(
        "Attempt",
        back_populates="exam",
    )