import streamlit as st

# Stil-Optimierung mit CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #222831;
        color: #EEEEEE;
        font-family: 'Segoe UI', sans-serif;
    }
    .video-container {
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
    }
    .button-row {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        width: 100%;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .button-row button {
        min-width: 120px;
        font-size: 1rem;
        padding: 0.5rem 1.5rem;
        border-radius: 8px;
        border: none;
        background: #393E46;
        color: #EEEEEE;
        transition: background 0.2s;
    }
    .button-row button:hover {
        background: #00ADB5;
        color: #222831;
    }
    @media (max-width: 600px) {
        .button-row {
            flex-direction: row;
            gap: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.title("Mission")
st.markdown("**Video 2:**")

# Video zentriert anzeigen
st.markdown('<div class="video-container">', unsafe_allow_html=True)
with open("video 2.mp4", "rb") as video_file:
    st.video(video_file.read())
st.markdown('</div>', unsafe_allow_html=True)

# Buttons unter dem Video, links und rechts
st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Zurück", key="zurueck"):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("Weiter", key="weiter"):
        st.switch_page("pages/3_Kapitel1.py")
st.markdown('</div>', unsafe_allow_html=True)
