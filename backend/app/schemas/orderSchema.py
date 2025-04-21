from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.menu_itemSchema import MenuItemResponse
from app.enum.OrderStatus import OrderStatus

class OrderBase(BaseModel):
    total_amount: float
    status: OrderStatus

class OrderCreate(OrderBase):
    menu_item_ids: List[int] # Keeping IDs for simplicity in request payload

class OrderResponse(BaseModel):
    id: int
    total_amount: float
    status: OrderStatus
    timestamp: datetime
    menu_items: List[MenuItemResponse] # Return full menu item details

    class Config:
        from_attributes = True