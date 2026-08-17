import getpass

from sqlalchemy import select

from app.db.session import SessionLocal
from app.core.security import get_password_hash
from app.models.user import User


def main():
    email = input("Admin email: ").strip().lower()
    full_name = input("Admin full name: ").strip()
    password = getpass.getpass("Admin password: ")

    if not email or not full_name or not password:
        raise ValueError("All fields are required.")

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
            role="ADMIN",
            is_active=True,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        print(f"Admin created successfully: {user.email}")

    finally:
        db.close()


if __name__ == "__main__":
    main()