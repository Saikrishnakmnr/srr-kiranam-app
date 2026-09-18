import streamlit as st


def inject_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: #070711;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 1rem;
            padding-bottom: 3rem;
        }

        .neon-card {
            background: rgba(20, 20, 35, 0.92);
            border: 1px solid rgba(0, 255, 255, 0.25);
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 0 18px rgba(0, 255, 255, 0.08);
        }

        .product-card {
            background: rgba(20, 20, 35, 0.95);
            border: 1px solid rgba(0, 255, 255, 0.2);
            border-radius: 18px;
            padding: 15px;
            margin-bottom: 20px;
        }

        h1, h2, h3 {
            letter-spacing: 0.5px;
        }

        button {
            border-radius: 12px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def header(settings=None):
    store_name = "SRR Kiranam"

    if settings:
        store_name = settings.get(
            "store_name",
            settings.get("name", store_name),
        )

    st.markdown(
        f"""
        <div style="
            padding:15px 5px 10px 5px;
            text-align:center;
        ">
            <h1 style="
                margin:0;
                font-size:32px;
                font-weight:800;
            ">
                ⚡ {store_name}
            </h1>
            <div style="opacity:.7;">
                Fast local delivery
            </div>
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
        ("Sign In", "pages/login.py", "🔐"),
        ("Admin", "pages/admin.py", "⚙️"),
    ]

    for col, (label, path, icon) in zip(cols, links):
        with col:
            if st.button(
                label,
                key=f"nav_{label.lower().replace(' ', '_')}",
                icon=icon,
                use_container_width=True,
            ):
                st.switch_page(path)


def product_card(product):
    name = product.get("name", "Product")
    price = product.get("price", product.get("selling_price", 0))
    mrp = product.get("mrp", 0)

    st.markdown(
        f"""
        <div class="product-card">
            <h3>{name}</h3>
            <div style="font-size:22px;font-weight:700;">
                ₹{price}
            </div>
            <div style="opacity:.6;">
                MRP ₹{mrp}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer(settings=None):
    st.markdown(
        """
        <hr>
        <div style="
            text-align:center;
            opacity:.6;
            padding:20px 0;
        ">
            © SRR Kiranam · Local Delivery
        </div>
        """,
        unsafe_allow_html=True,
    )
