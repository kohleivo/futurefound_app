import streamlit as st

st.title("Lernkontrolle, Kapitel 1")
st.subheader("Was beschreibt den Kern des Lean-Startup-Ansatzes?")

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
            st.info("🔄 Gleich geht's weiter! Die Frage wird jetzt neu geladen ...")
