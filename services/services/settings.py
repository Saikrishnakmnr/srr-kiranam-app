import streamlit as st


DEFAULT_SETTINGS = {
    "store_name": "SRR Kiranam",
    "business_type": "Kiranam Store",
    "tagline": "Fresh groceries delivered to your door",
    "phone": "",
    "whatsapp": "",
    "address": "",
    "logo_url": "",
    "favicon_url": "",
}


def load_settings():
    """Load store settings from Supabase.

    Falls back to safe default settings if the table
    is unavailable or not yet configured.
    """

    settings = DEFAULT_SETTINGS.copy()

    try:
        from services.supabase_client import get_supabase

        supabase = get_supabase()

        if supabase is None:
            return settings

        response = (
            supabase
            .table("store_settings")
            .select("*")
            .limit(1)
            .execute()
        )

        rows = response.data or []

        if not rows:
            return settings

        row = rows[0]

        # Store name
        settings["store_name"] = (
            row.get("store_name")
            or row.get("name")
            or settings["store_name"]
        )

        # Business type
        settings["business_type"] = (
            row.get("business_type")
            or row.get("store_type")
            or settings["business_type"]
        )

        # Tagline
        settings["tagline"] = (
            row.get("tagline")
            or row.get("description")
            or settings["tagline"]
        )

        # Contact information
        settings["phone"] = (
            row.get("phone")
            or row.get("phone_number")
            or ""
        )

        settings["whatsapp"] = (
            row.get("whatsapp")
            or row.get("whatsapp_number")
            or ""
        )

        # Address
        settings["address"] = (
            row.get("address")
            or row.get("store_address")
            or ""
        )

        # Branding
        settings["logo_url"] = (
            row.get("logo_url")
            or row.get("logo")
            or ""
        )

        settings["favicon_url"] = (
            row.get("favicon_url")
            or row.get("favicon")
            or ""
        )

    except Exception:
        # Keep the app working even if settings are not available.
        pass

    return settings
