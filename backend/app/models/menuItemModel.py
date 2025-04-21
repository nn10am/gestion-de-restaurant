from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, Table
from app.database import Base
from sqlalchemy.orm import relationship

# Association table for Many-to-Many relationship
order_menu_items = Table(
    "order_menu_items",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("menu_item_id", Integer, ForeignKey("menu_items.id"))
)

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    availability = Column(Boolean, default=True)
    
    # Define back_populates 
    orders = relationship("Order", secondary="order_menu_items", back_populates="menu_items")

