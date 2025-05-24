import streamlit as st

st.title("Kapitel 1")
st.header("Einführung in Kapitel 1")

st.video("https://www.youtube.com/watch?v=dein_video2")  # Ersetze durch dein Video

st.subheader("Lernziel 1: Du verstehst, was Lean Startup bedeutet – und was es nicht ist.")

tiles = [
    {"title": "Ein Startup ohne Geld", "info": "Lean hat nichts mit wenig Geld zu tun, sondern mit schnellem Lernen.", "icon": "💸"},
    {"title": "Nur für Tech-Startups", "info": "Funktioniert branchenunabhängig.", "icon": "🏭"},
    {"title": "Ein festes Rezept", "info": "Es geht um Experimente, nicht um einen starren Plan.", "icon": "🧪"},
    {"title": "Nur was für Anfänger", "info": "Auch Konzerne nutzen es für neue Projekte", "icon": "🏢"}
]

# Session-State für jeden Button initialisieren
for idx in range(len(tiles)):
    key = f"tile_{idx}_clicked"
    if key not in st.session_state:
        st.session_state[key] = False

cols = st.columns(2)
for idx, tile in enumerate(tiles):
    with cols[idx % 2]:
        key = f"tile_{idx}_clicked"
        if not st.session_state[key]:
            if st.button(f"{tile['icon']} {tile['title']}", key=f"button_{idx}"):
                st.session_state[key] = True
        if st.session_state[key]:
            st.info(tile["info"])

# Buttons vor und zurück (links/rechts)
st.markdown("""
    <style>
    .button-row {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-top: 2rem;
        margin-bottom: 2rem;
        width: 100%;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Zurück", key="zurueck"):
        st.switch_page("pages/2_Mission.py")
with col2:
    if st.button("Weiter", key="weiter"):
        st.switch_page("pages/4_Lernkontrolle.py")
st.markdown('</div>', unsafe_allow_html=True)
