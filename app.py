import streamlit as st
from config.settings import load_settings
from components.ui import inject_css, header, footer
from services.catalog import get_categories, get_products
from services.offers import get_active_offers

st.set_page_config(page_title="SRR Kiranam", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")
settings = load_settings()
inject_css()
header(settings)

st.markdown(f"""
<div class="hero">
  <div class="hero-kicker">⚡ {settings.get('business_type','Local Store').upper()}</div>
  <h1>{settings.get('store_name','SRR Kiranam')}</h1>
  <p>{settings.get('tagline','Everyday essentials, delivered to your door.')}</p>
  <div><a class="neon-btn" href="?page=shop">SHOP NOW</a></div>
</div>
""", unsafe_allow_html=True)

offers = get_active_offers()
if offers:
    st.subheader("🔥 Offers")
    cols = st.columns(min(3, len(offers)))
    for i, offer in enumerate(offers[:3]):
        with cols[i]:
            st.markdown(f"""<div class="offer-card"><b>{offer.get('name','Special Offer')}</b><br>
            {offer.get('description','Limited-time offer')}<br>
            <span>{offer.get('discount_value',0)}% OFF</span></div>""", unsafe_allow_html=True)

st.subheader("Shop by category")
cats = get_categories()
if cats:
    cols = st.columns(min(4, len(cats)))
    for i, cat in enumerate(cats[:8]):
        with cols[i]:
            st.markdown(f'<div class="category-card">✦ {cat.get("name","Category")}</div>', unsafe_allow_html=True)
else:
    st.info("Add categories from Admin.")

st.subheader("Featured products")
products = get_products(featured=True)
if products:
    cols = st.columns(min(4, len(products)))
    for i, p in enumerate(products[:8]):
        with cols[i]:
            price = p.get("selling_price", p.get("price", 0))
            st.markdown(f"""<div class="product-card">
            <div class="product-image">🛍️</div>
            <h3>{p.get('name','Product')}</h3>
            <p>{p.get('description','')}</p>
            <strong>₹{price}</strong>
            </div>""", unsafe_allow_html=True)
else:
    st.info("Add featured products from Admin.")

footer(settings)
