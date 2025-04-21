from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base 

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    contact_number = Column(String(20), nullable=False)
    party_size = Column(Integer, nullable=False)
    reservation_time = Column(DateTime, nullable=False, default=datetime.utcnow)

