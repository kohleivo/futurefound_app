import streamlit as st

# --- Buntes CSS-Design ---
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(120deg, #00adb5 0%, #393e46 100%);
    }
    .main-title {
        font-size: 2.2em;
        font-weight: bold;
        color: #fff;
        margin-bottom: 0.2em;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #0005;
    }
    .subtitle {
        color: #f8f9fa;
        font-size: 1.25em;
        margin-bottom: 1.5em;
    }
    .question-box {
        background: #fff;
        border-radius: 18px;
        box-shadow: 0 4px 16px #00adb555;
        padding: 1.6em 1.2em 1.2em 1.2em;
        margin-bottom: 2em;
        border: 3px solid #00adb5;
        max-width: 580px;
        margin-left: auto;
        margin-right: auto;
        position: relative;
    }
    .question-emoji {
        font-size: 2.2em;
        position: absolute;
        right: 20px;
        top: 18px;
    }
    .radio label {
        font-size: 1.1em !important;
        color: #222831 !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00adb5 60%, #393e46 100%);
        color: #fff;
        border-radius: 12px;
        font-size: 1.1em;
        font-weight: bold;
        padding: 0.6em 1.5em;
        margin-top: 1em;
        margin-bottom: 0.5em;
        border: none;
        box-shadow: 0 2px 8px #00adb533;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #393e46 40%, #00adb5 100%);
        color: #fff;
        transform: scale(1.04);
    }
    .stRadio>div {
        margin-bottom: 0.7em;
    }
    .custom-info {
        background: #fbeee6;
        border-left: 6px solid #ffb300;
        color: #222831;
        border-radius: 10px;
        padding: 1em 1.2em;
        margin-top: 1.2em;
        font-size: 1.08em;
        font-weight: 500;
    }
    .success-box {
        background: #eafff3;
        border-left: 6px solid #00c897;
        color: #222831;
        border-radius: 10px;
        padding: 1em 1.2em;
        margin-top: 1.2em;
        font-size: 1.08em;
        font-weight: 500;
    }
    .error-box {
        background: #fff2f2;
        border-left: 6px solid #ff6363;
        color: #222831;
        border-radius: 10px;
        padding: 1em 1.2em;
        margin-top: 1.2em;
        font-size: 1.08em;
        font-weight: 500;
    }
    .motivation-bar {
        height: 18px;
        background: linear-gradient(90deg, #ffb300 0%, #00adb5 100%);
        border-radius: 9px;
        margin-bottom: 1.2em;
        box-shadow: 0 2px 8px #00adb522;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- Motivationsbalken ---
st.markdown('<div class="motivation-bar"></div>', unsafe_allow_html=True)

# --- Titel und Frage ---
st.markdown('<div class="main-title">🎯 Lernkontrolle, Kapitel 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Was beschreibt den Kern des Lean-Startup-Ansatzes?</div>', unsafe_allow_html=True)

antworten = [
    "Mit möglichst wenig Geld ein Unternehmen gründen.",
    "Schnell zu lernen und das Geschäftsmodell anzupassen.",
    "Nur für Tech-Startups geeignet.",
    "Einen festen Plan verfolgen."
]
richtige_antwort = 1  # Index der richtigen Antwort

if "radio_key" not in st.session_state:
    st.session_state["radio_key"] = 0
if "abgegeben" not in st.session_state:
    st.session_state["abgegeben"] = False
if "feedback" not in st.session_state:
    st.session_state["feedback"] = None
if "reset_pending" not in st.session_state:
    st.session_state["reset_pending"] = False

def abgabe_callback():
    st.session_state["abgegeben"] = True
    auswahl = st.session_state[f"lernkontrolle_radio_{st.session_state['radio_key']}"]
    if antworten.index(auswahl) == richtige_antwort:
        st.session_state["feedback"] = "richtig"
    else:
        st.session_state["feedback"] = "falsch"

def reset_lernkontrolle():
    st.session_state["reset_pending"] = True

# Sofortiger Reset beim nächsten Rendern nach dem ersten Klick auf "Wiederholen"
if st.session_state["reset_pending"]:
    st.session_state["abgegeben"] = False
    st.session_state["feedback"] = None
    st.session_state["radio_key"] += 1
    st.session_state["reset_pending"] = False

# --- Fragebox mit Emoji ---
st.markdown('<div class="question-box">', unsafe_allow_html=True)
st.markdown('<div class="question-emoji">🤔</div>', unsafe_allow_html=True)

auswahl = st.radio(
    "Wähle die richtige Antwort:",
    antworten,
    key=f"lernkontrolle_radio_{st.session_state['radio_key']}",
    disabled=st.session_state["abgegeben"]
)

# "Abgabe"-Button nur anzeigen, wenn noch nicht abgegeben wurde
if not st.session_state["abgegeben"]:
    st.button("Abgabe", on_click=abgabe_callback)

# Feedback und "Wiederholen"/"Weiter"-Button
if st.session_state["abgegeben"]:
    if st.session_state["feedback"] == "richtig":
        st.markdown('<div class="success-box">✅ Richtig! Lean Startup bedeutet, schnell zu lernen. <br>Du bist auf dem richtigen Weg! 🎉</div>', unsafe_allow_html=True)
        if st.button("Weiter"):
            st.switch_page("pages/5_NaechstesKapitel.py")
    else:
        st.markdown('<div class="error-box">❌ Fast! Denk nochmal an das <b>Build-Measure-Learn-Prinzip</b>.<br>Probier es gleich nochmal!</div>', unsafe_allow_html=True)
        if st.button("Wiederholen"):
            reset_lernkontrolle()
            st.markdown('<div class="custom-info">🔄 Gleich geht\'s weiter! Die Frage wird jetzt neu geladen ...</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
