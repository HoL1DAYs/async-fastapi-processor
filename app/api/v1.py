from fastapi import APIRouter
from app.services.processor import process_data
from app.models.schemas import ProcessRequest, ProcessResponse

router = APIRouter()

@router.post("/", response_model=ProcessResponse)
async def process_endpoint(request: ProcessRequest):
    return await process_data(request.input_data)
