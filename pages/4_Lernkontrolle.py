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

# Initialisierung des Session State
if "lernkontrolle_selected" not in st.session_state:
    st.session_state["lernkontrolle_selected"] = None
if "lernkontrolle_feedback" not in st.session_state:
    st.session_state["lernkontrolle_feedback"] = None
if "lernkontrolle_abgegeben" not in st.session_state:
    st.session_state["lernkontrolle_abgegeben"] = False

# Auswahlfeld
selected = st.radio(
    "Wähle die richtige Antwort:",
    antworten,
    index=st.session_state["lernkontrolle_selected"] if st.session_state["lernkontrolle_selected"] is not None else 0,
    key="lernkontrolle_radio"
)

# Abgabe-Button nur anzeigen, wenn noch nicht abgegeben
if not st.session_state["lernkontrolle_abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["lernkontrolle_selected"] = antworten.index(selected)
        st.session_state["lernkontrolle_abgegeben"] = True
        if st.session_state["lernkontrolle_selected"] == richtige_antwort:
            st.session_state["lernkontrolle_feedback"] = "richtig"
        else:
            st.session_state["lernkontrolle_feedback"] = "falsch"

# Feedback und Navigation
if st.session_state["lernkontrolle_abgegeben"]:
    if st.session_state["lernkontrolle_feedback"] == "richtig":
        st.success("✅ Richtig! Lean Startup bedeutet, schnell zu lernen.")
        if st.button("Weiter"):
            # Hier kannst du auf die nächste Seite springen
            st.switch_page("pages/5_NaechstesKapitel.py")
    else:
        st.error("❌ Fast! Denk nochmal an das Build-Measure-Learn-Prinzip.")
        # Wiederholen-Button anzeigen, Abgabe-Button ist jetzt ausgeblendet
        if st.button("Wiederholen"):
            st.session_state["lernkontrolle_selected"] = None
            st.session_state["lernkontrolle_feedback"] = None
            st.session_state["lernkontrolle_abgegeben"] = False
            # Optional: Radio-Button zurücksetzen
            st.experimental_rerun()
