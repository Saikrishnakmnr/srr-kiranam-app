import os
from dotenv import load_dotenv
from services.supabase_client import get_supabase
load_dotenv()

DEFAULTS = {
    "store_name": "SRR Kiranam",
    "business_type": "Grocery",
    "tagline": "Everyday essentials, delivered to your door.",
    "address": "Karimnagar, Telangana, India",
    "phone": "",
    "whatsapp": "",
}


def load_settings():
    data = DEFAULTS.copy()
    try:
        import streamlit as st
        for key, env_name in [("store_name","STORE_NAME"),("business_type","BUSINESS_TYPE"),("tagline","STORE_TAGLINE"),("address","STORE_ADDRESS"),("phone","STORE_PHONE"),("whatsapp","STORE_WHATSAPP")]:
            value = st.secrets.get(env_name)
            if value:
                data[key] = value
    except Exception:
        pass
    for key, env_name in [("store_name","STORE_NAME"),("business_type","BUSINESS_TYPE"),("tagline","STORE_TAGLINE"),("address","STORE_ADDRESS"),("phone","STORE_PHONE"),("whatsapp","STORE_WHATSAPP")]:
        data[key] = os.getenv(env_name, data[key])

    sb = get_supabase()
    if sb:
        try:
            rows = sb.table("store_settings").select("*").limit(10).execute().data or []
            if rows:
                row = rows[0]
                data["store_name"] = row.get("store_name") or data["store_name"]
                data["address"] = row.get("store_address") or data["address"]
                data["phone"] = row.get("store_phone") or data["phone"]
        except Exception:
            pass
    return data
