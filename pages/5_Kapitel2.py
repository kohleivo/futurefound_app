import streamlit as st

# ... (CSS und stepper wie gehabt)

# --- Fragen, Antworten und Feedback wie im Original ---
fragen = [
    {
        "frage": "Was beschreibt den Kern des Lean-Startup-Ansatzes?",
        "antworten": [
            "Mit möglichst wenig Geld ein Unternehmen gründen.",
            "Schnell zu lernen und das Geschäftsmodell anzupassen.",
            "Nur für Tech-Startups geeignet.",
            "Einen festen Plan verfolgen."
        ],
        "richtig": 1,
        "feedback_richtig": "✅ Richtig! Lean Startup bedeutet, schnell zu lernen.",
        "feedback_falsch": "❌ Fast! Denk nochmal an das Build-Measure-Learn-Prinzip."
    },
    # ...weitere Fragen...
]

if "radio_key" not in st.session_state:
    st.session_state["radio_key"] = 0
if "abgegeben" not in st.session_state:
    st.session_state["abgegeben"] = False
if "feedback" not in st.session_state:
    st.session_state["feedback"] = None
if "reset_pending" not in st.session_state:
    st.session_state["reset_pending"] = False
if "frage_idx" not in st.session_state:
    st.session_state["frage_idx"] = 0

def abgabe_callback():
    st.session_state["abgegeben"] = True
    frage = fragen[st.session_state["frage_idx"]]
    auswahl = st.session_state[f"lernkontrolle_radio_{st.session_state['radio_key']}"]
    if frage["antworten"].index(auswahl) == frage["richtig"]:
        st.session_state["feedback"] = "richtig"
    else:
        st.session_state["feedback"] = "falsch"

def reset_lernkontrolle():
    st.session_state["reset_pending"] = True

if st.session_state["reset_pending"]:
    st.session_state["abgegeben"] = False
    st.session_state["feedback"] = None
    st.session_state["radio_key"] += 1
    st.session_state["reset_pending"] = False

aktuelle_frage = min(st.session_state["frage_idx"], len(fragen)-1)
gesamt_fragen = len(fragen)

st.markdown('<div class="main-title">Lernkontrolle, Kapitel 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Teste dein Wissen zum Lean-Startup-Ansatz!</div>', unsafe_allow_html=True)
stepper(aktuelle_frage, gesamt_fragen)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

frage = fragen[aktuelle_frage]
st.markdown(f"<b>{frage['frage']}</b>", unsafe_allow_html=True)

auswahl = st.radio(
    "Wähle die richtige Antwort:",
    frage["antworten"],
    key=f"lernkontrolle_radio_{st.session_state['radio_key']}",
