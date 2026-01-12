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


@router.post("/", response_model=schemas.Carrier, status_code=201)
async def create_carrier(
    carrier_in: schemas.CarrierCreate,
    db: AsyncSession = Depends(get_db)
):
    existing = await crud.carrier.get_by_account(db, carrier_in.account_number)
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Carrier with account {carrier_in.account_number} already exists"
        )
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


@router.put("/{id}", response_model=schemas.Carrier)
async def update_carrier(
    id: int,
    carrier_in: schemas.CarrierUpdate,
    db: AsyncSession = Depends(get_db)
):
    carrier = await crud.carrier.update(db, id=id, obj_in=carrier_in)
    if not carrier:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return carrier


@router.delete("/{id}", status_code=204)
async def delete_carrier(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    carrier = await crud.carrier.delete(db, id=id)
    if not carrier:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return None
