from pydantic import BaseModel
from datetime import datetime
from typing import List
from schemas.menu_item import MenuItemResponse
from app.enum.OrderStatus import OrderStatus

class OrderBase(BaseModel):
    menu_items: List[int] # List of MenuItems IDs

class OrderCreate(OrderBase):
    pass

class OrderResponse(BaseModel):
    id: int
    total_amount: float
    status: OrderStatus
    timestamp: datetime
    menu_items: List[MenuItemResponse]

    class Config:
        from_attributes = True