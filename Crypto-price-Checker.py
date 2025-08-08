import streamlit as st
import requests
from datetime import datetime

# 🖼️ Page Setup
st.set_page_config(page_title="Crypto Price Checker", page_icon="💹", layout="centered")

# 💅 Aesthetic CSS Styling with Image Background
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron&family=Poppins:wght@400;600&display=swap');

        html, body, .stApp {
            height: 100%;
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                url("https://images.unsplash.com/photo-1581090700227-1e8cfe4c1d5a?auto=format&fit=crop&w=1350&q=80");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            font-family: 'Poppins', sans-serif;
            color: white;
        }

        .title {
            text-align: center;
            font-size: 3rem;
            font-family: 'Orbitron', sans-serif;
            color: #00ffe7;
            margin-bottom: 0;
            text-shadow: 0 0 15px #00ffe7;
        }

        .subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: #cccccc;
            margin-top: 0;
        }

        .glass-box {
            background: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 0 20px rgba(0,255,231,0.3);
            backdrop-filter: blur(10px);
        }

        .price-text {
            font-size: 2rem;
            color: #00ffcc;
            text-align: center;
        }

        .updated-text {
            text-align: center;
            color: #aaa;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# 🔤 Title and Subtitle
st.markdown("<div class='title'>💹 Crypto Price Checker</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track live crypto prices in style 🚀</div>", unsafe_allow_html=True)

# 📥 User Input
crypto = st.text_input("🔍 Enter Cryptocurrency (e.g., bitcoin, ethereum):", "bitcoin").lower()

currency_map = {
    "INR": "Indian Rupee (₹)",
    "USD": "US Dollar ($)",
    "EUR": "Euro (€)",
    "JPY": "Japanese Yen (¥)",
    "GBP": "British Pound (£)",
    "CAD": "Canadian Dollar (C$)",
    "AUD": "Australian Dollar (A$)",
    "CHF": "Swiss Franc (Fr)",
    "SGD": "Singapore Dollar (S$)"
}

currency_display = list(currency_map.values())
selected_currency = st.selectbox("🌐 Select Currency:", currency_display)
currency_code = list(currency_map.keys())[currency_display.index(selected_currency)]

# 🔗 API Call
def get_price(crypto, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return data.get(crypto, {}).get(currency)
    except:
        return None

# 🚀 Check Price
if st.button("🚀 Get Price"):
    with st.spinner("Fetching price..."):
        price = get_price(crypto, currency_code.lower())
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if price:
            st.markdown(f"""
                <div class="glass-box">
                    <div class="price-text">✅ 1 {crypto.capitalize()} = {price} {currency_map[currency_code]}</div>
                    <div class="updated-text">📅 Last updated: {time_now}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Could not fetch price. Please check the coin name.")
