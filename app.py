import streamlit as st
from database import register_user, login_user

st.set_page_config(page_title="AI Study Assistant", layout="centered")

# Session states
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
            st.session_state.logged_in = True
            st.session_state.username = user[0]
            st.session_state.fullname = user[1]
            st.success("Login successful!")
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
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    age = st.number_input("Age", min_value=10, max_value=100, step=1)

    qualification_options = [
        "Engineering",
        "Medical",
        "Science",
        "Commerce",
        "Arts",
        "Diploma",
        "Other"
    ]

    qualification = st.selectbox("Qualification Stream", qualification_options)

    if qualification == "Other":
        qualification = st.text_input("Enter Your Qualification")

    if st.button("Create Account"):
        if password != confirm_password:
            st.error("Passwords do not match")
        elif not fullname or not username or not email:
            st.error("Please fill all required fields")
        else:
            msg = register_user(username, password, email, fullname, age, qualification)
            st.success(msg)

    st.markdown("Already have an account?")
    if st.button("⬅ Login Here"):
        st.session_state.page = "login"
        st.rerun()

# ---------------- DASHBOARD ----------------
def dashboard():
    st.sidebar.success(f"Welcome {st.session_state.fullname}")
    st.title("🎓 Student Dashboard")
    st.write("AI Study features will appear here.")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()

# ---------------- ROUTER ----------------
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        register_page()
else:
    dashboard()
