import streamlit as st

st.title("Lernkontrolle, Kapitel 1")
st.subheader("Was beschreibt den Kern des Lean-Startup-Ansatzes?")

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
if "reset_count" not in st.session_state:
    st.session_state["reset_count"] = 0

def abgabe_callback():
    st.session_state["abgegeben"] = True
    auswahl = st.session_state[f"lernkontrolle_radio_{st.session_state['radio_key']}"]
    if antworten.index(auswahl) == richtige_antwort:
        st.session_state["feedback"] = "richtig"
    else:
        st.session_state["feedback"] = "falsch"

def reset_lernkontrolle():
    st.session_state["reset_count"] += 1
    if st.session_state["reset_count"] >= 2:
        st.session_state["abgegeben"] = False
        st.session_state["feedback"] = None
        st.session_state["radio_key"] += 1
        st.session_state["reset_count"] = 0

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
        if st.session_state["reset_count"] == 0:
            if st.button("Wiederholen"):
                reset_lernkontrolle()
            st.info("🔄 Bereit für einen Neustart? Drücke noch einmal auf 'Wiederholen', um die Frage komplett zurückzusetzen!")
        elif st.session_state["reset_count"] == 1:
            st.info("🚀 Super! Jetzt noch ein Klick auf 'Wiederholen' und du kannst neu starten!")
            if st.button("Wiederholen"):
                reset_lernkontrolle()
