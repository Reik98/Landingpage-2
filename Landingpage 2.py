import streamlit as st

st.set_page_config(
    page_title="KI als Kollege - Change-Strategien und Meetingdesign",
    layout="wide"
)

# Custom CSS für Style und Layout
st.markdown("""
    <style>
        html, body {
            background-color: #f5f7fa;
            font-family: 'Inter', sans-serif;
            color: #222;
        }
        .header {
            background-color: #003865;
            color: white;
            padding: 60px 20px;
            text-align: center;
            border-radius: 0 0 20px 20px;
        }
        .header h1 {
            font-size: 2.5rem;
            margin: 0;
        }
        .header p {
            font-size: 1.2rem;
            margin: 20px 0;
        }
        .cta-button {
            background: #ff6600;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
        }
        .highlight {
            background: white;
            padding: 30px;
            margin: 30px 0;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        footer {
            background-color: #222;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
            border-radius: 20px 20px 0 0;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="header">
    <h1>KI als Kollege</h1>
    <p>Mit strukturiertem Change Management und modernen Meetingformaten zur erfolgreichen Zusammenarbeit mit KI-Agenten.</p>
    <a href="#angebot" class="cta-button">Jetzt Meeting-Coaching buchen</a>
</div>
""", unsafe_allow_html=True)

# SECTION 1: Warum KI abgelehnt wird
st.markdown("""
<div class="highlight">
    <h2>Warum Mitarbeiter KI ablehnen</h2>
    <p>Die fünf größten psychologischen Blockaden und wie ein durchdachter Change-Prozess helfen kann.</p>
</div>
""", unsafe_allow_html=True)

# SECTION 2: Unser Angebot
st.markdown("""
<div class="highlight" id="angebot">
    <h2>Unser Angebot</h2>
    <ul>
        <li>Change-Modell für KI-Einführung in Abteilungen</li>
        <li>Leitfaden: 5 Dos & Don'ts für Meetings mit KI</li>
        <li>Workshop: Integration mehrerer LLMs in Live-Meetings</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<footer>
    &copy; 2025 KI-Beratung GmbH · DSGVO-konform · Impressum · Datenschutz
</footer>
""", unsafe_allow_html=True)
