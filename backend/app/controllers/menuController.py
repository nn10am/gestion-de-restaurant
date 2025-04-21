from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.menuItemModel import MenuItem
from app.schemas.menu_itemSchema import MenuItemCreate, MenuItemResponse

router = APIRouter(prefix="/menu", tags=["Menu"])

@router.get("/", response_model=List[MenuItemResponse])
def get_all_menu(db: Session = Depends(get_db)):
    """Fetch all items in the menu."""
    return db.query(MenuItem).all()

@router.post("/", response_model=MenuItemResponse)
async def create_menu_item(menu_item_data: MenuItemCreate, db: Session = Depends(get_db)):
    """Add new item to the menu."""
    menu_item = MenuItem(**menu_item_data.dict())
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return menu_item