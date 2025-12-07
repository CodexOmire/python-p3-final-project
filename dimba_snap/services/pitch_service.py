from ..db import SessionLocal
from ..models.pitch import Pitch

def create_pitch(name, location, rate):
    with SessionLocal() as session:
        pitch = Pitch(name=name, location=location, hourly_rate=rate)
        session.add(pitch)
        session.commit()
        session.refresh(pitch)
        return pitch

def list_pitches():
    with SessionLocal() as session:
        return session.query(Pitch).all()
