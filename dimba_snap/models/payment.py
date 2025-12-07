from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey("reservations.id"))
    amount = Column(Float, nullable=False)
    method = Column(String, nullable=False)
    payment_date = Column(Date)

    reservation = relationship("Reservation", backref="payments")
