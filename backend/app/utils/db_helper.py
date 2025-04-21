from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import Depends

# Utility function to get the DB session
def get_db_session(db: Session = Depends(get_db)):
    return db
    