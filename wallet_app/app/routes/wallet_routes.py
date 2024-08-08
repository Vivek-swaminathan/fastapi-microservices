
from fastapi import APIRouter
from app.controllers.wallet_controller import handle_wallet_request
from app.models.request_model import SupabaseRequest

router = APIRouter()

@router.post("/wallet/")
async def wallet_endpoint(request: SupabaseRequest):
    return await handle_wallet_request(request)
