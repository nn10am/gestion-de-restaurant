from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.orderModel import Order
from app.schemas.orderSchema import OrderCreate, OrderResponse
from app.services.restaurant import Restaurant
from app.models.menuItemModel import MenuItem

router = APIRouter(prefix="/orders", tags=["Orders"])
restaurant = Restaurant()

@router.post("/", response_model=OrderResponse)
async def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    # Fetch menu items based on provided menu_item_ids
    # menu_items = db.query(MenuItem).filter(MenuItem.id.in_(order_data.menu_item_ids)).all()
    
    order = Order(
        total_amount = order_data.total_amount,
        status = order_data.status
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    restaurant.place_order(order) # Notify kitchen
    return order

@router.get("/", response_model=list[OrderResponse])
async def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()