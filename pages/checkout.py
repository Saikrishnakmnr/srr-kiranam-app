import streamlit as st
from config.settings import load_settings
from components.ui import header, footer
from components.cart import init_cart, subtotal, count

settings=load_settings(); init_cart(); header(settings)
st.markdown('<div class="section-head"><div><h2>📍 Checkout</h2><p>We will connect this form to your delivery and payment flow next.</p></div></div>', unsafe_allow_html=True)
if count()==0:
    st.info("Add products to your cart first.")
else:
    st.metric("Cart total", f"₹{subtotal():,.2f}")
    with st.form("checkout_form"):
        name=st.text_input("Customer name")
        phone=st.text_input("Mobile number")
        address=st.text_area("Delivery address")
        landmark=st.text_input("Landmark (optional)")
        notes=st.text_area("Delivery instructions (optional)")
        method=st.radio("Payment", ["Cash on Delivery", "Online payment (Razorpay — coming next)"], horizontal=True)
        submitted=st.form_submit_button("Place order", type="primary", use_container_width=True)
        if submitted:
            if not name or not phone or not address: st.error("Please enter name, mobile number and delivery address.")
            else: st.success("Checkout form is ready. Order creation/payment will be connected after the catalog and cart are verified.")
footer(settings)
