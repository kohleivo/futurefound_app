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

if "selected_tile" not in st.session_state:
    st.session_state["selected_tile"] = None

for idx, tile in enumerate(tiles):
    if st.button(f"{tile['icon']} {tile['title']}", key=tile['title']):
        st.session_state["selected_tile"] = idx
    if st.session_state["selected_tile"] == idx:
        st.info(tile["info"])

# Buttons vor und zurück
st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Zurück", key="zurueck"):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("Weiter", key="weiter"):
        st.switch_page("pages/3_Kapitel1.py")
st.markdown('</div>', unsafe_allow_html=True)
