from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class UserBase(BaseModel):
    name: str
    national_id: str
    job: str
    income: Decimal
    model_config = ConfigDict(from_attributes=True)

