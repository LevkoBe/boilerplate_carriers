from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.app.models.carrier import Carrier
from src.app.schemas.carrier import CarrierCreate, CarrierUpdate


class CRUDCarrier:
    async def get(self, db: AsyncSession, id: int):
        result = await db.execute(select(Carrier).filter(Carrier.id == id))
        return result.scalars().first()

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100):
        result = await db.execute(select(Carrier).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_account(self, db: AsyncSession, account_number: str):
        result = await db.execute(
            select(Carrier).filter(Carrier.account_number == account_number)
        )
        return result.scalars().first()

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

    async def update(self, db: AsyncSession, id: int, obj_in: CarrierUpdate):
        result = await db.execute(select(Carrier).filter(Carrier.id == id))
        db_obj = result.scalars().first()
        if not db_obj:
            return None

        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int):
        result = await db.execute(select(Carrier).filter(Carrier.id == id))
        db_obj = result.scalars().first()
        if not db_obj:
            return None

        await db.delete(db_obj)
        await db.commit()
        return db_obj


carrier = CRUDCarrier()
