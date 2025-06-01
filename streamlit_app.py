import streamlit as st

st.set_page_config(page_title="FutureFound App", page_icon="🚀")

# Seite 1
st.title("Willkommen!")
st.write("""
Du bist Business Consultant, Spezialistin für smarte Startups (also, fast… jedenfalls behauptet das dein LinkedIn-Profil).
Eines Tages bekommst du eine Nachricht vom kleinen, innovativen Startup FutureFound, das kurz vor dem Aus steht.
""")
video_file = open("video 1.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

if st.button("Mission starten!"):
    st.switch_page("pages/1_Kapitel1_Info.py")
