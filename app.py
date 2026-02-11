import streamlit as st
from database import register_user, login_user
from dashboard import dashboard  # Import StudyFlix dashboard
from courses import courses_dashboard  # Optional: courses page if used

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Study Assistant", layout="centered")

# ---------------- SESSION STATES ----------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            # Save all user info in session_state
            st.session_state.logged_in = True
            st.session_state.username = user[0]
            st.session_state.fullname = user[1]
            st.session_state.email = user[2]
            st.session_state.age = user[4]
            st.session_state.qualification = user[5]
            st.success("Login successful!")
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.markdown("Don't have an account?")
    if st.button("➡ Register Here"):
        st.session_state.page = "register"
        st.rerun()

# ---------------- REGISTER PAGE ----------------
def register_page():
    st.title("📝 Register")

    fullname = st.text_input("Full Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=10, max_value=100, step=1)

    # Qualification dropdown
    qualification_options = ["Engineering", "Medical", "Art", "Other"]
    qualification = st.selectbox("Qualification", qualification_options)

    # If "Other" selected, allow manual input
    if qualification == "Other":
        qualification = st.text_input("Enter your qualification")

    if st.button("Create Account"):
        if not fullname or not email or not username or not password or not age or not qualification:
            st.error("Please fill in all fields")
        else:
            msg = register_user(username, password, email, fullname, age, qualification)
            if "successfully" in msg:
                st.success(msg)
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error(msg)

    st.markdown("Already have an account?")
    if st.button("⬅ Login Here"):
        st.session_state.page = "login"
        st.rerun()

# ---------------- ROUTER ----------------
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        register_page()
else:
    if st.session_state.page == "dashboard":
        dashboard()  # Shows dashboard from dashboard.py
    elif st.session_state.page == "courses":
        courses_dashboard()
