from fastapi import APIRouter, Request
from app.services.processor import process_data
from app.models.schemas import ProcessResponse

router = APIRouter()

@router.post("/", response_model=ProcessResponse)
async def process_endpoint(request: Request):
    data = await request.json()
    result = await process_data(data)
    return result
