import streamlit as st
import datetime
import time
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="StudyFlix Dashboard",
    layout="wide"
)

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-color: #121212;
    color: white;
}

h1, h2, h3 {
    color: #E50914;
}

div.stButton > button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #ff1e1e;
}

section[data-testid="stSidebar"] {
    background-color: #1c1c1c;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION DEFAULTS ----------------
if "fullname" not in st.session_state:
    st.session_state.fullname = "Student"

if "xp" not in st.session_state:
    st.session_state.xp = 250

if "streak" not in st.session_state:
    st.session_state.streak = 3

if "study_hours" not in st.session_state:
    st.session_state.study_hours = 12

if "joke_shown" not in st.session_state:
    st.session_state.joke_shown = False


# ---------------- LEVEL FUNCTION ----------------
def get_level(xp):
    if xp < 200:
        return "Beginner"
    elif xp < 500:
        return "Scholar"
    elif xp < 1000:
        return "Mastermind"
    else:
        return "Legend"


# ---------------- DASHBOARD ----------------
def dashboard():

    level = get_level(st.session_state.xp)

    # ---------- SIDEBAR ----------
    st.sidebar.success(f"👋 Welcome, {st.session_state.fullname}")
    st.sidebar.markdown("### 🎯 Your Stats")
    st.sidebar.write(f"⭐ XP Points: {st.session_state.xp}")
    st.sidebar.write(f"🔥 Study Streak: {st.session_state.streak} Days")
    st.sidebar.write(f"🏆 Level: {level}")
    st.sidebar.markdown("---")
    st.sidebar.info(f"📅 Today: {datetime.date.today()}")

    # ---------- TITLE ----------
    st.title("🎬 StudyFlix Dashboard")
    st.markdown("### Where Study Feels Interesting ✨")

    st.markdown("---")

    # ---------- CONTINUE STUDY ----------
    st.subheader("🎥 Continue Study")
    if st.button("▶ Resume Last Session"):
        st.success("Resuming your last study episode...")

    st.markdown("---")

    # ---------- ROW 1 ----------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📚 Courses")
        st.write("Explore curated YouTube & top study resources.")
        if st.button("📖 View Courses"):
            st.info("Opening courses section...")

    with col2:
        st.subheader("🧠 AI Study Room")
        st.write("Upload notes, get summary & auto-generated quiz.")
        if st.button("🤖 Start AI Session"):
            st.success("Launching AI Study Room...")

    st.markdown("---")

    # ---------- ROW 2 ----------
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🔥 Study Streak")
        st.success(f"{st.session_state.streak} Day Streak 🔥")
        st.write("Consistency builds legends.")
        if st.button("📆 View Streak Details"):
            st.info("Showing streak analytics...")

    with col4:
        st.subheader("📊 My Growth")
        st.write("Track your performance & improvement.")
        if st.button("📈 View Progress"):
            st.info("Opening growth dashboard...")

    st.markdown("---")

    # ---------- UPDATES ----------
    st.subheader("📰 Latest Updates")
    st.info("📢 SPPU Result Date Announced: 25 March")
    st.info("📢 Hackathon Registration Deadline: 30 March")
    st.info("📢 New AI Course Added: Data Structures Mastery")

    st.markdown("---")

    # ---------- MOTIVATION ----------
    if st.session_state.xp > 300:
        st.success("🚀 You are leveling up like a true engineer!")
    else:
        st.warning("💡 Remember: Edison failed 1000 times. Keep going!")

    st.markdown("---")

    # ---------- MEME SECTION ----------
    st.markdown("### 😂 Meme Break")
    st.markdown("""
    **When you finally fix the bug after 4 hours...**  
    *It was a missing semicolon.* 😭💻
    """)

    # ---------- AUTO TECH JOKE POPUP ----------
    if not st.session_state.joke_shown:
        time.sleep(3)
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Debugging: Being a detective in a crime movie where you are also the murderer. 😭",
            "I changed my password to 'incorrect' so when I forget it says 'your password is incorrect' 😅"
        ]
        st.toast(random.choice(jokes))
        st.session_state.joke_shown = True

    st.markdown("---")
    st.success("🎬 Choose your next learning episode and keep climbing!")


# ---------------- RUN ----------------
dashboard()
