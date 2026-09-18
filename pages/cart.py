import streamlit as st
from config.settings import load_settings
from components.ui import header, footer, product_card
from components.cart import init_cart, items, add, remove, subtotal

settings=load_settings(); init_cart(); header(settings)
st.markdown('<div class="section-head"><div><h2>🛒 Your Cart</h2><p>Review quantities before checkout.</p></div></div>', unsafe_allow_html=True)
rows = items()
if not rows:
    st.info("Your cart is empty. Open Shop and add something you need.")
else:
    for idx, row in enumerate(rows):
        p=row["product"]; pid=str(p.get("id") or p.get("slug") or p.get("name")); qty=row["qty"]
        c1,c2,c3,c4=st.columns([2.7,1,1,1])
        with c1: st.write(f"**{p.get('name','Product')}**"); st.caption(f"₹{float(p.get('price',0) or 0):,.2f} each")
        with c2:
            if st.button("−", key=f"minus_{pid}", use_container_width=True): remove(pid); st.rerun()
        with c3: st.markdown(f"<div style='padding:.55rem;text-align:center'><b>{qty}</b></div>", unsafe_allow_html=True)
        with c4:
            if st.button("+", key=f"plus_{pid}", use_container_width=True): add(p); st.rerun()
        st.divider()
    total=subtotal()
    st.metric("Subtotal", f"₹{total:,.2f}")
    if st.button("Continue to checkout →", type="primary", use_container_width=True):
        st.switch_page("pages/checkout.py")
footer(settings)
