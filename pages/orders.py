import streamlit as st
from config.settings import load_settings
from components.ui import header, footer
from services.supabase_client import get_supabase

settings=load_settings(); header(settings)
st.markdown('<div class="section-head"><div><h2>📦 My Orders</h2><p>Order history will appear here after customer authentication is enabled.</p></div></div>', unsafe_allow_html=True)
st.info("No customer account is signed in yet. This page is intentionally empty until authentication is connected.")
footer(settings)
