import streamlit as st


def init_cart():
    """Initialize the shopping cart in session state."""
    if "cart" not in st.session_state:
        st.session_state["cart"] = {}


def add_to_cart(product, quantity=1):
    """Add a product to the cart."""
    init_cart()

    product_id = product.get("id")

    if product_id is None:
        product_id = product.get("name")

    key = str(product_id)

    if key in st.session_state["cart"]:
        st.session_state["cart"][key]["quantity"] += quantity
    else:
        st.session_state["cart"][key] = {
            "id": product.get("id"),
            "name": product.get("name", "Product"),
            "price": product.get("price", 0),
            "mrp": product.get("mrp", product.get("price", 0)),
            "image_url": product.get("image_url", ""),
            "quantity": quantity,
        }


def remove_from_cart(product_id):
    """Remove a product completely from the cart."""
    init_cart()

    key = str(product_id)

    if key in st.session_state["cart"]:
        del st.session_state["cart"][key]


def update_quantity(product_id, quantity):
    """Update the quantity of a cart item."""
    init_cart()

    key = str(product_id)

    if key not in st.session_state["cart"]:
        return

    if quantity <= 0:
        del st.session_state["cart"]
    else:
        st.session_state["cart"][key]["quantity"] = quantity


def clear_cart():
    """Remove all products from the cart."""
    st.session_state["cart"] = {}


def get_cart_items():
    """Return cart items as a list."""
    init_cart()
    return list(st.session_state["cart"].values())


def get_cart_count():
    """Return total number of items in the cart."""
    init_cart()

    return sum(
        item.get("quantity", 0)
        for item in st.session_state["cart"].values()
    )


def get_cart_subtotal():
    """Return cart subtotal."""
    init_cart()

    total = 0

    for item in st.session_state["cart"].values():
        price = float(item.get("price", 0) or 0)
        quantity = int(item.get("quantity", 0) or 0)
        total += price * quantity

    return total


def get_cart_total():
    """Return current cart total."""
    return get_cart_subtotal()
