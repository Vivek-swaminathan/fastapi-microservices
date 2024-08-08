
from fastapi import APIRouter
from app.controllers.sub_controller import handle_request
from app.models.request_model import SupabaseRequest

router = APIRouter()

@router.post("/dynamic/")
async def dynamic_endpoint(request: SupabaseRequest):
    return await handle_request(request)
