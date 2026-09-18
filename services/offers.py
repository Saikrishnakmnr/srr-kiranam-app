from .supabase_client import get_supabase
def get_active_offers():
    sb=get_supabase()
    if not sb: return []
    try:
        return sb.table("offers").select("*").eq("active",True).execute().data or []
    except Exception: return []
