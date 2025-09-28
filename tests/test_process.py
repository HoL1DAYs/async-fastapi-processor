import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_process_endpoint():
    transport = ASGITransport(app=app, raise_app_exceptions=True)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"input_data": {"test_key": "test_value"}}
        response = await ac.post("/process_data/", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "input_data" in data
    assert data["input_data"] == {"test_key": "test_value"}

    assert "cat_fact" in data
    assert isinstance(data["cat_fact"], dict)
    assert "fact" in data["cat_fact"]
    assert isinstance(data["cat_fact"]["fact"], str)
