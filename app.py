import streamlit as st

from components.ui import inject_css
from components.cart import init_cart


st.set_page_config(
    page_title="SRR Kiranam",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
init_cart()


pages = [
    st.Page("pages/home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/shop.py", title="Shop", icon="🛍️"),
    st.Page("pages/cart.py", title="Cart", icon="🛒"),
    st.Page("pages/checkout.py", title="Checkout", icon="💳"),
    st.Page("pages/orders.py", title="Orders", icon="📦"),
    st.Page("pages/login.py", title="Sign In", icon="🔐"),
    st.Page("pages/debug.py", title="Database Check", icon="🔎"),
    st.Page("pages/admin.py", title="Admin", icon="⚙️"),
    
]


current = st.navigation(
    pages,
    position="hidden",
)

current.run()
