from sqlalchemy import Column, Integer, Float, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base 
from app.enum.OrderStatus import OrderStatus



# Association table for Many-to-Many relationship
order_menu_items = Table(
    "order_menu_items",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("menu_item_id", Integer, ForeignKey("menu_items.id"))
)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    timestamp = Column(DateTime, default = datetime.utcnow)

    # Relationship with MenuItem
    menu_items = relationship("MenuItem", secondary=order_menu_items, back_populates="orders")