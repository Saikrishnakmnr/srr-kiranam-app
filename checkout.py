import streamlit as st
from components.ui import inject_css, header, footer
from config.settings import load_settings
settings=load_settings(); st.set_page_config(page_title="Checkout | SRR Kiranam",page_icon="💳",layout="wide")
inject_css(); header(settings)
st.title("💳 Checkout")
st.warning("Configure Supabase, Razorpay and Google Maps credentials before enabling live checkout.")
st.text_input("House / Flat number")
st.text_input("Landmark")
st.text_area("Delivery instructions")
st.button("Continue to payment")
footer(settings)
