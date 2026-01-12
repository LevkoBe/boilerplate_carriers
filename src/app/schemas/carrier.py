from pydantic import BaseModel, ConfigDict
from typing import Optional


class CarrierBase(BaseModel):
    carrier_code: str
    friendly_name: Optional[str] = None
    account_number: str
    requires_funded_amount: bool = False
    balance: float = 0.0


class CarrierCreate(CarrierBase):
    pass


class CarrierUpdate(CarrierBase):
    pass


class Carrier(CarrierBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
