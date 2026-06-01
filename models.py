from base import Base
from decimal import Decimal
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean
from datetime import datetime

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now())
    is_active = Column(Boolean, default=True)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    national_id = Column(String, index=True)
    job = Column(String, index=True)
    income = Column(Numeric(precision=18, scale=2), default=0)