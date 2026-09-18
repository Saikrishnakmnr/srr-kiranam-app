import streamlit as st
from config.settings import load_settings
from components.ui import header, footer, product_card
from components.cart import init_cart, add, count
from services.catalog import get_categories, get_products
from services.offers import get_active_offers

settings = load_settings(); init_cart(); header(settings)

st.markdown(f'''<section class="hero"><div class="eyebrow">⚡ {settings.get("business_type", "Local Store").upper()}</div><h1>{settings.get("store_name", "SRR Kiranam")}</h1><p>{settings.get("tagline", "Everyday essentials, delivered to your door.")}</p><div class="hero-badges"><span class="pill">🛒 Easy ordering</span><span class="pill">📍 Local delivery</span><span class="pill">💳 Secure checkout</span></div></section>''', unsafe_allow_html=True)

cats = get_categories(); products = get_products(); featured = get_products(featured=True) or products[:8]; offers = get_active_offers()

st.markdown('<div class="section-head"><div><h2>Shop by category</h2><p>Find what you need in a few taps.</p></div></div>', unsafe_allow_html=True)
if cats:
    cols = st.columns(min(4, len(cats)))
    for i, cat in enumerate(cats[:8]):
        name = str(cat.get("name", "Category")); low = name.lower()
        icon = "🥛" if "dairy" in low else "🏠" if "house" in low else "🛒"
        with cols[i % len(cols)]:
            st.markdown(f'<div class="category-card"><div class="category-icon">{icon}</div><div class="category-name">{name}</div><div class="category-slug">Browse in Shop →</div></div>', unsafe_allow_html=True)
else: st.info("No categories are available yet. Add them from Admin.")

st.markdown('<div class="section-head"><div><h2>Popular products</h2><p>Products currently available in your catalog.</p></div></div>', unsafe_allow_html=True)
if featured:
    cols = st.columns(4)
    for i, product in enumerate(featured[:8]):
        with cols[i % 4]:
            product_card(product)
            if st.button("Add to cart", key=f"home_add_{product.get('id', i)}", use_container_width=True):
                add(product); st.toast(f"Added {product.get('name', 'product')} to cart")
else: st.info("Your catalog is connected, but no active products were found.")

if offers:
    st.markdown('<div class="section-head"><div><h2>Offers & savings</h2><p>Promotions configured for your store.</p></div></div>', unsafe_allow_html=True)
    cols = st.columns(min(3, len(offers)))
    for i, offer in enumerate(offers[:3]):
        with cols[i]:
            value = offer.get("discount_value", offer.get("value", "")); suffix = "% OFF" if value != "" else ""
            st.markdown(f'<div class="offer-card"><div class="offer-title">{offer.get("name", "Special offer")}</div><div class="offer-copy">{offer.get("description", "Limited-time savings")}</div><div class="offer-badge">{value}{suffix}</div></div>', unsafe_allow_html=True)

st.markdown(f'<div class="cartbar">🛒 <b>{count()}</b> item(s) in your cart · Open <b>Cart</b> above to review.</div>', unsafe_allow_html=True)
footer(settings)
