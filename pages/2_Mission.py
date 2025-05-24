import streamlit as st

# Zustand initialisieren
if "mission_gestartet" not in st.session_state:
    st.session_state["mission_gestartet"] = False

st.title("Mission")
st.write("Video 1:")

video_file = open("video 2.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Button-Callback-Funktion
def mission_starten():
    st.session_state["mission_gestartet"] = True

# "Mission Starten"-Button, nur anzeigen, wenn Mission noch nicht gestartet
if not st.session_state["mission_gestartet"]:
    st.button("Mission Starten", on_click=mission_starten)

# "Weiter" und "Zurück"-Buttons nur anzeigen, wenn Mission gestartet wurde
if st.session_state["mission_gestartet"]:
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Zurück"):
            st.switch_page("streamlit_app.py")
    with col2:
        if st.button("Weiter"):
            st.switch_page("pages/3_Kapitel1.py")
