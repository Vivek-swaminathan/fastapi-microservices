
from fastapi import APIRouter
from app.controllers.developer_controller import handle_developer_api_request
from app.models.request_model import SupabaseRequest

router = APIRouter()

@router.post("/developer-api/")
async def developer_api_endpoint(request: SupabaseRequest):
    return await handle_developer_api_request(request)
