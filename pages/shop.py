import streamlit as st

from components.ui import inject_css, header, footer
from services.catalog import get_categories, get_products
from services.settings import load_settings
from components.cart import add_to_cart, init_cart


st.set_page_config(
    page_title="Shop",
    page_icon="🛍️",
    layout="wide",
)

inject_css()
init_cart()

settings = load_settings()
header(settings)

st.markdown(
    """
    <h1 style="margin-top:25px;">🛍️ Shop</h1>
    <p style="opacity:.7;">Browse our products and add them to your cart.</p>
    """,
    unsafe_allow_html=True,
)

# Search
search = st.text_input(
    "🔎 Search products",
    placeholder="Search Milk, Rice, groceries...",
)

# Categories
categories = get_categories()

category_options = ["All"]

category_map = {}

for category in categories:
    category_id = category.get("id")
    category_name = category.get("name", "Category")

    category_options.append(category_name)

    category_map[category_name] = category_id

selected_category = st.selectbox(
    "📂 Category",
    category_options,
)

# Load products
selected_category_id = None

if selected_category != "All":
    selected_category_id = category_map.get(selected_category)

products = get_products(
    category_id=selected_category_id,
    search=search.strip() if search else None,
)

st.markdown("---")

if not products:
    st.info(
        "No products found. Please check your Supabase product data."
    )
else:
    st.markdown(
        f"### 🛒 {len(products)} product(s)"
    )

    columns = st.columns(3)

    for index, product in enumerate(products):
        with columns[index % 3]:

            name = product.get("name", "Product")
            price = product.get("price", 0)
            mrp = product.get("mrp", price)
            image_url = product.get("image_url", "")
            description = product.get("description", "")

            if image_url:
                st.image(
                    image_url,
                    use_container_width=True,
                )

            st.markdown(
                f"""
                <div class="neon-card">
                    <h3>{name}</h3>
                    <div style="font-size:24px;font-weight:800;">
                        ₹{price}
                    </div>
                    <div style="opacity:.6;">
                        MRP ₹{mrp}
                    </div>
                    <p style="opacity:.75;">
                        {description}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                f"🛒 Add {name}",
                key=f"add_product_{product.get('id', index)}",
                use_container_width=True,
            ):
                add_to_cart(product)
                st.success(f"{name} added to cart!")


footer(settings)
