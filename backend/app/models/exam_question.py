import uuid

from sqlalchemy import ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ExamQuestion(Base):
    __tablename__ = "exam_questions"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    exam_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("exams.id"),
        nullable=False,
        index=True,
    )

    question_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("questions.id"),
        nullable=False,
        index=True,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    exam = relationship(
        "Exam",
        back_populates="exam_questions",
    )

    question = relationship(
        "Question",
    )