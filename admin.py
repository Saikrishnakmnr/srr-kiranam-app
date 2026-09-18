import streamlit as st
from config.settings import load_settings
from components.ui import header, footer
from services.supabase_client import get_supabase, table_columns, db_status
from services.catalog import get_categories, get_products, save_category, save_product, CATEGORY_TABLE, PRODUCT_TABLE

settings=load_settings(); header(settings)
st.markdown('<div class="section-head"><div><h2>⚙️ Store Admin</h2><p>Manage the catalog without touching the code.</p></div></div>', unsafe_allow_html=True)

ok, status = db_status()
if ok: st.markdown('<div class="admin-note">● Database connected · Your existing Supabase tables are being used.</div>', unsafe_allow_html=True)
else: st.warning(status)

cats=get_categories(False); products=get_products(False, False)
st.markdown('<div style="height:.8rem"></div>', unsafe_allow_html=True)
m1,m2,m3=st.columns(3)
with m1: st.metric("Categories", len(cats))
with m2: st.metric("Products", len(products))
with m3: st.metric("Cart/orders", "Ready")

tabs=st.tabs(["🏪 Store", "🛍️ Products", "📂 Categories", "📦 Orders", "🎁 Offers", "🚚 Delivery"])

with tabs[0]:
    st.subheader("Store identity")
    st.caption("Your Streamlit/GitHub/Supabase project names stay unchanged. These are customer-facing settings.")
    with st.form("store_form"):
        name=st.text_input("Store name", settings.get("store_name","SRR Kiranam"))
        business=st.selectbox("Business type", ["Grocery","Plastic & Home Needs","Stationery","Bakery","General Store","Other"], index=0)
        tagline=st.text_input("Tagline", settings.get("tagline","Everyday essentials, delivered to your door."))
        address=st.text_area("Address", settings.get("address","Karimnagar, Telangana, India"))
        phone=st.text_input("Phone", settings.get("phone",""))
        if st.form_submit_button("Save store settings", type="primary"):
            sb=get_supabase()
            if not sb: st.error("Configure Supabase secrets first.")
            else:
                try:
                    cols=table_columns("store_settings")
                    rows=sb.table("store_settings").select("*").limit(1).execute().data or []
                    payload={}
                    for target, value in [("store_name",name),("store_address",address),("store_phone",phone)]:
                        if target in cols: payload[target]=value
                    if rows and payload:
                        sb.table("store_settings").update(payload).eq("id", rows[0].get("id")).execute()
                        st.success("Store settings saved. Refresh Home to see the changes.")
                    else: st.warning("No editable store_settings row/columns were detected.")
                except Exception as exc: st.error(f"Could not save settings: {exc}")

with tabs[1]:
    st.subheader("Add a product")
    cat_map={str(c.get("id")):c.get("name") for c in cats if c.get("id")}
    with st.form("add_product"):
        c1,c2=st.columns(2)
        with c1:
            pname=st.text_input("Product name *", placeholder="e.g. Aashirvaad Atta 5 kg")
            price=st.number_input("Selling price (₹) *", min_value=0.0, step=1.0, format="%.2f")
            mrp=st.number_input("MRP (₹)", min_value=0.0, step=1.0, format="%.2f")
            unit=st.text_input("Unit", placeholder="1 kg / 1 packet / 1 piece")
        with c2:
            description=st.text_area("Description", placeholder="Short product description")
            category_id=st.selectbox("Category", ["No category"] + list(cat_map.keys()), format_func=lambda x: "No category" if x=="No category" else cat_map.get(x,x))
            image_url=st.text_input("Image URL (optional)", placeholder="https://...")
            stock=st.number_input("Stock quantity", min_value=0, value=0, step=1)
        featured=st.checkbox("Show on Home as popular product")
        active=st.checkbox("Active / visible in Shop", value=True)
        submitted=st.form_submit_button("➕ Add product", type="primary", use_container_width=True)
        if submitted:
            if not pname.strip(): st.error("Product name is required.")
            else:
                success,msg=save_product({"name":pname.strip(),"description":description.strip(),"price":price,"mrp":mrp or None,"unit":unit.strip(),"category_id":None if category_id=="No category" else category_id,"image_url":image_url.strip(),"stock":stock,"featured":featured,"active":active})
                (st.success if success else st.error)(msg)

    st.subheader("Current catalog")
    if products:
        for i,p in enumerate(products):
            pid=p.get("id"); price=p.get("selling_price",p.get("price",0));
            row1,row2,row3,row4=st.columns([3,1,1,1])
            with row1: st.write(f"**{p.get('name','Product')}**"); st.caption(f"{p.get('category_name','Uncategorized')} · ₹{price}")
            with row2: st.write("Featured" if p.get("featured") else "—")
            with row3:
                if st.button("Delete", key=f"del_{pid}"):
                    try:
                        sb=get_supabase(); sb.table(PRODUCT_TABLE).delete().eq("id",pid).execute(); st.success("Deleted"); st.rerun()
                    except Exception as exc: st.error(str(exc))
            with row4:
                if st.button("Hide/Show", key=f"toggle_{pid}"):
                    try:
                        cols=table_columns(PRODUCT_TABLE)
                        if "active" not in cols: st.warning("This table has no active column.")
                        else:
                            sb=get_supabase(); sb.table(PRODUCT_TABLE).update({"active":not bool(p.get("active",True))}).eq("id",pid).execute(); st.rerun()
                    except Exception as exc: st.error(str(exc))
    else: st.info("No products found.")

with tabs[2]:
    st.subheader("Categories")
    with st.form("add_category"):
        cname=st.text_input("Category name", placeholder="Groceries")
        if st.form_submit_button("➕ Add category", type="primary"):
            if not cname.strip(): st.error("Enter a category name.")
            else:
                success,msg=save_category(cname.strip()); (st.success if success else st.error)(msg)
    if cats:
        for c in cats:
            st.write(f"**{c.get('name','Category')}**  ·  `{c.get('slug','')}`")

with tabs[3]:
    st.subheader("Orders")
    st.info("The existing `kiranam_orders` and `kiranam_order_items` tables are ready. The next step is connecting checkout to order creation and an admin order-status board.")

with tabs[4]:
    st.subheader("Offers")
    st.info("We will connect the offers engine after the catalog/cart flow is verified. This keeps the first deployment stable.")

with tabs[5]:
    st.subheader("Delivery")
    st.info("Delivery zones, distance pricing, free-delivery threshold and Google Maps will be connected after checkout is working.")

footer(settings)
