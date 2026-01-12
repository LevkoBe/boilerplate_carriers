from sqlalchemy import Column, Integer, String, Boolean, Float
from src.app.db.base_class import Base


class Carrier(Base):
    id = Column(Integer, primary_key=True, index=True)
    carrier_code = Column(String, index=True, nullable=False)
    friendly_name = Column(String, nullable=True)
    account_number = Column(String, unique=True, index=True)
    requires_funded_amount = Column(Boolean, default=False)
    balance = Column(Float, default=0.0)
