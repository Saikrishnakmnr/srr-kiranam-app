import streamlit as st
from components.ui import inject_css, header, footer
from config.settings import load_settings
from services.supabase_client import get_supabase

settings=load_settings(); st.set_page_config(page_title="Admin | SRR Kiranam",page_icon="⚙️",layout="wide")
inject_css(); header(settings)
st.title("⚙️ Admin")
st.caption("Management console foundation. Protect this page with Supabase Auth before production use.")

tabs=st.tabs(["Store","Products","Offers","Delivery","Orders","Content","Marketing"])
with tabs[0]:
    st.subheader("Store branding")
    st.text_input("Store name", settings.get("store_name","SRR Kiranam"))
    st.text_input("Tagline", settings.get("tagline","Everyday essentials, delivered to your door."))
    st.selectbox("Business type", ["Grocery","Plastic & Home Needs","Stationery","Bakery","General Store","Other"])
with tabs[1]:
    st.info("Product CRUD connects to Supabase `products`.")
with tabs[2]:
    st.info("Create percentage, flat, coupon and free-delivery offers in Supabase.")
with tabs[3]:
    st.info("Configure delivery zones, distance limits and charges.")
with tabs[4]:
    st.info("Manage order status: New → Confirmed → Packing → Ready → Out for delivery → Delivered.")
with tabs[5]:
    st.info("Manage public About, FAQ, Delivery, Policy and Guide content.")
with tabs[6]:
    st.info("GA4 and AdSense IDs should be configured as secrets/environment variables.")
footer(settings)
