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

# Session-State für Reset beim Seitenaufruf
if "kapitel1_visited" not in st.session_state:
    for idx in range(len(tiles)):
        st.session_state[f"tile_{idx}_clicked"] = False
    st.session_state["kapitel1_visited"] = True

# Stil für die Kacheln
st.markdown("""
    <style>
    .tile-container {
        background: #fff;
        border-radius: 18px;
        box-shadow: 0 4px 16px #0001;
        padding: 1.3em 1.2em 1.2em 1.2em;
        margin-bottom: 1.7em;
        min-height: 90px;
        max-width: 540px;
        margin-left: auto;
        margin-right: auto;
        transition: min-height 0.3s;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .tile-header {
        display: flex;
        align-items: center;
        font-size: 1.17em;
        font-weight: bold;
        margin-bottom: 0.7em;
        color: #222831;
    }
    .tile-icon {
        font-size: 2em;
        margin-right: 0.7em;
    }
    .tile-button {
        margin-bottom: 0.5em;
        width: fit-content;
    }
    .tile-info {
        margin-top: 0.7em;
        background: #e6f7fa;
        border-left: 4px solid #00ADB5;
        padding: 0.8em 1em;
        border-radius: 8px;
        color: #222831;
        font-size: 1em;
        font-weight: 400;
    }
    </style>
""", unsafe_allow_html=True)

for idx, tile in enumerate(tiles):
    key = f"tile_{idx}_clicked"
    st.markdown('<div class="tile-container">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="tile-header">'
        f'<span class="tile-icon">{tile["icon"]}</span>'
        f'{tile["title"]}'
        f'</div>',
        unsafe_allow_html=True
    )
    if st.button("Mehr erfahren", key=f"button_{idx}", help="Zeigt mehr Informationen an"):
        st.session_state[key] = True
    if st.session_state[key]:
        st.markdown(f'<div class="tile-info">{tile["info"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Navigation: Session-State für diese Seite zurücksetzen beim Seitenwechsel
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Zurück", key="zurueck"):
        for idx in range(len(tiles)):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/2_Mission.py")
with col2:
    if st.button("Weiter", key="weiter"):
        for idx in range(len(tiles)):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/4_Lernkontrolle.py")
