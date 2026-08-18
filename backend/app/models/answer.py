import uuid

from sqlalchemy import Boolean, ForeignKey, Integer, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Answer(Base):
    __tablename__ = "answers"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    question_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("questions.id"),
        nullable=False,
        index=True,
    )

    answer_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    is_correct: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    question = relationship(
        "Question",
        back_populates="answers",
    )