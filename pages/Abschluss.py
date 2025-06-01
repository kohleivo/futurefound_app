import streamlit as st

# --- Stil und Abschlussbox ---
st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; margin-bottom: 0.3em;}
    .subtitle { color: #d9e0e7; font-size: 1.18em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .outro-box { background: #393e46; color: #fff; border-radius: 14px; padding: 1.3em 1.6em; margin: 1.6em 0 1.6em 0; border-left: 7px solid #00adb5; font-size: 1.12em; }
    .congrats-box { background: #eafff3; color: #23272f; border-radius: 14px; padding: 1.3em 1.6em; margin: 1.6em 0 1.6em 0; border-left: 7px solid #00c897; font-size: 1.18em; font-weight: bold;}
    .voiceover { font-style: italic; color: #bfc9d1; font-size: 1.05em; margin: 1.1em 0 1.1em 0;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Mission erfüllt!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Was du aus Lean Startup mitnimmst</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# --- Zusammenfassungstext ---
st.markdown(
    '<div class="outro-box">'
    'Du hast gelernt, wie du den <b>Build-Measure-Learn-Zyklus</b> im täglichen Geschäftsumfeld von Startups anwenden kannst. '
    'Indem du Entscheidungen schnell triffst und iterativ vorgehst, kannst du schneller validieren, was wirklich funktioniert, '
    'und unnötige Risiken und Ressourcenverschwendung vermeiden. Du hast gesehen, wie wichtig es ist, in kleinen Schritten zu denken '
    'und immer weiter zu testen, zu messen und daraus zu lernen.'
    '</div>',
    unsafe_allow_html=True
)

# --- Video (25 Sekunden) ---
st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
with open("video 4.mp4", "rb") as video_file:  # Passe ggf. den Dateinamen an
    st.video(video_file.read())
st.markdown('</div>', unsafe_allow_html=True)

# --- Glückwunsch-Box ---
st.markdown(
    '<div class="congrats-box">'
    '🎉 Mission erfüllt: Du hast gelernt, was Lean Startup bedeutet – und es direkt angewendet. <br> <br>'
    'Glückwunsch!'
    '</div>',
    unsafe_allow_html=True
)

# --- Abschluss-Navigation ---
st.markdown("<div style='height: 44px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 6, 1], gap="small")
with col3:
    if st.button("Fertig!"):
        st.switch_page("streamlit_app.py")
