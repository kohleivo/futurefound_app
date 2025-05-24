import streamlit as st

# --- Stil für dunklen Hintergrund, Trennlinie und Button ---
st.markdown("""
    <style>
    .stApp {
        background: #23272f !important;
    }
    .main-title {
        font-size: 2.1em;
        font-weight: bold;
        color: #fff;
        margin-bottom: 0.2em;
        letter-spacing: 1px;
        text-align: center;
    }
    .subtitle {
        color: #d9e0e7;
        font-size: 1.18em;
        margin-bottom: 1.4em;
        text-align: center;
    }
    .white-divider {
        height: 2.5px;
        width: 100%;
        background: #fff;
        margin: 32px 0 28px 0;
        border: none;
        border-radius: 2px;
        box-shadow: 0 1px 4px #0001;
    }
    .emoji-question {
        font-size: 2.2em;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .stButton > button {
        background: #393e46;
        color: #fff;
        border: none;
        border-radius: 8px;
        font-size: 1.07em;
        font-weight: 500;
        padding: 0.5em 2em;
        margin-top: 1.1em;
        margin-bottom: 0.6em;
        box-shadow: 0 2px 8px #22283133;
        transition: 0.18s;
    }
    .stButton > button:hover {
        background: #00adb5;
        color: #fff;
        transform: translateY(-2px) scale(1.03);
        box-shadow: 0 4px 16px #00adb533;
    }
    .stRadio label {
        font-size: 1.09em !important;
        color: #e9ecef !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎯 Lernkontrolle, Kapitel 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Was beschreibt den Kern des Lean-Startup-Ansatzes?</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="emoji-question">🤔</div>', unsafe_allow_html=True)

antworten = [
    "Mit möglichst wenig Geld ein Unternehmen gründen.",
    "Schnell zu lernen und das Geschäftsmodell anzupassen.",
    "Nur für Tech-Startups geeignet.",
    "Einen festen Plan verfolgen."
]
richtige_antwort = 1

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

auswahl = st.radio(
    "Wähle die richtige Antwort:",
    antworten,
    key=f"lernkontrolle_radio_{st.session_state['radio_key']}",
    disabled=st.session_state["abgegeben"]
)

if not st.session_state["abgegeben"]:
    st.button("Abgabe", on_click=abgabe_callback)

if st.session_state["abgegeben"]:
    if st.session_state["feedback"] == "richtig":
        st.success("✅ Richtig! Lean Startup bedeutet, schnell zu lernen.")
        if st.button("Weiter"):
            st.switch_page("pages/5_NaechstesKapitel.py")
    else:
        st.error("❌ Fast! Denk nochmal an das Build-Measure-Learn-Prinzip.")
        if st.button("Wiederholen"):
            reset_lernkontrolle()
