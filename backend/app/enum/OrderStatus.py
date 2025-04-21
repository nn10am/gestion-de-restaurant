import enum 

# OrderStatus Enum
class OrderStatus(enum.Enum):
    pending = "pending"
    preparing = "preparing"
    ready = "delete"
    completed = "completed"
    cancelled = "cancelled"