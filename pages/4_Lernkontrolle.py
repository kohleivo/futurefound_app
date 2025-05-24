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
if "reset_flag" not in st.session_state:
    st.session_state["reset_flag"] = False

# Nach Klick auf "Wiederholen" wird im nächsten Durchlauf alles zurückgesetzt
if st.session_state["reset_flag"]:
    st.session_state["abgegeben"] = False
    st.session_state["feedback"] = None
    st.session_state["radio_key"] += 1
    st.session_state["reset_flag"] = False

auswahl = st.radio(
    "Wähle die richtige Antwort:",
    antworten,
    key=f"lernkontrolle_radio_{st.session_state['radio_key']}",
    disabled=st.session_state["abgegeben"]
)

if not st.session_state["abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["abgegeben"] = True
        if antworten.index(auswahl) == richtige_antwort:
            st.session_state["feedback"] = "richtig"
        else:
            st.session_state["feedback"] = "falsch"

if st.session_state["abgegeben"]:
    if st.session_state["feedback"] == "richtig":
        st.success("✅ Richtig! Lean Startup bedeutet, schnell zu lernen.")
        if st.button("Weiter"):
            st.switch_page("pages/5_NaechstesKapitel.py")
    else:
        st.error("❌ Fast! Denk nochmal an das Build-Measure-Learn-Prinzip.")
        if st.button("Wiederholen"):
            st.session_state["reset_flag"] = True
