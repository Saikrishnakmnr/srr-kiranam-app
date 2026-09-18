import streamlit as st

def inject_css():
    st.markdown("""<style>
    :root{--neon:#7c3aed;--cyan:#06b6d4;--pink:#ec4899;--bg:#070711;--card:#11111d}
    .stApp{background:radial-gradient(circle at 15% 10%,#17103b 0,transparent 35%),radial-gradient(circle at 85% 20%,#082d35 0,transparent 30%),var(--bg);color:#f8fafc}
    .block-container{max-width:1200px;padding-top:1rem}
    .hero{padding:4rem 2rem;margin:1rem 0 2rem;border:1px solid #ffffff22;border-radius:28px;background:linear-gradient(135deg,#141127cc,#08232dcc);box-shadow:0 0 45px #7c3aed33}
    .hero-kicker{color:#22d3ee;font-weight:800;letter-spacing:.12em}
    .hero h1{font-size:clamp(2.5rem,7vw,5.5rem);line-height:.95;background:linear-gradient(90deg,#22d3ee,#a78bfa,#f472b6);-webkit-background-clip:text;color:transparent;text-shadow:0 0 30px #7c3aed55}
    .hero p{font-size:1.2rem;color:#cbd5e1}
    .neon-btn{display:inline-block;padding:.8rem 1.2rem;border-radius:999px;border:1px solid #22d3ee;color:white;text-decoration:none;box-shadow:0 0 20px #22d3ee55}
    .product-card,.category-card,.offer-card{border:1px solid #ffffff18;border-radius:20px;padding:1rem;background:#11111dcc;box-shadow:0 0 22px #7c3aed22;margin-bottom:1rem;min-height:150px}
    .product-card:hover,.category-card:hover,.offer-card:hover{transform:translateY(-3px);box-shadow:0 0 30px #22d3ee33}
    .product-image{height:120px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#18152d,#0d3035);font-size:3rem}
    .offer-card span{color:#22d3ee;font-size:1.4rem;font-weight:900}
    footer{margin-top:4rem;padding:2rem 0;color:#94a3b8;border-top:1px solid #ffffff12}
    </style>""", unsafe_allow_html=True)

def header(settings):
    st.markdown(f"### ⚡ {settings.get('store_name','SRR Kiranam')}")

def footer(settings):
    st.markdown(f"<footer>© {settings.get('store_name','SRR Kiranam')} · {settings.get('address','Karimnagar, Telangana')}</footer>", unsafe_allow_html=True)
