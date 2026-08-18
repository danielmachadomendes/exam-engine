from datetime import datetime
import uuid

from sqlalchemy import DateTime, ForeignKey, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class AttemptAnswer(Base):
    __tablename__ = "attempt_answers"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    attempt_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("attempts.id"),
        nullable=False,
        index=True,
    )

    question_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("questions.id"),
        nullable=False,
        index=True,
    )

    answer_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("answers.id"),
        nullable=False,
        index=True,
    )

    answered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    attempt = relationship(
        "Attempt",
        back_populates="answers",
    )

    question = relationship(
        "Question",
    )

    answer = relationship(
        "Answer",
    )