from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.app.models.carrier import Carrier
from src.app.schemas.carrier import CarrierCreate


class CRUDCarrier:
    async def get(self, db: AsyncSession, id: int):
        result = await db.execute(select(Carrier).filter(Carrier.id == id))
        return result.scalars().first()

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100):
        result = await db.execute(select(Carrier).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: CarrierCreate):
        db_obj = Carrier(
            carrier_code=obj_in.carrier_code,
            friendly_name=obj_in.friendly_name,
            account_number=obj_in.account_number,
            requires_funded_amount=obj_in.requires_funded_amount,
            balance=obj_in.balance
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


carrier = CRUDCarrier()
