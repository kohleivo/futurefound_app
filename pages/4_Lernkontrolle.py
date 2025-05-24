import streamlit as st

st.title("Lernkontrolle, Kapitel 1")
st.subheader("Was beschreibt den Kern des Lean-Startup-Ansatzes?")

antworten = [
    "Bitte auswählen...",
    "Mit möglichst wenig Geld ein Unternehmen gründen.",
    "Schnell zu lernen und das Geschäftsmodell anzupassen.",
    "Nur für Tech-Startups geeignet.",
    "Einen festen Plan verfolgen."
]
richtige_antwort = 2  # Index der richtigen Antwort

if "abgegeben" not in st.session_state:
    st.session_state["abgegeben"] = False
if "feedback" not in st.session_state:
    st.session_state["feedback"] = None

def abgabe_callback():
    st.session_state["abgegeben"] = True
    auswahl = st.session_state["lernkontrolle_radio"]
    if auswahl == antworten[richtige_antwort]:
        st.session_state["feedback"] = "richtig"
    else:
        st.session_state["feedback"] = "falsch"

def reset_lernkontrolle():
    st.session_state["abgegeben"] = False
    st.session_state["feedback"] = None

auswahl = st.radio(
    "Wähle die richtige Antwort:",
    antworten,
    index=0,
    key="lernkontrolle_radio",
    disabled=st.session_state["abgegeben"]
)

if not st.session_state["abgegeben"]:
    if auswahl != antworten[0]:
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
