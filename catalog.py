from .supabase_client import get_supabase

def get_categories():
    sb=get_supabase()
    if not sb: return []
    try:
        return sb.table("categories").select("*").eq("active", True).order("sort_order").execute().data or []
    except Exception: return []

def get_products(featured=False):
    sb=get_supabase()
    if not sb: return []
    try:
        q=sb.table("products").select("*, categories(name)").eq("active", True)
        if featured: q=q.eq("featured", True)
        data=q.order("name").execute().data or []
        for p in data: p["category_name"]=(p.get("categories") or {}).get("name","")
        return data
    except Exception: return []
