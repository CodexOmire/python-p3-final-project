from datetime import date
from ..db import SessionLocal
from ..models.payment import Payment
from ..models.reservation import Reservation

def add_payment(reservation_id, amount, method):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    with SessionLocal() as session:
        res = session.get(Reservation, reservation_id)
        if not res:
            raise ValueError("Reservation not found.")

        payment = Payment(
            reservation_id=reservation_id,
            amount=amount,
            method=method,
            payment_date=date.today()
        )
        res.payment_status = "completed"
        session.add(payment)
        session.commit()
        session.refresh(payment)
        return payment

def list_payments():
    with SessionLocal() as session:
        return session.query(Payment).all()
