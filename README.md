# SRR Shop — Streamlit storefront

This version is designed for the existing setup:

- Streamlit: `https://srr-shop.streamlit.app/`
- GitHub repository: `srr-kiranam-app`
- Supabase project: `srr-kiranam-app`

## Important

Upload the **contents of this folder** to the root of the existing GitHub repository and replace the older app files. Do not rename the repository or Supabase project.

The app uses the existing Supabase tables:

- `store_settings`
- `kiranam_categories`
- `kiranam_products`
- `kiranam_profiles`
- `kiranam_orders`
- `kiranam_order_items`

The first release focuses on a polished customer catalog, cart, and real Admin category/product entry. Checkout, authentication, Razorpay, Maps, delivery rules, offers, analytics and SEO can then be connected incrementally.

## Streamlit Cloud secrets

In App settings → Secrets, add:

```toml
SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
SUPABASE_ANON_KEY = "YOUR_ANON_KEY"
STORE_NAME = "SRR Kiranam"
STORE_TAGLINE = "Everyday essentials, delivered to your door."
STORE_ADDRESS = "Karimnagar, Telangana, India"
```

Never put a Supabase service-role key or Razorpay secret in GitHub.
