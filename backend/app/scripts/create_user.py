import getpass

from sqlalchemy import select

from app.core.security import get_password_hash
from app.db.session import SessionLocal
from app.models.user import User


VALID_ROLES = {"ADMIN", "MANAGER", "LEARNER"}


def main():
    email = input("Email: ").strip().lower()
    full_name = input("Full name: ").strip()
    role = input("Role (ADMIN/MANAGER/LEARNER): ").strip().upper()
    password = getpass.getpass("Password: ")

    if not email or not full_name or not password:
        raise ValueError("All fields are required.")

    if role not in VALID_ROLES:
        raise ValueError(
            f"Invalid role. Choose one of: {', '.join(VALID_ROLES)}"
        )

    db = SessionLocal()

    try:
        existing_user = db.scalar(
            select(User).where(User.email == email)
        )

        if existing_user:
            raise ValueError(
                f"A user with email {email} already exists."
            )

        user = User(
            email=email,
            full_name=full_name,
            password_hash=get_password_hash(password),
            role=role,
            is_active=True,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        print(
            f"User created successfully: "
            f"{user.email} ({user.role})"
        )

    finally:
        db.close()


if __name__ == "__main__":
    main()