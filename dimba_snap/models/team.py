from sqlalchemy import Column, Integer, String
from dimba_snap.db import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    coach = Column(String)

    def __repr__(self):
        return f"<Team id={self.id} name={self.name}>"
