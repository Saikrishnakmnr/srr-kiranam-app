from .supabase_client import get_supabase, table_columns

CATEGORY_TABLE = "kiranam_categories"
PRODUCT_TABLE = "kiranam_products"


def _first_existing(d, *keys, default=None):
    for key in keys:
        if key in d and d.get(key) is not None:
            return d.get(key)
    return default


def get_categories(active_only=True):
    sb = get_supabase()
    if not sb:
        return []
    try:
        q = sb.table(CATEGORY_TABLE).select("*")
        cols = table_columns(CATEGORY_TABLE)
        if active_only and "active" in cols:
            q = q.eq("active", True)
        if "sort_order" in cols:
            q = q.order("sort_order")
        else:
            q = q.order("name")
        return q.execute().data or []
    except Exception:
        return []


def get_products(featured=False, active_only=True):
    sb = get_supabase()
    if not sb:
        return []
    try:
        cols = table_columns(PRODUCT_TABLE)
        q = sb.table(PRODUCT_TABLE).select("*")
        if active_only and "active" in cols:
            q = q.eq("active", True)
        if featured and "featured" in cols:
            q = q.eq("featured", True)
        if "name" in cols:
            q = q.order("name")
        rows = q.execute().data or []
        cats = {str(c.get("id")): c.get("name") for c in get_categories(False)}
        for p in rows:
            cat_id = _first_existing(p, "category_id", "category")
            nested = p.get("categories") or {}
            p["category_name"] = nested.get("name") if isinstance(nested, dict) else cats.get(str(cat_id), "")
            p["selling_price"] = _first_existing(p, "selling_price", "sale_price", "price", default=0)
            p["image_url"] = _first_existing(p, "image_url", "image", "photo_url", "thumbnail_url")
        return rows
    except Exception:
        return []


def get_product_count():
    return len(get_products(featured=False, active_only=False))


def save_category(name, slug=None):
    sb = get_supabase()
    if not sb:
        return False, "Supabase is not configured."
    try:
        cols = table_columns(CATEGORY_TABLE)
        payload = {"name": name}
        if "slug" in cols:
            payload["slug"] = slug or name.strip().lower().replace(" ", "-")
        if "active" in cols:
            payload["active"] = True
        if "sort_order" in cols:
            payload["sort_order"] = 0
        sb.table(CATEGORY_TABLE).insert(payload).execute()
        return True, "Category added."
    except Exception as exc:
        return False, str(exc)


def save_product(values):
    sb = get_supabase()
    if not sb:
        return False, "Supabase is not configured."
    try:
        cols = table_columns(PRODUCT_TABLE)
        payload = {}
        aliases = {
            "name": ["name"], "slug": ["slug"], "description": ["description"],
            "price": ["price", "selling_price", "sale_price"], "mrp": ["mrp"],
            "category_id": ["category_id"], "image_url": ["image_url", "image", "photo_url"],
            "featured": ["featured"], "active": ["active"], "stock": ["stock", "stock_quantity"],
            "unit": ["unit"],
        }
        for key, candidates in aliases.items():
            if values.get(key) is None or values.get(key) == "":
                continue
            target = next((c for c in candidates if c in cols), None)
            if target:
                payload[target] = values[key]
        if "slug" in cols and "slug" not in payload:
            payload["slug"] = values["name"].strip().lower().replace(" ", "-")
        if "active" in cols and "active" not in payload:
            payload["active"] = True
        sb.table(PRODUCT_TABLE).insert(payload).execute()
        return True, "Product added successfully."
    except Exception as exc:
        return False, str(exc)
