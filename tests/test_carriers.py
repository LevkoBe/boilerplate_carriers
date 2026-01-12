import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_carrier(client: AsyncClient):
    response = await client.post(
        "/api/v1/carriers/",
        json={
            "carrier_code": "fedex",
            "friendly_name": "FedEx",
            "account_number": "FDX123456",
            "requires_funded_amount": False,
            "balance": 0.0
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["carrier_code"] == "fedex"
    assert "id" in data


@pytest.mark.asyncio
async def test_get_carriers(client: AsyncClient):
    # Create first
    await client.post(
        "/api/v1/carriers/",
        json={
            "carrier_code": "ups",
            "account_number": "UPS789",
            "balance": 100.0
        }
    )

    response = await client.get("/api/v1/carriers/")
    assert response.status_code == 200
    assert len(response.json()) >= 1


@pytest.mark.asyncio
async def test_update_carrier(client: AsyncClient):
    create_response = await client.post(
        "/api/v1/carriers/",
        json={"carrier_code": "dhl", "account_number": "DHL999"}
    )
    carrier_id = create_response.json()["id"]

    update_response = await client.put(
        f"/api/v1/carriers/{carrier_id}",
        json={"balance": 500.0}
    )
    assert update_response.status_code == 200
    assert update_response.json()["balance"] == 500.0


@pytest.mark.asyncio
async def test_delete_carrier(client: AsyncClient):
    create_response = await client.post(
        "/api/v1/carriers/",
        json={"carrier_code": "usps", "account_number": "USPS111"}
    )
    carrier_id = create_response.json()["id"]

    delete_response = await client.delete(f"/api/v1/carriers/{carrier_id}")
    assert delete_response.status_code == 204

    get_response = await client.get(f"/api/v1/carriers/{carrier_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_duplicate_account_fails(client: AsyncClient):
    await client.post(
        "/api/v1/carriers/",
        json={"carrier_code": "test", "account_number": "ACC123"}
    )

    response = await client.post(
        "/api/v1/carriers/",
        json={"carrier_code": "test2", "account_number": "ACC123"}
    )
    assert response.status_code == 400
