import streamlit as st

st.title("Lernkontrolle, Kapitel 1")
st.write("Was ist das Ziel von Lean Startup?")

options = [
    "Mit möglichst wenig Geld ein Unternehmen gründen.",
    "Schnell lernen und das Geschäftsmodell anpassen.",
    "Nur für Tech-Startups geeignet.",
    "Einen festen Plan verfolgen."
]
correct = 1

if "answered" not in st.session_state:
    st.session_state["answered"] = False
    st.session_state["selected"] = None

selected = st.radio("Wähle die richtige Antwort:", options, key="selected")

if st.button("Abgabe") and not st.session_state["answered"]:
    if selected == options[correct]:
        st.success("Richtig!")
        st.session_state["answered"] = True
        if st.button("Weiter"):
            st.info("Das nächste Kapitel ist noch nicht implementiert.")
    else:
        st.error("Fast! – Denk nochmals nach.")
        if st.button("Wiederholen"):
            st.session_state["answered"] = False
            st.session_state["selected"] = None
