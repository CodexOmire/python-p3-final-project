from sqlalchemy import Column, Integer, String
from dimba_snap.db import Base

class Pitch(Base):
    __tablename__ = "pitches"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    def __repr__(self):
        return f"<Pitch id={self.id} name={self.name}>"
