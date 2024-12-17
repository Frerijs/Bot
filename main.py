import streamlit as st
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

# Funkcija, lai iegūtu BTC cenu
def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
        return price
    else:
        return None

# Streamlit aplikācija
st.title("Bitcoin (BTC) pašreizējās cenas vizualizācija")
st.write("Šī aplikācija parāda BTC cenas izmaiņas reāllaikā USD.")

# Iestatījumi
refresh_rate = st.sidebar.slider("Atjaunināšanas intervāls (sekundēs):", 1, 60, 5)
max_points = st.sidebar.number_input("Datu punktu skaits:", 10, 500, 50)

# Sākuma vērtības
prices = []
timestamps = []

# Galvenā cilpa datu atjaunināšanai
placeholder = st.empty()
progress_bar = st.progress(0)

for i in range(max_points):
    price = get_btc_price()
    if price is not None:
        current_time = pd.Timestamp.now()
        prices.append(price)
        timestamps.append(current_time)
        
        # Ierobežo punktu skaitu
        if len(prices) > max_points:
            prices.pop(0)
            timestamps.pop(0)
        
        # Datu vizualizācija
        data = pd.DataFrame({"Laiks": timestamps, "Cena (USD)": prices})
        placeholder.line_chart(data.set_index("Laiks"))
        
        progress_bar.progress((i + 1) / max_points)
        time.sleep(refresh_rate)
    else:
        st.error("Neizdevās iegūt BTC cenu. Pārbaudi internetu un API statusu.")
        break

st.success("Datu apstrāde pabeigta!")