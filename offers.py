from .supabase_client import get_supabase, table_columns


def get_active_offers():
    sb = get_supabase()
    if not sb:
        return []
    try:
        cols = table_columns("offers")
        if not cols:
            return []
        q = sb.table("offers").select("*")
        if "active" in cols:
            q = q.eq("active", True)
        return q.execute().data or []
    except Exception:
        return []
