import streamlit as st

st.markdown("""
    <style>
    /* Minimalistischer, professioneller Hintergrund */
    .stApp {
        background: linear-gradient(135deg, #e9ecef 0%, #cfd8dc 100%) !important;
    }
    /* Überschrift */
    .main-title {
        font-size: 2.1em;
        font-weight: bold;
        color: #222831;
        margin-bottom: 0.2em;
        letter-spacing: 1px;
    }
    .subtitle {
        color: #393e46;
        font-size: 1.18em;
        margin-bottom: 1.4em;
    }
    /* Weiße Trennlinie wie in page3 */
    .white-divider {
        height: 2.5px;
        width: 100%;
        background: #fff;
        margin: 32px 0 28px 0;
        border: none;
        border-radius: 2px;
        box-shadow: 0 1px 4px #0001;
    }
    /* Button clean und dezent */
    .stButton > button {
        background: #007bff;
        color: #fff;
        border: none;
        border-radius: 8px;
        font-size: 1.07em;
        font-weight: 500;
        padding: 0.5em 2em;
        margin-top: 1.1em;
        margin-bottom: 0.6em;
        box-shadow: 0 2px 8px #007bff22;
        transition: 0.18s;
    }
    .stButton > button:hover {
        background: #0056b3;
        color: #fff;
        transform: translateY(-2px) scale(1.03);
        box-shadow: 0 4px 16px #007bff33;
    }
    /* Radio-Button Text */
    .stRadio label {
        font-size: 1.09em !important;
        color: #222831 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎯 Lernkontrolle, Kapitel 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Was beschreibt den Kern des Lean-Startup-Ansatzes?</div>', unsafe_allow_html=True)

# Weiße Trennlinie wie in page3
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

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
