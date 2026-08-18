from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies import require_roles
from app.models.topic import Topic
from app.schemas.topic import (
    TopicCreate,
    TopicResponse,
    TopicUpdate,
)
from app.core.roles import UserRole


router = APIRouter(
    prefix="/topics",
    tags=["topics"],
)


@router.post(
    "",
    response_model=TopicResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_topic(
    data: TopicCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.MANAGER,
        )
    ),
):
    existing_topic = db.scalar(
        select(Topic).where(Topic.name == data.name)
    )

    if existing_topic:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A topic with this name already exists.",
        )

    topic = Topic(
        name=data.name,
        description=data.description,
        is_active=True,
    )

    db.add(topic)
    db.commit()
    db.refresh(topic)

    return topic


@router.get(
    "",
    response_model=list[TopicResponse],
)
def list_topics(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.MANAGER,
            UserRole.LEARNER,
        )
    ),
):
    return db.scalars(
        select(Topic)
        .order_by(Topic.name)
    ).all()


@router.get(
    "/{topic_id}",
    response_model=TopicResponse,
)
def get_topic(
    topic_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.MANAGER,
            UserRole.LEARNER,
        )
    ),
):
    topic = db.get(Topic, topic_id)

    if topic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Topic not found.",
        )

    return topic


@router.put(
    "/{topic_id}",
    response_model=TopicResponse,
)
def update_topic(
    topic_id: UUID,
    data: TopicUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.MANAGER,
        )
    ),
):
    topic = db.get(Topic, topic_id)

    if topic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Topic not found.",
        )

    if data.name is not None:
        existing_topic = db.scalar(
            select(Topic).where(
                Topic.name == data.name,
                Topic.id != topic_id,
            )
        )

        if existing_topic:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A topic with this name already exists.",
            )

        topic.name = data.name

    if data.description is not None:
        topic.description = data.description

    if data.is_active is not None:
        topic.is_active = data.is_active

    db.commit()
    db.refresh(topic)

    return topic