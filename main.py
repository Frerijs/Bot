import streamlit as st
import requests
import time

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
st.write("Šī aplikācija parāda BTC cenu reāllaikā USD.")

# Iestatījumi
refresh_rate = st.sidebar.slider("Atjaunināšanas intervāls (sekundēs):", 1, 60, 5)
max_updates = st.sidebar.number_input("Atjauninājumu skaits:", 5, 100, 20)

# Sākuma vērtības
placeholder = st.empty()
prices = []

# Cikls cenu atjaunošanai un rādīšanai kā teksts
for i in range(max_updates):
    price = get_btc_price()
    if price is not None:
        prices.append(price)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Izvadīt jaunāko cenu kā tekstu
        placeholder.markdown(f"""
            ## Pašreizējā BTC cena: **{price:.2f} USD**
            **Atjaunināts:** {current_time}
        """)
    else:
        st.error("Neizdevās iegūt BTC cenu. Pārbaudi interneta savienojumu vai API statusu.")
        break
    
    time.sleep(refresh_rate)

st.success("Datu atjaunināšana pabeigta!")