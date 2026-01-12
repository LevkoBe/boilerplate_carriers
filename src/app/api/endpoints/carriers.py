from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.app import crud, schemas
from src.app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Carrier])
async def read_carriers(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    carriers = await crud.carrier.get_multi(db, skip=skip, limit=limit)
    return carriers


@router.post("/", response_model=schemas.Carrier)
async def create_carrier(
    carrier_in: schemas.CarrierCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.carrier.create(db=db, obj_in=carrier_in)


@router.get("/{id}", response_model=schemas.Carrier)
async def read_carrier(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    carrier = await crud.carrier.get(db, id=id)
    if not carrier:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return carrier
