import streamlit as st

st.title("Mission")
st.write("Video 2:")

video_file = open("video 2.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

col1, col2 = st.columns([1,1])

with col1:
    if st.button("Zurück"):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("Weiter"):
        st.switch_page("pages/3_Kapitel1.py")
