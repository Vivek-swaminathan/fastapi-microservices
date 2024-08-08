
from fastapi import APIRouter
from app.controllers.extension_controller import handle_extension_request
from app.models.request_model import SupabaseRequest

router = APIRouter()

@router.post("/extension/")
async def extension_endpoint(request: SupabaseRequest):
    return await handle_extension_request(request)
