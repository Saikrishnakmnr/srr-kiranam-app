import streamlit as st


def init_cart():
    if "cart" not in st.session_state:
        st.session_state.cart = {}


def add(product):
    init_cart()
    pid = str(product.get("id") or product.get("slug") or product.get("name"))
    item = dict(product)
    item["price"] = product.get("selling_price", product.get("price", 0))
    current = st.session_state.cart.get(pid, {"product": item, "qty": 0})
    current["qty"] += 1
    st.session_state.cart[pid] = current


def remove(pid):
    init_cart()
    if pid in st.session_state.cart:
        st.session_state.cart[pid]["qty"] -= 1
        if st.session_state.cart[pid]["qty"] <= 0:
            del st.session_state.cart[pid]


def items():
    init_cart()
    return list(st.session_state.cart.values())


def count():
    return sum(x["qty"] for x in items())


def subtotal():
    total = 0.0
    for x in items():
        try: total += float(x["product"].get("price", 0) or 0) * x["qty"]
        except Exception: pass
    return total
