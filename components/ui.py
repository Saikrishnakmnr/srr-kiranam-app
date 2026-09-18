import streamlit as st


def inject_neon_css():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 10%, rgba(0,255,220,.08), transparent 30%),
                radial-gradient(circle at 90% 20%, rgba(140,0,255,.08), transparent 30%),
                #070b14;
            color: #f5f7ff;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 1rem;
            padding-bottom: 4rem;
        }

        .store-header {
            padding: 18px 20px;
            border: 1px solid rgba(0,255,220,.25);
            border-radius: 18px;
            background: rgba(12,18,32,.86);
            box-shadow: 0 0 25px rgba(0,255,220,.08);
            margin-bottom: 18px;
        }

        .store-title {
            font-size: 28px;
            font-weight: 800;
            margin: 0;
            background: linear-gradient(90deg,#00ffe0,#8b5cff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .store-tagline {
            color: #aeb8ca;
            font-size: 14px;
            margin-top: 3px;
        }

        .nav-button button {
            border-radius: 12px !important;
            border: 1px solid rgba(0,255,220,.20) !important;
            background: rgba(15,23,40,.85) !important;
        }

        .nav-button button:hover {
            border-color: #00ffe0 !important;
            box-shadow: 0 0 14px rgba(0,255,220,.20) !important;
        }

        .hero {
            padding: 34px 28px;
            border-radius: 24px;
            background:
                linear-gradient(135deg,
                    rgba(0,255,220,.13),
                    rgba(139,92,255,.13)),
                rgba(10,15,27,.92);
            border: 1px solid rgba(0,255,220,.22);
            box-shadow: 0 0 35px rgba(0,255,220,.07);
            margin-bottom: 28px;
        }

        .hero h1 {
            font-size: clamp(32px,5vw,58px);
            line-height: 1.05;
            margin-bottom: 10px;
        }

        .hero p {
            color: #b9c2d3;
            font-size: 17px;
        }

        .product-card {
            padding: 16px;
            border-radius: 18px;
            background: rgba(14,20,34,.92);
            border: 1px solid rgba(255,255,255,.08);
            margin-bottom: 16px;
            min-height: 190px;
        }

        .product-card:hover {
            border-color: rgba(0,255,220,.35);
            box-shadow: 0 0 22px rgba(0,255,220,.08);
        }

        .product-name {
            font-size: 18px;
            font-weight: 750;
            margin-top: 8px;
        }

        .product-price {
            font-size: 21px;
            font-weight: 800;
            color: #00ffe0;
        }

        .product-mrp {
            color: #7f8ba0;
            text-decoration: line-through;
            margin-left: 7px;
        }

        .discount-badge {
            display: inline-block;
            margin-top: 5px;
            padding: 3px 8px;
            border-radius: 999px;
            background: rgba(0,255,160,.10);
            color: #00ffb0;
            font-size: 12px;
            font-weight: 700;
        }

        .section-title {
            font-size: 25px;
            font-weight: 800;
            margin: 25px 0 14px;
        }

        .footer {
            margin-top: 50px;
            padding: 25px 10px;
            text-align: center;
            color: #7f8ba0;
            border-top: 1px solid rgba(255,255,255,.08);
        }

        @media (max-width: 700px) {
            .block-container {
                padding-left: .7rem;
                padding-right: .7rem;
            }

            .store-title {
                font-size: 23px;
            }

            .hero {
                padding: 24px 18px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def header(settings):
    store_name = settings.get("store_name", "SRR Kiranam")
    tagline = settings.get(
        "store_tagline",
        "Everyday essentials, delivered to your door."
    )

    st.markdown(
        f"""
        <div class="store-header">
            <div class="store-title">{store_name}</div>
            <div class="store-tagline">{tagline}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(6)

    links = [
        ("Home", "pages/home.py", "🏠"),
        ("Shop", "pages/shop.py", "🛍️"),
        ("Cart", "pages/cart.py", "🛒"),
        ("Orders", "pages/orders.py", "📦"),
        ("Admin", "pages/admin.py", "⚙️"),
        ("Checkout", "pages/checkout.py", "💳"),
    ]

    for col, (label, path, icon) in zip(cols, links):
        with col:
            if st.button(
                label,
                key=f"nav_{label.lower()}",
                icon=icon,
                use_container_width=True,
            ):
                st.switch_page(path)


def footer(settings):
    store_name = settings.get("store_name", "SRR Kiranam")

    st.markdown(
        f"""
        <div class="footer">
            © 2026 {store_name} · All rights reserved.
        </div>
        """,
        unsafe_allow_html=True,
    )
