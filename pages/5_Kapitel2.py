import streamlit as st

# --- Stil und Schrittzähler ---
st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.18em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .stepper-wrap { display: flex; justify-content: center; align-items: center; margin: 1.2em 0 2em 0; }
    .stepper-ball { width: 32px; height: 32px; border-radius: 50%; background: #393e46; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.15em; margin: 0 8px; border: 2.5px solid #393e46; transition: background 0.2s, color 0.2s; }
    .stepper-ball.active { background: #00adb5; color: #23272f; border: 2.5px solid #fff; box-shadow: 0 0 0 4px #00adb522; }
    .stepper-ball.done { background: linear-gradient(135deg, #00adb5 70%, #393e46 100%); color: #fff; border: 2.5px solid #00adb5; }
    .stepper-bar { flex: 1; height: 6px; background: #393e46; border-radius: 3px; margin: 0 3px; position: relative; min-width: 28px; max-width: 70px; }
    .stepper-bar-fill { height: 100%; background: #00adb5; border-radius: 3px; position: absolute; left: 0; top: 0; transition: width 0.3s; }
    </style>
""", unsafe_allow_html=True)

def stepper(current, total):
    balls = []
    for i in range(total):
        ball_class = "stepper-ball"
        if i < current:
            ball_class += " done"
        elif i == current:
            ball_class += " active"
        balls.append(f'<div class="{ball_class}">{i+1}</div>')
    bars = []
    for i in range(total-1):
        fill = "100%" if i < current else "0%"
        bars.append(f'<div class="stepper-bar"><div class="stepper-bar-fill" style="width:{fill};"></div></div>')
    html = '<div class="stepper-wrap">'
    for i in range(total):
        html += balls[i]
        if i < total-1:
            html += bars[i]
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

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
    {
        "frage": "Was ist ein MVP (Minimum Viable Product)?",
        "antworten": [
            "Ein Produkt mit allen Features.",
            "Die minimal funktionsfähige Version, um Annahmen zu testen.",
            "Ein Produkt, das nur intern genutzt wird.",
            "Ein Produkt, das sofort an alle verkauft wird."
        ],
        "richtig": 1,
        "feedback_richtig": "✅ Richtig! Ein MVP ist die einfachste Version, um schnell zu testen.",
        "feedback_falsch": "❌ Das ist nicht korrekt. Überleg nochmal, was ein MVP leisten soll."
    }
    # Du kannst beliebig weitere Fragen ergänzen!
]

# --- Session State ---
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
    st.experimental_rerun()  # Seite sofort neu laden, Button verschwindet direkt

def reset_lernkontrolle():
    st.session_state["reset_pending"] = True

# Sofortiger Reset beim nächsten Rendern nach dem ersten Klick auf "Wiederholen"
if st.session_state["reset_pending"]:
    st.session_state["abgegeben"] = False
    st.session_state["feedback"] = None
    st.session_state["radio_key"] += 1
    st.session_state["reset_pending"] = False

# --- Fehlerbehandlung für Index ---
aktuelle_frage = min(st.session_state["frage_idx"], len(fragen)-1)
gesamt_fragen = len(fragen)

# --- Titel, Stepper, Divider ---
st.markdown('<div class="main-title">Lernkontrolle, Kapitel 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Teste dein Wissen zum Lean-Startup-Ansatz!</div>', unsafe_allow_html=True)
stepper(aktuelle_frage, gesamt_fragen)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# --- Frage anzeigen ---
frage = fragen[aktuelle_frage]
st.markdown(f"<b>{frage['frage']}</b>", unsafe_allow_html=True)

auswahl = st.radio(
    "Wähle die richtige Antwort:",
    frage["antworten"],
    key=f"lernkontrolle_radio_{st.session_state['radio_key']}",
    disabled=st.session_state["abgegeben"]
)

if not st.session_state["abgegeben"]:
    st.button("Abgabe", on_click=abgabe_callback)

if st.session_state["abgegeben"]:
    if st.session_state["feedback"] == "richtig":
        st.success(frage["feedback_richtig"])
        if aktuelle_frage < gesamt_fragen-1:
            if st.button("Weiter"):
                st.session_state["frage_idx"] += 1
                st.session_state["abgegeben"] = False
                st.session_state["feedback"] = None
                st.session_state["radio_key"] += 1
        else:
            if st.button("Zurück zur Übersicht"):
                st.session_state["frage_idx"] = 0
                st.session_state["abgegeben"] = False
                st.session_state["feedback"] = None
                st.session_state["radio_key"] += 1
                st.switch_page("pages/6_Kapitelübersicht.py")
    else:
        st.error(frage["feedback_falsch"])
        if st.button("Wiederholen"):
            reset_lernkontrolle()
            st.info("🔄 Gleich geht's weiter! Die Frage wird jetzt neu geladen ...")
