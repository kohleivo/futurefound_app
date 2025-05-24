import streamlit as st

st.set_page_config(page_title="FutureFound App", page_icon="🚀")

# Seite 1
st.title("Willkommen!")
st.write("""
Du bist Business Consultant, Spezialistin für smarte Startups (also, fast… jedenfalls behauptet das dein LinkedIn-Profil).
Eines Tages bekommst du eine Nachricht vom kleinen, innovativen Startup FutureFound, das kurz vor dem Aus steht.
""")
if st.button("Weiter"):
    st.switch_page("pages/2_Mission.py")
