from sqlalchemy.exc import IntegrityError
from ..db import SessionLocal
from ..models.user import User

def create_user(name, email, role):
    with SessionLocal() as session:
        user = User(name=name, email=email.lower(), role=role)
        session.add(user)
        try:
            session.commit()
            session.refresh(user)
            return user
        except IntegrityError:
            session.rollback()
            raise ValueError("Email already exists.")

def list_users():
    with SessionLocal() as session:
        return session.query(User).all()
