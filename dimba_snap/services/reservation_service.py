from ..db import SessionLocal
from ..models.reservation import Reservation
from ..models.team import Team
from ..models.pitch import Pitch

def create_reservation(team_id, pitch_id, date, start, end):
    if start >= end:
        raise ValueError("Start time must be before end time.")
    with SessionLocal() as session:
        team = session.get(Team, team_id)
        pitch = session.get(Pitch, pitch_id)
        if not team or not pitch:
            raise ValueError("Team or pitch not found.")

        reservation = Reservation(
            team_id=team_id,
            pitch_id=pitch_id,
            date=date,
            start_time=start,
            end_time=end
        )
        session.add(reservation)
        session.commit()
        session.refresh(reservation)
        return reservation

def list_reservations():
    with SessionLocal() as session:
        return session.query(Reservation).all()
