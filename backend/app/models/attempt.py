from datetime import datetime
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import AttemptStatus
from app.db.base import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    exam_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("exams.id"),
        nullable=False,
        index=True,
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default="now()",
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    passed: Mapped[bool | None] = mapped_column(
        nullable=True,
    )

    status: Mapped[AttemptStatus] = mapped_column(
        Enum(AttemptStatus),
        nullable=False,
        default=AttemptStatus.IN_PROGRESS,
        server_default=AttemptStatus.IN_PROGRESS.value,
    )

    user = relationship(
        "User",
    )

    exam = relationship(
        "Exam",
        back_populates="attempts",
    )

    answers = relationship(
        "AttemptAnswer",
        back_populates="attempt",
        cascade="all, delete-orphan",
    )