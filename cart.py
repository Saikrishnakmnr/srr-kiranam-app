import streamlit as st
from components.ui import inject_css, header, footer
from config.settings import load_settings
settings=load_settings(); st.set_page_config(page_title="Cart | SRR Kiranam",page_icon="🛒",layout="wide")
inject_css(); header(settings)
st.title("🛒 Cart")
st.info("Cart persistence and checkout will use the same Supabase order model. Add products from the Shop page once the catalog is configured.")
footer(settings)
