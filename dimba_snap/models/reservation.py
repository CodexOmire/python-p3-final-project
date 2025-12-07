from sqlalchemy import Column, Integer, Date, Time, ForeignKey, String
from sqlalchemy.orm import relationship
from ..db import Base

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    pitch_id = Column(Integer, ForeignKey("pitches.id"))
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    payment_status = Column(String, default="pending")

    team = relationship("Team", backref="reservations")
    pitch = relationship("Pitch", backref="reservations")
