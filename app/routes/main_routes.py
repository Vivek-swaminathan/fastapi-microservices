
from fastapi import APIRouter
from app.controllers.main_controller import (
    call_subservice, call_wallet_service, call_hushh_service, call_extension_service, call_developer_api_service
)
from app.models.request_model import SupabaseRequest

router = APIRouter()

""" @router.post("/interact-with-subservice/")
async def interact_with_subservice(request: SupabaseRequest):
    return await call_subservice(request)
 """
@router.post("/wallet-action/")
async def wallet_action(request: SupabaseRequest):
    return await call_wallet_service(request)

@router.post("/hushh-action/")
async def hushh_action(request: SupabaseRequest):
    return await call_hushh_service(request)

@router.post("/extension-action/")
async def extension_action(request: SupabaseRequest):
    return await call_extension_service(request)

@router.post("/developer-api-action/")
async def developer_api_action(request: SupabaseRequest):
    return await call_developer_api_service(request)
