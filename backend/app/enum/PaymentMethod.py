import enum

class PaymentMethod(enum.Enum):
    cash = "cash"
    credit_card = "credit_card"
    mobile_payment = "mobile_payment"
    