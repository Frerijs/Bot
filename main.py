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
st.title("Bitcoin (BTC) pašreizējās cenas vizualizācija ar 15 min grafiku")
st.write("Šī aplikācija parāda BTC cenu reāllaikā USD un 15 minūšu cenu izmaiņu grafiku.")

# Sānjoslas iestatījumi
refresh_rate = st.sidebar.slider("Atjaunināšanas intervāls (sekundēs):", 5, 60, 10)

# Sākuma vērtības
prices = []
timestamps = []

# Galvenais vizualizācijas cikls
placeholder_text = st.empty()
placeholder_chart = st.empty()
progress_bar = st.progress(0)

start_time = time.time()
while True:
    # Saņem BTC cenu
    price = get_btc_price()
    if price is not None:
        current_time = pd.Timestamp.now()
        prices.append(price)
        timestamps.append(current_time)

        # Ierobežo datus līdz pēdējām 15 minūtēm
        while timestamps and (current_time - timestamps[0]).seconds > 900:
            prices.pop(0)
            timestamps.pop(0)

        # Teksta atjaunināšana
        placeholder_text.markdown(f"""
            ## Pašreizējā BTC cena: **{price:.2f} USD**
            **Atjaunināts:** {current_time.strftime('%Y-%m-%d %H:%M:%S')}
        """)

        # 15 min grafika atjaunināšana
        if len(prices) > 1:
            data = pd.DataFrame({"Laiks": timestamps, "Cena (USD)": prices})
            placeholder_chart.line_chart(data.set_index("Laiks"))

    else:
        st.error("Neizdevās iegūt BTC cenu. Pārbaudi interneta savienojumu vai API statusu.")
        break

    # Atjaunināšanas pauze
    time.sleep(refresh_rate)

    # Iziet no cikla pēc 15 minūtēm
    if time.time() - start_time > 900:
        st.success("15 minūšu datu vizualizācija pabeigta!")
        break