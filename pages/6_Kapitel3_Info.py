import streamlit as st

# Session-State für Reset beim Seitenaufruf
if "kapitel1_visited" not in st.session_state:
    for idx in range(4):
        st.session_state[f"tile_{idx}_clicked"] = False
    st.session_state["kapitel1_visited"] = True

st.title("Startup Lean-Up! Vom Produkt zur validierten Problemhypothese")
st.markdown('<div class="subtitle">Lernziel: Du lernst warum es entscheidend ist, zuerst das Problem zu verstehen – nicht das Produkt zu bauen.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="info-text">'
    'Viele Startups scheitern nicht an der Technologie – sondern daran, dass sie ein Produkt für ein Problem entwickeln, das niemand hat. Lean Startup kehrt diese Logik um:'
    '</div>',
    unsafe_allow_html=True
)

# --- Szenario-Box (neu hinzugefügt, fett für die letzte Zeile) ---
st.markdown("""
    <style>
    .szenario-box {
        background: #393e46;
        color: #fff;
        border-radius: 12px;
        padding: 1.1em 1.4em;
        margin: 1.3em 0 1.3em 0;
        border-left: 6px solid #00adb5;
        font-size: 1.05em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="szenario-box">'
    'Viele Startups scheitern nicht an der Technologie – sondern daran, dass sie ein Produkt für ein Problem entwickeln, das niemand hat.<br>'
    '<b>Lean Startup kehrt diese Logik um:</b><br>'
    '<b>Nicht zuerst entwickeln – sondern zuerst verstehen.</b>'
    '</div>',
    unsafe_allow_html=True
)

# --- YouTube-Video (nur von 0:00 bis 2:40 abspielbar) ---
youtube_id = "dQw4w9WgXcQ"  # Ersetze durch die ID deines Videos!
start_seconds = 0
end_seconds = 160  # 2 Minuten 40 Sekunden

embed_url = f"https://www.youtube.com/embed/wXc-SWqBnKc?start=0&end=160&controls=1"

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <iframe width="700" height="394"
        src="{embed_url}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

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

# --- Vertikaler Abstand vor den Buttons ---
st.markdown("<div style='height: 44px;'></div>", unsafe_allow_html=True)

# --- Navigation mit drei Spalten, Buttons links/rechts ---
col1, col2, col3 = st.columns([1, 6, 1], gap="small")

with col1:
    if st.button("Zurück", key="zurueck"):
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("streamlit_app.py")
with col3:
    if st.button("Weiter", key="weiter"):
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/3_Kapitel1_Lernkontrolle.py")
