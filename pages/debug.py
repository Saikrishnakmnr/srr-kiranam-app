import streamlit as st

from services.supabase_client import get_supabase


st.set_page_config(
    page_title="Database Check",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Supabase Database Check")

supabase = get_supabase()

if supabase is None:
    st.error("Supabase client is not configured.")
    st.stop()

st.success("Supabase client connected.")

st.subheader("kiranam_categories")

try:
    response = (
        supabase
        .table("kiranam_categories")
        .select("*")
        .execute()
    )

    st.write("Rows returned:", len(response.data or []))

    st.json(response.data or [])

except Exception as e:
    st.error("Category query failed")
    st.exception(e)


st.subheader("kiranam_products")

try:
    response = (
        supabase
        .table("kiranam_products")
        .select("*")
        .execute()
    )

    st.write("Rows returned:", len(response.data or []))

    st.json(response.data or [])

except Exception as e:
    st.error("Product query failed")
    st.exception(e)
