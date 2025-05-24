import streamlit as st

st.title("Mission")
st.write("Video 1:")

# Beispiel: Lokale Videodatei oder YouTube-Link
# Für YouTube-Link z.B.: st.video("https://www.youtube.com/watch?v=dein_video")
st.video("https://www.youtube.com/watch?v=dein_video")  # Ersetze den Link durch dein Video

if st.button("Mission Starten"):
    st.success("Mission gestartet! Navigiere weiter zum nächsten Kapitel.")
