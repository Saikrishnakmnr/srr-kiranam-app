# SRR Kiranam — Streamlit Store

A modular Streamlit + Supabase foundation for a local delivery business. The first configuration is SRR Kiranam, but the branding/business type is designed to be changeable.

## Streamlit Community Cloud

1. Push this folder to your GitHub repository.
2. In Streamlit Community Cloud choose **Create app**.
3. Select the repository and branch.
4. Set the main file to `app.py`.
5. Add Supabase credentials under App Settings → Secrets.
6. Deploy.

No npm is required.

## Secrets

```toml
SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
SUPABASE_ANON_KEY = "YOUR_ANON_KEY"
STORE_NAME = "SRR Kiranam"
STORE_TAGLINE = "Everyday essentials, delivered to your door."
STORE_ADDRESS = "Karimnagar, Telangana, India"
GOOGLE_MAPS_API_KEY = "..."
RAZORPAY_KEY_ID = "..."
GA4_MEASUREMENT_ID = "G-..."
ADSENSE_CLIENT = "ca-pub-..."
```

Do not put Supabase service-role keys, Razorpay secret keys, or private credentials in GitHub.

## Architecture

`app.py` is the entry point. `pages/`, `components/`, `services/`, and `config/` keep the larger application maintainable.

The current files intentionally provide a safe UI/database foundation. Before accepting real orders, add authentication, server-side payment verification/webhooks, Google Maps address validation, delivery-distance logic, and strict authorization for admin operations.

## AdSense / SEO

This Streamlit build does not claim automatic AdSense approval. Keep useful public business content, privacy/policy pages, clear navigation, and comply with Google's current publisher policies. Use your AdSense account's current site setup/review instructions before serving ads.

For indexing, use descriptive public pages and submit the deployed domain/sitemap through Google Search Console where supported. Streamlit routing and search-engine rendering should be tested on the deployed app before relying on it for SEO-heavy product pages.
