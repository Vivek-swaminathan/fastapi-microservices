
from fastapi import HTTPException
import httpx
from app.models.request_model import SupabaseRequest

async def call_service(url: str, request: SupabaseRequest):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=request.dict())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"Error from {url.split('/')[-2]} service")

""" async def call_subservice(request: SupabaseRequest):
    return await call_service("http://localhost:8001/dynamic/", request) """

async def call_wallet_service(request: SupabaseRequest):
    return await call_service("http://localhost:8001/wallet/", request)

async def call_hushh_service(request: SupabaseRequest):
    return await call_service("http://localhost:8002/hushh/", request)

async def call_extension_service(request: SupabaseRequest):
    return await call_service("http://localhost:8003/extension/", request)

async def call_developer_api_service(request: SupabaseRequest):
    return await call_service("http://localhost:8004/developer-api/", request)
