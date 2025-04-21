from sqlalchemy import Column, Integer, Float, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base 
from app.enum.OrderStatus import OrderStatus
from app.models.menuItemModel import order_menu_items




class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    timestamp = Column(DateTime, default = datetime.utcnow)

    # Relationship with MenuItem
    menu_items = relationship("MenuItem", secondary=order_menu_items, back_populates="orders")