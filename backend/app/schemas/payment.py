from pydantic import BaseModel
from app.enum.PaymentMethod import PaymentMethod
from app.enum.PaymentStatus import PaymentStatus

class PaymentBase(BaseModel):
    amount: float
    payment_method: PaymentMethod
    payment_status: PaymentStatus
    order_id: int

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int
    
    class Config:
        from_attributes = True