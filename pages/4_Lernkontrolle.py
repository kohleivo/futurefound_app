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

# Session-State initialisieren
if "abgegeben" not in st.session_state:
    st.session_state["abgegeben"] = False
if "feedback" not in st.session_state:
    st.session_state["feedback"] = None
if "auswahl" not in st.session_state:
    st.session_state["auswahl"] = antworten[0]  # Default-Auswahl

def reset_lernkontrolle():
    st.session_state["abgegeben"] = False
    st.session_state["feedback"] = None
    st.session_state["auswahl"] = antworten[0]

# Radio-Button für die Auswahl
auswahl = st.radio(
    "Wähle die richtige Antwort:",
    antworten,
    key="auswahl",
    disabled=st.session_state["abgegeben"]
)

# "Abgabe"-Button nur anzeigen, wenn noch nicht abgegeben wurde
if not st.session_state["abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["abgegeben"] = True
        if antworten.index(st.session_state["auswahl"]) == richtige_antwort:
            st.session_state["feedback"] = "richtig"
        else:
            st.session_state["feedback"] = "falsch"

# Feedback und "Wiederholen"/"Weiter"-Button
if st.session_state["abgegeben"]:
    if st.session_state["feedback"] == "richtig":
        st.success("✅ Richtig! Lean Startup bedeutet, schnell zu lernen.")
        if st.button("Weiter"):
            # Hier ggf. auf die nächste Seite springen
            st.switch_page("pages/5_NaechstesKapitel.py")
    else:
        st.error("❌ Fast! Denk nochmal an das Build-Measure-Learn-Prinzip.")
        if st.button("Wiederholen"):
            reset_lernkontrolle()
