from .base import Base
from decimal import Decimal
from sqlalchemy import Column, Integer, String, Float, Decimal as DecimalColumn

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    national_id = Column(String, index=True)
    job = Column(String, index=True)
    income = Column(DecimalColumn, index=True)