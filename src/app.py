import os
import streamlit as st
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from chatbot import EduGuideAIChatbot

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="EduGuideAI · Academic, Immigration & Student Support",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Premium CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Fonts ─────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

* { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Animated Background ────────────────────────────────────── */
.stApp {
    background: #050d1a;
    background-image:
        radial-gradient(ellipse 80% 60% at 20% -10%, rgba(0, 180, 255, 0.08) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 85% 80%,  rgba(100, 255, 218, 0.06) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 60% 40%,  rgba(139, 92, 246, 0.05) 0%, transparent 60%);
    color: #e2e8f0;
    min-height: 100vh;
}

/* ── Hide default Streamlit chrome ──────────────────────────── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; }

/* ── Sidebar ────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #07111f 0%, #0d1b2e 100%) !important;
    border-right: 1px solid rgba(100, 255, 218, 0.12) !important;
}

section[data-testid="stSidebar"] > div { padding-top: 1.5rem; }

/* ── Sidebar Logo Area ─────────────────────────────────────── */
.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 1rem 0 1.2rem 0;
    border-bottom: 1px solid rgba(100, 255, 218, 0.12);
    margin-bottom: 1.2rem;
}

.sidebar-logo-icon {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #00b4d8, #64ffda);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    box-shadow: 0 0 18px rgba(100, 255, 218, 0.35);
    flex-shrink: 0;
}

.sidebar-logo-text h2 {
    margin: 0;
    font-size: 1.15rem;
    font-weight: 700;
    background: linear-gradient(90deg, #64ffda, #00b4d8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sidebar-logo-text p {
    margin: 0;
    font-size: 0.72rem;
    color: #4a6080;
    letter-spacing: 0.04em;
}

/* ── Status Badge ──────────────────────────────────────────── */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.status-online {
    background: rgba(52, 211, 153, 0.12);
    border: 1px solid rgba(52, 211, 153, 0.3);
    color: #34d399;
}

.status-offline {
    background: rgba(248, 113, 113, 0.12);
    border: 1px solid rgba(248, 113, 113, 0.3);
    color: #f87171;
}

.pulse-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34d399;
    animation: pulse-green 1.8s ease-in-out infinite;
}

.pulse-dot-off {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #f87171;
}

@keyframes pulse-green {
    0%, 100% { box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.6); }
    50%       { box-shadow: 0 0 0 5px rgba(52, 211, 153, 0); }
}

/* ── Metric Cards ──────────────────────────────────────────── */
.metric-row { display: flex; gap: 10px; margin-bottom: 0.8rem; }

.metric-card {
    flex: 1;
    background: linear-gradient(145deg, rgba(17, 34, 64, 0.9), rgba(10, 22, 42, 0.95));
    border: 1px solid rgba(100, 255, 218, 0.1);
    border-radius: 14px;
    padding: 1rem 0.85rem;
    transition: border-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-card:hover {
    border-color: rgba(100, 255, 218, 0.45);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(100, 255, 218, 0.08);
}

.metric-label {
    font-size: 0.65rem;
    color: #4a6080;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
}

.metric-value {
    font-size: 1.55rem;
    font-weight: 800;
    margin: 4px 0 2px;
    background: linear-gradient(90deg, #64ffda, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
}

.metric-sub {
    font-size: 0.67rem;
    color: #3a5070;
}

/* ── Sample Question Buttons ───────────────────────────────── */
.stButton > button {
    background: rgba(17, 34, 64, 0.7) !important;
    color: #8ea8c3 !important;
    border: 1px solid rgba(100, 255, 218, 0.1) !important;
    border-radius: 10px !important;
    width: 100% !important;
    text-align: left !important;
    padding: 0.55rem 0.85rem !important;
    font-size: 0.82rem !important;
    font-family: 'Inter', sans-serif !important;
    margin-bottom: 6px !important;
    transition: all 0.25s ease !important;
    line-height: 1.4 !important;
    white-space: normal !important;
}

.stButton > button:hover {
    background: rgba(100, 255, 218, 0.06) !important;
    border-color: rgba(100, 255, 218, 0.45) !important;
    color: #64ffda !important;
    transform: translateX(5px) !important;
    box-shadow: 0 4px 16px rgba(100, 255, 218, 0.08) !important;
}

/* ── Main Header ───────────────────────────────────────────── */
.main-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 1.5rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid rgba(100, 255, 218, 0.1);
}

.main-title {
    font-size: 2.6rem;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(125deg, #64ffda 0%, #38bdf8 45%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.02em;
    margin: 0 0 8px 0;
}

.main-subtitle {
    color: #4a6080;
    font-size: 0.9rem;
    font-weight: 400;
    display: flex;
    align-items: center;
    gap: 8px;
}

.tag {
    display: inline-flex;
    align-items: center;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #818cf8;
    padding: 2px 9px;
    border-radius: 999px;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.tag-teal {
    background: rgba(100, 255, 218, 0.08);
    border-color: rgba(100, 255, 218, 0.25);
    color: #64ffda;
}

/* ── Chat Messages ─────────────────────────────────────────── */
div[data-testid="stChatMessage"] {
    border-radius: 18px !important;
    margin-bottom: 0.8rem !important;
    padding: 1.1rem 1.25rem !important;
    animation: fadeSlideIn 0.35s ease-out both;
}

@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* User messages */
div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, rgba(26, 44, 76, 0.85), rgba(20, 38, 66, 0.9)) !important;
    border: 1px solid rgba(56, 189, 248, 0.15) !important;
}

/* Assistant messages */
div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, rgba(13, 27, 48, 0.9), rgba(10, 22, 42, 0.95)) !important;
    border: 1px solid rgba(100, 255, 218, 0.12) !important;
}

div[data-testid="stChatMessage"] p {
    color: #c8d8e8 !important;
    line-height: 1.75 !important;
    font-size: 0.95rem !important;
}

/* ── Chat Input ────────────────────────────────────────────── */
div[data-testid="stChatInput"] {
    border-top: 1px solid rgba(100, 255, 218, 0.1) !important;
    padding-top: 1rem !important;
}

div[data-testid="stChatInput"] textarea {
    background: rgba(17, 34, 64, 0.85) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(100, 255, 218, 0.2) !important;
    border-radius: 14px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.93rem !important;
    padding: 0.9rem 1rem !important;
    resize: none !important;
    box-shadow: 0 0 0 0 rgba(100, 255, 218, 0);
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}

div[data-testid="stChatInput"] textarea:focus {
    border-color: #64ffda !important;
    box-shadow: 0 0 0 3px rgba(100, 255, 218, 0.1) !important;
    outline: none !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #2d4a65 !important;
}

/* ── Info Cards (Feature Highlights) ──────────────────────── */
.info-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin: 1.2rem 0 1.6rem 0;
}

.info-card {
    background: linear-gradient(145deg, rgba(17, 34, 64, 0.6), rgba(10, 22, 42, 0.7));
    border: 1px solid rgba(100, 255, 218, 0.08);
    border-radius: 16px;
    padding: 1.1rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
}

.info-card:hover {
    border-color: rgba(100, 255, 218, 0.3);
    box-shadow: 0 6px 24px rgba(100, 255, 218, 0.07);
    transform: translateY(-4px);
}

.info-icon {
    font-size: 1.8rem;
    margin-bottom: 8px;
    display: block;
}

.info-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    margin-bottom: 4px;
}

.info-desc {
    font-size: 0.75rem;
    color: #3a5070;
    line-height: 1.4;
}

/* ── Disclaimer ─────────────────────────────────────────────── */
.disclaimer {
    background: rgba(245, 158, 11, 0.06);
    border: 1px solid rgba(245, 158, 11, 0.2);
    border-radius: 12px;
    padding: 0.85rem 1.2rem;
    margin-top: 1.2rem;
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 0.78rem;
    color: #78716c;
    line-height: 1.5;
}

.disclaimer-icon { font-size: 1rem; flex-shrink: 0; margin-top: 1px; }

/* ── Section Dividers ──────────────────────────────────────── */
.section-label {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #2d4a65;
    font-weight: 700;
    margin: 1.2rem 0 0.6rem 0;
}

/* ── Sidebar Checkbox ──────────────────────────────────────── */
.stCheckbox label span {
    color: #4a6080 !important;
    font-size: 0.82rem !important;
}

/* ── Sidebar line chart ─────────────────────────────────────── */
div[data-testid="stVegaLiteChart"] {
    border-radius: 10px;
    overflow: hidden;
}

/* ── Expand More Expander ────────────────────────────────────── */
div[data-testid="stExpander"] {
    background: rgba(10, 22, 42, 0.7) !important;
    border: 1px solid rgba(100, 255, 218, 0.15) !important;
    border-radius: 12px !important;
    margin-top: 8px !important;
}

div[data-testid="stExpander"] summary {
    color: #64ffda !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    padding: 0.55rem 0.9rem !important;
}

div[data-testid="stExpander"] summary:hover {
    color: #9effea !important;
}

div[data-testid="stExpander"] > div > div {
    padding: 0.7rem 1rem 1rem !important;
    color: #a8c0d8 !important;
    font-size: 0.9rem !important;
    line-height: 1.75 !important;
    border-top: 1px solid rgba(100, 255, 218, 0.08) !important;
}

/* ── Scrollbar ──────────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #050d1a; }
::-webkit-scrollbar-thumb { background: #1e3a5f; border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: #2a4d7a; }
</style>

""", unsafe_allow_html=True)


# ─── Load Resources ────────────────────────────────────────────────────────────
@st.cache_resource
def load_eduguide_chatbot():
    bot = EduGuideAIChatbot()
    bot.load_model()
    return bot


# ─── Load Bot ─────────────────────────────────────────────────────────────────
try:
    chatbot = load_eduguide_chatbot()
    model_loaded = True
except Exception as e:
    model_loaded = False
    _load_error = e

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">🎓</div>
        <div class="sidebar-logo-text">
            <h2>EduGuideAI</h2>
            <p>STUDENT & VISA ASSISTANT</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Status
    if model_loaded:
        st.markdown("""
        <div class="status-badge status-online">
            <div class="pulse-dot"></div> Assistant Online
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="status-badge status-offline">
            <div class="pulse-dot-off"></div> Assistant Offline
        </div>
        """, unsafe_allow_html=True)
        st.error("Model failed to load.")
        if '_load_error' in dir():
            with st.expander("Error details"):
                st.exception(_load_error)


    # ── Sample Questions ─────────────────────────────────────────────────────
    st.markdown('<div class="section-label" style="margin-top:1.2rem;">🔍 Try Asking</div>', unsafe_allow_html=True)

    sample_questions = [
        "What is a Subclass 500 Student Visa?",
        "How many hours can I work on a student visa?",
        "What is the 80% attendance rule?",
        "What are the Group of Eight (Go8) universities?",
        "What is plagiarism and the consequences?",
        "What is the cost of living in Australia?",
    ]

    # ── Chat History ─────────────────────────────────────────────────────────
    if "messages" not in st.session_state:
        welcome = (
            "👋 G'day! I am **EduGuideAI**, your retrieval-augmented conversational assistant for academic, immigration, and student support.\n\n"
            "Ask me anything about **visas**, **university selection**, **academic rules**, **assignments**, "
            "**attendance requirements**, or **cultural integration**!"
        )
        st.session_state.messages = [
            {"role": "assistant", "short": welcome, "full": welcome}
        ]

    def process_message(prompt):
        st.session_state.messages.append({"role": "user", "short": prompt, "full": prompt})
        if model_loaded:
            with st.spinner("Retrieving guide details…"):
                short, full = chatbot.get_response(prompt)
        else:
            short = full = "⚠️ EduGuideAI is currently offline. Please check that the dataset exists."
        st.session_state.messages.append({"role": "assistant", "short": short, "full": full})

    for sq in sample_questions:
        if st.button(sq, key=f"sidebar_q_{sq}"):
            process_message(sq)
            st.rerun()

    # ── About ────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label" style="margin-top:1rem;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size:0.76rem; color:#2d4a65; line-height:1.55;">
        EduGuideAI uses a <strong style="color:#3a5c80;">TF-IDF Hybrid Retrieval</strong> engine
        trained on a curated academic regulations, visa rules, and student support dataset.
    </p>
    """, unsafe_allow_html=True)


# ─── Main Content ─────────────────────────────────────────────────────────────

# Header
st.markdown("""
<div class="main-header">
    <div>
        <h1 class="main-title">EduGuideAI 🎓</h1>
        <div class="main-subtitle">
            A Retrieval-Augmented Conversational Assistant for Academic, Immigration, and Student Support &nbsp;
            <span class="tag tag-teal">TF-IDF Retrieval</span>&nbsp;
            <span class="tag">Student Support</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Feature Highlights (shown only when no conversation yet)
if len(st.session_state.messages) <= 1:
    st.markdown("""
    <div class="info-grid">
        <div class="info-card">
            <span class="info-icon">📜</span>
            <div class="info-title">Visas & Rules</div>
            <div class="info-desc">Subclass 500, 485, work hour limits, and visa requirements</div>
        </div>
        <div class="info-card">
            <span class="info-icon">🏫</span>
            <div class="info-title">Uni Selection</div>
            <div class="info-desc">Group of Eight, technological networks, intakes, and requirements</div>
        </div>
        <div class="info-card">
            <span class="info-icon">📝</span>
            <div class="info-title">Academia</div>
            <div class="info-desc">80% attendance policy, plagiarism rules, and extensions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        short = message.get("short", message.get("content", ""))
        full  = message.get("full",  message.get("content", ""))
        st.markdown(short)
        # Show expander only for assistant messages where full != short
        if message["role"] == "assistant" and full != short:
            with st.expander("📖 Expand for full answer"):
                st.markdown(full)

# Input
if user_prompt := st.chat_input("Ask a visa or university question… e.g. 'What is the attendance rule?'"):
    process_message(user_prompt)
    st.rerun()

# Disclaimer
st.markdown("""
<div class="disclaimer">
    <span class="disclaimer-icon">⚠️</span>
    <span>
        <strong style="color:#a8996b;">Education & Visa Disclaimer:</strong>
        EduGuideAI is an educational assistant providing general guide details compiled from public immigration and university policy documents. 
        It is <em>not</em> legal immigration advice or official university advice. Always check official sources like homeaffairs.gov.au or your university's handbook.
    </span>
</div>
""", unsafe_allow_html=True)
