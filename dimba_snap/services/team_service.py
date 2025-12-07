from ..db import SessionLocal
from ..models.team import Team
from ..models.user import User

def create_team(name, user_id):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if not user:
            raise ValueError("User not found.")
        team = Team(name=name, user_id=user_id)
        session.add(team)
        session.commit()
        session.refresh(team)
        return team

def list_teams():
    with SessionLocal() as session:
        return session.query(Team).all()
