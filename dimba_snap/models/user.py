from sqlalchemy import Column, Integer, String
from ..db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)  # admin or team_manager

    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"
