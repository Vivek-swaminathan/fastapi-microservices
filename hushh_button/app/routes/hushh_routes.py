
from fastapi import APIRouter
from app.controllers.hushh_controller import handle_hushh_request
from app.models.request_model import SupabaseRequest

router = APIRouter()

@router.post("/hushh/")
async def hushh_endpoint(request: SupabaseRequest):
    return await handle_hushh_request(request)
