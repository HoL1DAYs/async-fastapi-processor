import httpx
import json
import uuid
from app.services.redis_client import redis_client
from app.services.logger import logger
from app.core.config import settings


async def process_data(input_data: dict) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.external_api_url)
            response.raise_for_status()
            cat_fact = response.json()
    except httpx.RequestError as e:
        logger.error(f"HTTP error: {e}")
        raise
    except Exception as e:
        logger.exception("Unexpected error during external request")
        raise

    result = {
        "input_data": input_data,
        "cat_fact": cat_fact
    }

    log_entry = {
        "id": str(uuid.uuid4()),
        "input": input_data,
        "output": cat_fact
    }

    await redis_client.set(log_entry["id"], json.dumps(log_entry))
    logger.info(f"Processed request: {log_entry['id']}")

    return result
