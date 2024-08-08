
from fastapi import HTTPException
from app.models.request_model import SupabaseRequest
from app.services.supabase_service import perform_supabase_action

async def handle_extension_request(request: SupabaseRequest):
    try:
        result = perform_supabase_action(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
