import html
import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    :root { --bg:#070914; --card:#101525; --card2:#141b2e; --line:rgba(255,255,255,.10); --text:#f7f9ff; --muted:#9ba8bf; --cyan:#25d9ff; --violet:#8b5cf6; --pink:#ff4fa3; --green:#35e0a1; }
    .stApp { background: radial-gradient(circle at 8% 0%, rgba(139,92,246,.18), transparent 30%), radial-gradient(circle at 92% 10%, rgba(37,217,255,.13), transparent 28%), var(--bg); color:var(--text); }
    [data-testid="stSidebar"] { display:none; }
    .block-container { max-width:1240px; padding: 1.2rem 1.2rem 4rem; }
    header[data-testid="stHeader"] { background:transparent; }
    .topbar { display:flex; align-items:center; justify-content:space-between; gap:1rem; padding:.75rem 0 1rem; border-bottom:1px solid var(--line); margin-bottom:1rem; }
    .brand { font-size:1.35rem; font-weight:900; letter-spacing:-.02em; }
    .brand-mark { color:var(--cyan); text-shadow:0 0 18px rgba(37,217,255,.45); }
    .navhint { color:var(--muted); font-size:.9rem; }
    .hero { position:relative; overflow:hidden; padding:3.3rem 2rem; border:1px solid rgba(255,255,255,.10); border-radius:32px; background:linear-gradient(135deg,rgba(17,21,37,.96),rgba(8,30,43,.92)); box-shadow:0 20px 70px rgba(0,0,0,.25), 0 0 55px rgba(139,92,246,.12); }
    .hero:after { content:""; position:absolute; width:260px; height:260px; right:-100px; top:-110px; border-radius:50%; background:rgba(37,217,255,.13); filter:blur(5px); }
    .eyebrow { color:var(--cyan); font-weight:800; letter-spacing:.14em; text-transform:uppercase; font-size:.78rem; }
    .hero h1 { font-size:clamp(2.6rem,7vw,5.8rem); line-height:.95; margin:.65rem 0 1rem; letter-spacing:-.055em; background:linear-gradient(90deg,#36dcff,#9b8cff,#ff67b1); -webkit-background-clip:text; background-clip:text; color:transparent; }
    .hero p { max-width:680px; color:#c9d4e8; font-size:1.12rem; line-height:1.6; }
    .hero-badges { display:flex; flex-wrap:wrap; gap:.6rem; margin-top:1.3rem; }
    .pill { display:inline-flex; align-items:center; gap:.35rem; padding:.48rem .8rem; border-radius:999px; border:1px solid var(--line); background:rgba(255,255,255,.045); color:#dbe7f8; font-size:.84rem; }
    .section-head { display:flex; justify-content:space-between; align-items:end; gap:1rem; margin:2rem 0 1rem; }
    .section-head h2 { margin:0; font-size:1.55rem; letter-spacing:-.03em; }
    .section-head p { margin:.25rem 0 0; color:var(--muted); font-size:.9rem; }
    .category-card { min-height:112px; padding:1.15rem; border:1px solid var(--line); border-radius:22px; background:linear-gradient(145deg,rgba(20,27,46,.95),rgba(11,15,28,.92)); box-shadow:0 12px 35px rgba(0,0,0,.15); }
    .category-icon { font-size:1.8rem; }
    .category-name { margin-top:.6rem; font-weight:800; }
    .category-slug { color:var(--muted); font-size:.78rem; }
    .product-card { padding:.7rem; border:1px solid var(--line); border-radius:24px; background:linear-gradient(150deg,rgba(17,21,37,.98),rgba(12,16,28,.96)); box-shadow:0 14px 35px rgba(0,0,0,.18); height:100%; }
    .product-card:hover { border-color:rgba(37,217,255,.38); box-shadow:0 18px 45px rgba(37,217,255,.08); }
    .product-photo { height:175px; border-radius:18px; display:flex; align-items:center; justify-content:center; background:radial-gradient(circle at 50% 35%,rgba(37,217,255,.15),transparent 45%), linear-gradient(135deg,#151c31,#0a101f); overflow:hidden; }
    .product-photo img { width:100%; height:100%; object-fit:cover; }
    .product-placeholder { font-size:3.3rem; }
    .product-meta { padding:.75rem .25rem .15rem; }
    .product-name { font-size:1.02rem; font-weight:850; margin-bottom:.28rem; }
    .product-desc { color:var(--muted); min-height:2.6em; font-size:.84rem; line-height:1.45; }
    .price-row { display:flex; align-items:baseline; gap:.55rem; margin:.55rem 0 .25rem; }
    .price { font-size:1.2rem; font-weight:900; }
    .mrp { color:#7f8ba0; text-decoration:line-through; font-size:.82rem; }
    .discount { color:var(--green); font-size:.78rem; font-weight:800; }
    .offer-card { padding:1.15rem; border:1px solid rgba(37,217,255,.17); border-radius:22px; background:linear-gradient(135deg,rgba(37,217,255,.08),rgba(139,92,246,.08)); }
    .offer-title { font-weight:900; font-size:1.05rem; }
    .offer-copy { color:#b9c6da; font-size:.88rem; margin-top:.35rem; }
    .offer-badge { color:var(--cyan); font-weight:900; margin-top:.7rem; }
    .cartbar { position:sticky; bottom:12px; z-index:5; margin-top:1.2rem; padding:.75rem 1rem; border:1px solid rgba(37,217,255,.22); border-radius:20px; background:rgba(8,12,23,.92); backdrop-filter:blur(12px); box-shadow:0 12px 35px rgba(0,0,0,.28); }
    .stat-card { padding:1rem; border:1px solid var(--line); border-radius:18px; background:rgba(255,255,255,.035); }
    .stat-value { font-size:1.55rem; font-weight:900; }
    .stat-label { color:var(--muted); font-size:.78rem; }
    .admin-note { padding:1rem; border-radius:18px; border:1px solid rgba(53,224,161,.16); background:rgba(53,224,161,.055); color:#c8f7e7; }
    footer { margin-top:3rem; padding-top:1.5rem; border-top:1px solid var(--line); color:var(--muted); font-size:.85rem; }
    .stButton > button { border-radius:12px; border:1px solid rgba(37,217,255,.25); }
    .stButton > button:hover { border-color:var(--cyan); box-shadow:0 0 20px rgba(37,217,255,.12); }
    div[data-testid="stMetric"] { background:rgba(255,255,255,.035); border:1px solid var(--line); padding:.7rem; border-radius:16px; }
    @media (max-width: 700px) { .hero { padding:2.3rem 1.2rem; border-radius:24px; } .product-photo { height:145px; } .topbar { align-items:flex-start; flex-direction:column; } }
    </style>
    """, unsafe_allow_html=True)


def icon_for(name: str) -> str:
    text = (name or "").lower()
    mapping = [
        (("milk", "dairy", "curd", "butter", "cheese"), "🥛"),
        (("rice", "dal", "atta", "flour", "wheat", "grain"), "🌾"),
        (("oil", "ghee"), "🫗"),
        (("soap", "shampoo", "detergent", "clean"), "🧼"),
        (("bucket", "plastic", "box", "container"), "🪣"),
        (("biscuit", "snack", "chips", "chocolate"), "🍪"),
        (("drink", "juice", "water", "cola"), "🥤"),
    ]
    for words, icon in mapping:
        if any(w in text for w in words):
            return icon
    return "🛍️"


def product_card(product: dict):
    name = html.escape(str(product.get("name") or "Product"))
    desc = html.escape(str(product.get("description") or "Everyday essential"))
    image = product.get("image_url") or product.get("image") or product.get("photo_url")
    price = product.get("selling_price", product.get("price", 0))
    mrp = product.get("mrp")
    try:
        price_f = float(price or 0)
    except Exception:
        price_f = 0
    try:
        mrp_f = float(mrp) if mrp is not None else None
    except Exception:
        mrp_f = None
    discount = round((1 - price_f / mrp_f) * 100) if mrp_f and mrp_f > price_f else 0
    photo = f'<img src="{html.escape(str(image))}" alt="{name}">' if image else f'<div class="product-placeholder">{icon_for(name)}</div>'
    price_html = f'<span class="price">₹{price_f:,.2f}</span>'
    if mrp_f and mrp_f > price_f:
        price_html += f'<span class="mrp">₹{mrp_f:,.2f}</span><span class="discount">{discount}% OFF</span>'
    st.markdown(f'''<div class="product-card"><div class="product-photo">{photo}</div><div class="product-meta"><div class="product-name">{name}</div><div class="product-desc">{desc}</div><div class="price-row">{price_html}</div></div></div>''', unsafe_allow_html=True)


def header(settings):
    name = html.escape(str(settings.get("store_name", "SRR Kiranam")))
    st.markdown(f'''<div class="topbar"><div><div class="brand"><span class="brand-mark">⚡</span> {name}</div><div class="navhint">Fresh essentials · Simple ordering · Local delivery</div></div></div>''', unsafe_allow_html=True)
    cols = st.columns([1,1,1,1,1,1])
    links = [("Home","pages/home.py","🏠"),("Shop","pages/shop.py","🛍️"),("Cart","pages/cart.py","🛒"),("Orders","pages/orders.py","📦"),("Admin","pages/admin.py","⚙️"),("Checkout","pages/checkout.py","💳")]
    for col, (label, path, icon) in zip(cols, links):
        with col:
            st.page_link(path, label=label, icon=icon, use_container_width=True)


def footer(settings):
    name = html.escape(str(settings.get("store_name", "SRR Kiranam")))
    address = html.escape(str(settings.get("address", "Karimnagar, Telangana, India")))
    st.markdown(f'<footer>© {name} · {address}<br><span>Storefront powered by Streamlit + Supabase</span></footer>', unsafe_allow_html=True)
