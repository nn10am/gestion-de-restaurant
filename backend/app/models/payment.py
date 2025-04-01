from sqlalchemy import Column, Integer, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base 
from app.enum.PaymentMethod import PaymentMethod
from app.enum.PaymentStatus import PaymentStatus

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.pending)

    # Relationship with Order
    order_id = Column(Integer, ForeignKey("oreers.id"), nullable=False)
    order = relationship("Order")