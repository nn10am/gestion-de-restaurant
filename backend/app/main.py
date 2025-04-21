from fastapi import FastAPI
from app.controllers.orderController import router as order_router
from app.database import Base, engine
from app.models import menuItemModel, orderModel, paymentModel, reservationModel, staffModel
from app.controllers.menuController import router as menu_router
#Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(tilte="Restaurant Management API")

# Include controllers
app.include_router(order_router)
app.include_router(menu_router)

@app.get("/")
def home():
    return {"message:" "Welcome to Restaurant Management API"}