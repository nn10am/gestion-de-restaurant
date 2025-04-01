from sqlalchemy import Column, Integer, String
from app.database import Base 

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    contact_number = Column(String(20), nullable=False)

    