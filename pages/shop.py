import streamlit as st
from components.ui import inject_css, header, footer
from config.settings import load_settings
from services.catalog import get_categories, get_products

st.set_page_config(page_title="Shop | SRR Kiranam", page_icon="🛒", layout="wide")
settings = load_settings()
inject_css(); header(settings)
st.title("🛒 Shop")

cats = get_categories()
cat_names = ["All"] + [c["name"] for c in cats]
selected = st.selectbox("Category", cat_names)
query = st.text_input("🔎 Search products", placeholder="Search rice, oil, buckets...")

products = get_products()
if selected != "All":
    products = [p for p in products if str(p.get("category_name","")).lower() == selected.lower()]
if query:
    products = [p for p in products if query.lower() in str(p.get("name","")).lower()]

if not products:
    st.info("No products found.")
else:
    cols = st.columns(4)
    for i,p in enumerate(products):
        with cols[i % 4]:
            st.markdown(f"""<div class="product-card"><div class="product-image">🛍️</div>
            <h3>{p.get('name','Product')}</h3><p>{p.get('description','')}</p>
            <strong>₹{p.get('selling_price',p.get('price',0))}</strong></div>""", unsafe_allow_html=True)
footer(settings)
