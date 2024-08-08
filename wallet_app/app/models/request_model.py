
from pydantic import BaseModel
from typing import Optional, Dict

class SupabaseRequest(BaseModel):
    table: str
    action: str
    conditions: Optional[Dict] = None
    data: Optional[Dict] = None
