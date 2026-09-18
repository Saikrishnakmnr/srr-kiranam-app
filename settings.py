import os
from dotenv import load_dotenv
load_dotenv()

DEFAULTS = {
    "store_name":"SRR Kiranam",
    "business_type":"Grocery",
    "tagline":"Everyday essentials, delivered to your door.",
    "address":"Karimnagar, Telangana, India",
}
def load_settings():
    data = DEFAULTS.copy()
    try:
        import streamlit as st
        if hasattr(st, "secrets") and "STORE_NAME" in st.secrets:
            data["store_name"] = st.secrets["STORE_NAME"]
            data["tagline"] = st.secrets.get("STORE_TAGLINE", data["tagline"])
            data["address"] = st.secrets.get("STORE_ADDRESS", data["address"])
    except Exception:
        pass
    data["store_name"] = os.getenv("STORE_NAME", data["store_name"])
    data["tagline"] = os.getenv("STORE_TAGLINE", data["tagline"])
    data["address"] = os.getenv("STORE_ADDRESS", data["address"])
    return data
