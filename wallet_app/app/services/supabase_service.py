
from app.models.request_model import SupabaseRequest
from supabase_client import supabase

def perform_supabase_action(request: SupabaseRequest):
    table = supabase.table(request.table)
    if request.action == "insert":
        return table.insert(request.data).execute().data
    elif request.action == "select":
        query = table.select("*")
        if request.conditions:
            for key, value in request.conditions.items():
                query = query.eq(key, value)
        return query.execute().data
    elif request.action == "update":
        query = table.update(request.data)
        if request.conditions:
            for key, value in request.conditions.items():
                query = query.eq(key, value)
        return query.execute().data
    elif request.action == "delete":
        query = table.delete()
        if request.conditions:
            for key, value in request.conditions.items():
                query = query.eq(key, value)
        return query.execute().data
    else:
        raise ValueError("Invalid action specified.")
