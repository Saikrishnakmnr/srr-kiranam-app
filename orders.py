import streamlit as st
from components.ui import inject_css, header, footer
from config.settings import load_settings
settings=load_settings(); st.set_page_config(page_title="Orders | SRR Kiranam",page_icon="📦",layout="wide")
inject_css(); header(settings)
st.title("📦 My Orders")
st.info("Customer authentication and order history will load from Supabase after credentials are configured.")
footer(settings)
