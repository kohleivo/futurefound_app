import streamlit as st

# --- Stil und Schrittzähler ---
st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.18em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .stepper { display: flex; align-items: center; justify-content: center; margin-bottom: 1.2em; }
    .step { width: 30px; height: 30px; border-radius: 50%; background: #393e46; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 8px; border: 2.5px solid #00adb5; }
    .step.active { background: #00adb5; color: #23272f; border: 2.5px solid #fff; }
    .progress-bar-bg { width: 180px; height: 8px; background: #393e46; border-radius: 6px; margin: 0 10px; }
    .progress-bar-fg { height: 8px; background: #00adb5; border-radius: 6px; }
    .feedback-bubble { background: #fff; color: #23272f; border-radius: 16px; padding: 1em 1.1em; margin: 1.3em 0 1.3em 0; box-shadow: 0 2px 12px #00adb522; position: relative; max-width: 480px; }
    .avatar { position: absolute; left: -56px; top: 0; font-size: 2.5em; }
    </style>
""", unsafe_allow_html=True)

# --- Fragen und Feedback ---
fragen = [
    {
        "frage": "Wofür steht die Abkürzung BML im Lean-Startup-Ansatz?",
        "antworten": [
            "Brainstorm – Market – Launch",
            "Business – Model – Launch",
            "Budget – Marketing – Learning",
            "Build – Measure – Learn"
        ],
        "richtig": 3,
        "feedback_richtig": "GründerIn sagt: Genau! Build – Measure – Learn ist der Kern des Lean-Startup-Ansatzes.",
        "feedback_falsch": "GründerIn sagt: Das stimmt so nicht. Probier es nochmals!"
    },
    {
        "frage": "Was beschreibt den Lean-Ansatz im Sinne von Build – Measure – Learn (BML)?",
        "antworten": [
            "Möglichst günstig ein Produkt entwickeln und verkaufen",
            "Schnell ein vollständiges Produkt bauen und intensiv bewerben",
            "Ideen schrittweise testen, Daten sammeln und daraus lernen",
            "Einmal planen und dann konsequent umsetzen"
        ],
        "richtig": 2,
        "feedback_richtig": "GründerIn sagt: Genau! Schrittweises Testen und Lernen ist entscheidend.",
        "feedback_falsch": "GründerIn sagt: Nicht ganz. Denk an das Prinzip: Testen, messen, lernen!"
    },
    {
        "frage": "Wofür steht MVP (Minimum Viable Product ) im Lean-Startup-Kontext?",
        "antworten": [
            "Es handelt sich um das fertige, ausgereifte Produkt, das alle Features umfasst.",
            "Es ist das minimal funktionsfähige Produkt, um die wichtigsten Annahmen zu testen und Feedback zu erhalten.",
            "Es ist das teuerste und umfangreichste Produkt, das den gesamten Markt ansprechen soll.",
            "Es ist ein Prototyp, der nur intern verwendet wird, um technische Lösungen zu validieren."
        ],
        "richtig": 1,
        "feedback_richtig": "GründerIn sagt: Richtig! Ein MVP ist die einfachste Version, um schnell zu testen.",
        "feedback_falsch": "GründerIn sagt: Das ist nicht korrekt. Überleg nochmal, was ein MVP leisten soll."
    },
    {
        "frage": "Wie reagierst du in unserem Beispiel?",
        "antworten": [
            "Neues Feature entwickeln",
            "NutzerInnen interviewen",
            "Mehr Werbung schalten",
            "Das Produkt einstellen"
        ],
        "richtig": 1,
        "feedback_richtig": "GründerIn sagt: Ah, wir müssen also rausfinden, was unsere User wirklich brauchen!",
        "feedback_falsch": "GründerIn sagt: Das macht wenig Sinn, probiere es nochmals!"
    }
]

# --- Session State für Quiz ---
if "k2_frage_idx" not in st.session_state:
    st.session_state["k2_frage_idx"] = 0
if "k2_abgegeben" not in st.session_state:
    st.session_state["k2_abgegeben"] = False
if "k2_feedback" not in st.session_state:
    st.session_state["k2_feedback"] = None
if "k2_radio_key" not in st.session_state:
    st.session_state["k2_radio_key"] = 0
if "k2_reset_pending" not in st.session_state:
    st.session_state["k2_reset_pending"] = False

# --- Reset-Logik ---
def reset_frage():
    st.session_state["k2_abgegeben"] = False
    st.session_state["k2_feedback"] = None
    st.session_state["k2_radio_key"] += 1

def reset_pending():
    st.session_state["k2_reset_pending"] = True

if st.session_state["k2_reset_pending"]:
    reset_frage()
    st.session_state["k2_reset_pending"] = False

# --- Schrittzähler & Fortschrittsbalken ---
aktuelle_frage = st.session_state["k2_frage_idx"]
gesamt_fragen = len(fragen)
progress = int((aktuelle_frage+1)/gesamt_fragen*100)

st.markdown('<div class="stepper">', unsafe_allow_html=True)
for i in range(gesamt_fragen):
    step_class = "step active" if i == aktuelle_frage else "step"
    st.markdown(f'<div class="{step_class}">{i+1}</div>', unsafe_allow_html=True)
    if i < gesamt_fragen-1:
        # Fortschrittsbalken zwischen den Kreisen
        bar_width = "70px"
        filled = int(bar_width.replace("px","")) * (progress/100) if i < aktuelle_frage else 0
        st.markdown(
            f'<div class="progress-bar-bg" style="width:{bar_width};">'
            f'<div class="progress-bar-fg" style="width:{filled}px;"></div></div>', unsafe_allow_html=True
        )
st.markdown('</div>', unsafe_allow_html=True)

# --- Weiße Trennlinie ---
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# --- Frage anzeigen ---
frage = fragen[aktuelle_frage]
st.markdown(f"<b>{frage['frage']}</b>", unsafe_allow_html=True)

auswahl = st.radio(
    "Antwort auswählen:",
    frage["antworten"],
    key=f"k2_radio_{st.session_state['k2_radio_key']}_{aktuelle_frage}",
    disabled=st.session_state["k2_abgegeben"]
)

# --- Abgabe-Button ---
if not st.session_state["k2_abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["k2_abgegeben"] = True
        if frage["antworten"].index(auswahl) == frage["richtig"]:
            st.session_state["k2_feedback"] = "richtig"
        else:
            st.session_state["k2_feedback"] = "falsch"

# --- Feedback & Navigation ---
if st.session_state["k2_abgegeben"]:
    if st.session_state["k2_feedback"] == "richtig":
        st.markdown(
            f'<div class="feedback-bubble"><span class="avatar">🧑‍💼</span> <b>{frage["feedback_richtig"]}</b></div>',
            unsafe_allow_html=True
        )
        if aktuelle_frage < gesamt_fragen-1:
            if st.button("Weiter"):
                st.session_state["k2_frage_idx"] += 1
                reset_frage()
        else:
            if st.button("Zurück zu Kapitelübersicht"):
                st.session_state["k2_frage_idx"] = 0
                reset_frage()
                st.switch_page("pages/6_Kapitelübersicht.py")
    else:
        st.markdown(
            f'<div class="feedback-bubble"><span class="avatar">🧑‍💼</span> <b>{frage["feedback_falsch"]}</b></div>',
            unsafe_allow_html=True
        )
        if st.button("Wiederholen"):
            reset_pending()
            st.info("🔄 Gleich geht's weiter! Die Frage wird jetzt neu geladen ...")
