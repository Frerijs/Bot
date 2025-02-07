import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# Funkcija, lai ģenerētu zvaigznes formu
def generate_star(points=5, inner_radius=0.5, outer_radius=1.0):
    angles = np.linspace(0, 2 * np.pi, points * 2, endpoint=False)
    radii = np.array([outer_radius if i % 2 == 0 else inner_radius for i in range(len(angles))])
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y

# Pilns zvaigžņu saraksts
star_list = [
    {"name": "Luminara", "power": "Dāvā sapņotājiem radošas idejas", "legend": "Teika vēsta, ka, ja ieraudzīsi šo zvaigzni, tev būs laimīgs mēnesis!"},
    {"name": "Celestara", "power": "Aizsargā pret sliktiem sapņiem", "legend": "Šī zvaigzne spīd tikai tiem, kas meklē patiesību."},
    {"name": "Orionis", "power": "Nes veiksmi ceļotājiem", "legend": "Senie astronomi uzskatīja, ka tā ir atslēga uz paralēlo dimensiju."},
    {"name": "Mystara", "power": "Piešķir spēku un izturību", "legend": "Leģenda vēsta, ka tā ir nokritusi no dievu vainaga."},
    {"name": "Astraeus", "power": "Sniedz mieru un harmoniju", "legend": "Ja vēlēsies zem šīs zvaigznes, tava vēlēšanās piepildīsies!"},
    {"name": "Vespera", "power": "Palīdz atrast ceļu dzīvē", "legend": "Zvaigzne, kas parādās tikai tiem, kas seko savam liktenim."},
    {"name": "Zyphron", "power": "Dod gudrību un zināšanas", "legend": "Senās kultūras uzskatīja, ka tā ir vārti uz zināšanu valstību."},
    {"name": "Novaeus", "power": "Iespējams, tā ir ceļš uz citu dimensiju", "legend": "Tie, kas to redz, piedzīvo neizskaidrojamus sapņus."},
    {"name": "Sirioth", "power": "Pievelk labas enerģijas", "legend": "Zvaigzne, kas pasargā no ļaunām domām un sliktiem nodomiem."}
]

# Streamlit lietotnes sākums
st.title("✨ Maģiskā Zvaigžņu Ģenerators ✨")
st.write("Spied pogu un izveido savu unikālo maģisko zvaigzni!")

if st.button("🌟 Ģenerēt maģisko zvaigzni!"):
    # Izvēlamies nejaušu zvaigzni no saraksta
    selected_star = random.choice(star_list)

    # Nejauša zvaigznes parametru izvēle
    num_points = random.choice([5, 6, 7, 8])  
    inner_radius = random.uniform(0.3, 0.6)   
    outer_radius = random.uniform(0.8, 1.2)   

    # Ģenerējam zvaigznes formu
    x, y = generate_star(num_points, inner_radius, outer_radius)

    # Nejauša krāsa un fons
    colors = ["gold", "deepskyblue", "purple", "magenta", "red", "lime"]
    backgrounds = ["black", "navy", "darkred", "darkgreen"]
    star_color = random.choice(colors)
    bg_color = random.choice(backgrounds)

    # Zīmējam zvaigzni
    fig, ax = plt.subplots(figsize=(5,5))
    ax.fill(x, y, color=star_color, edgecolor="white", linewidth=2)
    ax.set_facecolor(bg_color)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Saglabājam attēlu
    star_image_path = "magical_star.png"
    plt.savefig(star_image_path, bbox_inches='tight', facecolor=bg_color)
    st.image(star_image_path, caption=f"Tava maģiskā zvaigzne: {selected_star['name']}")

    # Parādām leģendu
    st.subheader(f"🔮 Maģiskā Zvaigzne: {selected_star['name']}")
    st.markdown(f"🌟 **Forma:** {num_points}-punktu zvaigzne  \n"
                f"🎨 **Krāsa:** {star_color}  \n"
                f"🔮 **Maģija:** {selected_star['power']}  \n"
                f"📜 **Leģenda:** {selected_star['legend']}")

st.write("Izmēģini vēlreiz, lai atrastu savu īsto maģisko zvaigzni! 🌠")