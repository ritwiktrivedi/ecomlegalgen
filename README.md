# 🎈 EcomLegalGen

A simple Streamlit app to generate base legal templates for an ecommerce store.

The templates assume use of Razorpay payment Gateway and Shopify as the ecom service provider.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ecomlegalgen.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

PS: I first setup a virtual environment using a tool like uv in WSL.

```
uv venv
uv pip install -r requirements.txt
source .venv/bin/activate
(ecomlegalgen) $> streamlit run streamlit_app.py
```
