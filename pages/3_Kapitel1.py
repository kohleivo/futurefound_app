import streamlit as st

# Session-State für Reset beim Seitenaufruf
if "kapitel1_visited" not in st.session_state:
    # Beim ersten Laden: alle Infotexte ausblenden
    for idx in range(4):
        st.session_state[f"tile_{idx}_clicked"] = False
    st.session_state["kapitel1_visited"] = True

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

st.markdown("""
    <style>
    .tile-box {
        border: 2px solid #00ADB5;
        border-radius: 12px;
        padding: 1.2em 1em 1em 1em;
        margin-bottom: 1.3em;
        background: #f8f9fa;
        box-shadow: 0 2px 8px #0001;
    }
    .tile-title {
        font-size: 1.1em;
        font-weight: bold;
        margin-bottom: 0.2em;
        color: #222831;
    }
    .tile-icon {
        font-size: 1.6em;
        margin-right: 0.5em;
        vertical-align: middle;
    }
    </style>
""", unsafe_allow_html=True)

for idx, tile in enumerate(tiles):
    key = f"tile_{idx}_clicked"
    st.markdown('<div class="tile-box">', unsafe_allow_html=True)
    st.markdown(
        f'<span class="tile-icon">{tile["icon"]}</span>'
        f'<span class="tile-title">{tile["title"]}</span>',
        unsafe_allow_html=True
    )
    if st.button("Mehr erfahren", key=f"button_{idx}"):
        st.session_state[key] = True
    if st.session_state[key]:
        st.info(tile["info"])
    st.markdown('</div>', unsafe_allow_html=True)

# Navigation: Session-State für diese Seite zurücksetzen beim Seitenwechsel
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Zurück", key="zurueck"):
        # Reset aller Infotexte beim Verlassen der Seite
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/2_Mission.py")
with col2:
    if st.button("Weiter", key="weiter"):
        # Reset aller Infotexte beim Verlassen der Seite
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/4_Lernkontrolle.py")
