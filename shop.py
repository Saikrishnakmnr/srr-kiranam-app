import streamlit as st
from config.settings import load_settings
from components.ui import header, footer, product_card
from components.cart import init_cart, add, count
from services.catalog import get_categories, get_products

settings=load_settings(); init_cart(); header(settings)
st.markdown('<div class="section-head"><div><h2>🛍️ Shop</h2><p>Search the catalog and add products to your cart.</p></div></div>', unsafe_allow_html=True)

cats = get_categories(); products = get_products()
search_col, cat_col = st.columns([2,1])
with search_col: query = st.text_input("Search", placeholder="Try rice, milk, soap...", label_visibility="collapsed")
with cat_col: selected = st.selectbox("Category", ["All"] + [c.get("name", "Category") for c in cats], label_visibility="collapsed")

filtered = products
if selected != "All": filtered = [p for p in filtered if str(p.get("category_name", "")).lower() == str(selected).lower()]
if query: filtered = [p for p in filtered if query.lower() in str(p.get("name", "")).lower() or query.lower() in str(p.get("description", "")).lower()]

st.caption(f"{len(filtered)} product(s)")
if not filtered: st.info("No products match your search.")
else:
    cols = st.columns(4)
    for i,p in enumerate(filtered):
        with cols[i % 4]:
            product_card(p)
            if st.button("Add to cart", key=f"shop_add_{p.get('id', i)}", use_container_width=True):
                add(p); st.toast(f"Added {p.get('name','product')} to cart")

st.markdown(f'<div class="cartbar">🛒 <b>{count()}</b> item(s) in cart · Open Cart when you are ready.</div>', unsafe_allow_html=True)
footer(settings)
