import os
from dotenv import load_dotenv
load_dotenv()


def _secret(name):
    value = os.getenv(name)
    if value:
        return value
    try:
        import streamlit as st
        return st.secrets.get(name)
    except Exception:
        return None


def get_supabase():
    try:
        from supabase import create_client
        url = _secret("SUPABASE_URL")
        key = _secret("SUPABASE_ANON_KEY")
        if not url or not key:
            return None
        return create_client(url, key)
    except Exception:
        return None


def table_columns(table_name):
    sb = get_supabase()
    if not sb:
        return set()
    try:
        rows = sb.table(table_name).select("*").limit(1).execute().data or []
        return set(rows[0].keys()) if rows else set()
    except Exception:
        return set()


def db_status():
    sb = get_supabase()
    if not sb:
        return False, "Supabase secrets are not configured."
    try:
        sb.table("store_settings").select("id").limit(1).execute()
        return True, "Connected to Supabase."
    except Exception as exc:
        return False, f"Supabase connection failed: {exc}"
