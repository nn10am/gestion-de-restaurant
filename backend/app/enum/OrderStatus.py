import enum

# OrderStatus Enum
class OrderStatus(enum.Enum):
    pending = "pending"
    preparing = "preparing"
    ready = "ready"
    completed = "completed"
    cancelled = "cancelled"