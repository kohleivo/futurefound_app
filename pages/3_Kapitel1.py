import streamlit as st

# Session-State für Reset beim Seitenaufruf
if "kapitel1_visited" not in st.session_state:
    for idx in range(4):
        st.session_state[f"tile_{idx}_clicked"] = False
    st.session_state["kapitel1_visited"] = True

st.title("Was ist eigentlich «Lean Startup»?")
st.header("Du verstehst, was Lean Startup bedeutet – und was es nicht ist.")

# Video zentriert anzeigen
st.markdown('<div class="video-container">', unsafe_allow_html=True)
with open("video 2.mp4", "rb") as video_file:
    st.video(video_file.read())
st.markdown('</div>', unsafe_allow_html=True)

st.subheader("Lean Startup ist NICHT…")

tiles = [
    {"title": "Ein Startup ohne Geld", "info": "Lean hat nichts mit wenig Geld zu tun, sondern mit schnellem Lernen.", "icon": "💸"},
    {"title": "Nur für Tech-Startups", "info": "Funktioniert branchenunabhängig.", "icon": "🏭"},
    {"title": "Ein festes Rezept", "info": "Es geht um Experimente, nicht um einen starren Plan.", "icon": "🧪"},
    {"title": "Nur was für Anfänger", "info": "Auch Konzerne nutzen es für neue Projekte", "icon": "🏢"}
]

st.markdown("""
    <style>
    .white-divider {
        height: 2px;
        width: 100%;
        background: #fff;
        margin: 28px 0 18px 0;
        border: none;
        border-radius: 2px;
        box-shadow: 0 1px 4px #0001;
    }
    .tile-title {
        font-size: 1.1em;
        font-weight: bold;
        margin-bottom: 0.2em;
        color: #fff !important;
    }
    .tile-icon {
        font-size: 1.6em;
        margin-right: 0.5em;
        vertical-align: middle;
    }
    </style>
""", unsafe_allow_html=True)

for idx, tile in enumerate(tiles):
    if idx > 0:
        st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)
    key = f"tile_{idx}_clicked"
    st.markdown(
        f'<span class="tile-icon">{tile["icon"]}</span>'
        f'<span class="tile-title">{tile["title"]}</span>',
        unsafe_allow_html=True
    )
    if st.button("Mehr erfahren", key=f"button_{idx}"):
        st.session_state[key] = True
    if st.session_state[key]:
        st.info(tile["info"])

# Navigation: Session-State für diese Seite zurücksetzen beim Seitenwechsel
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Zurück", key="zurueck"):
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/2_Mission.py")
with col2:
    if st.button("Weiter", key="weiter"):
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/4_Lernkontrolle.py")
