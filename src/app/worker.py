import asyncio
from arq.connections import RedisSettings
from src.app.core.config import settings


async def process_carrier_balance_update(ctx, carrier_id: int, new_balance: float):
    await asyncio.sleep(2)  # Simulate work
    print(f"Processed balance update for carrier {carrier_id}: ${new_balance}")
    return {"carrier_id": carrier_id, "balance": new_balance, "status": "processed"}


class WorkerSettings:
    functions = [process_carrier_balance_update]
    redis_settings = RedisSettings(host='localhost', port=6379)