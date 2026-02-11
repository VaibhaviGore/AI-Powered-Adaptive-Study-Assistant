import streamlit as st

def courses_dashboard():

    # ---- Custom CSS ----
    st.markdown("""
    <style>
    .course-container {
        display: flex;
        overflow-x: auto;
        padding: 20px 0;
        gap: 20px;
    }

    .course-card {
        min-width: 250px;
        background-color: #1f1f1f;
        padding: 20px;
        border-radius: 15px;
        transition: transform 0.3s ease;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
    }

    .course-card:hover {
        transform: scale(1.05);
        background-color: #2a2a2a;
    }

    .course-title {
        font-size: 22px;
        font-weight: bold;
        color: white;
    }

    .course-info {
        font-size: 14px;
        color: #bbbbbb;
        margin-top: 5px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 style='color:white;'>🎬 StudyFlix Courses</h1>
        <p style='color:gray;'>Upgrade your skills. Learn like a pro.</p>
    """, unsafe_allow_html=True)

    courses = [
        {"name": "C Programming", "icon": "💻",
         "level": "Beginner", "duration": "4 Weeks",
         "youtube": "https://www.youtube.com/watch?v=irqbmMNs2Bo",
         "web1": "https://www.programiz.com/c-programming"},

        {"name": "C++ Programming", "icon": "🧠",
         "level": "Beginner-Intermediate", "duration": "6 Weeks",
         "youtube": "https://www.youtube.com/watch?v=vLnPwxZdW4Y",
         "web1": "https://www.programiz.com/cpp-programming"},

        {"name": "Java Programming", "icon": "☕",
         "level": "Intermediate", "duration": "8 Weeks",
         "youtube": "https://www.youtube.com/watch?v=eIrMbAQSU34",
         "web1": "https://www.javatpoint.com/java-tutorial"},

        {"name": "Python Programming", "icon": "🐍",
         "level": "Beginner-Advanced", "duration": "6 Weeks",
         "youtube": "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
         "web1": "https://www.w3schools.com/python/"}
    ]

    # ---- Horizontal Scroll Row ----
    st.markdown("<div class='course-container'>", unsafe_allow_html=True)

    for i, course in enumerate(courses):

        st.markdown(f"""
        <div class='course-card'>
            <div class='course-title'>
                {course['icon']} {course['name']}
            </div>
            <div class='course-info'>
                🎯 {course['level']} <br>
                ⏳ {course['duration']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")

    # ---- Course Detail Section ----
    selected_course = st.selectbox(
        "📚 Select a Course to Explore",
        [c["name"] for c in courses]
    )

    course_data = next(c for c in courses if c["name"] == selected_course)

    st.subheader(f"{course_data['icon']} {course_data['name']}")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button("🎥 Watch Playlist", course_data["youtube"])

    with col2:
        st.link_button("🌐 Study Website", course_data["web1"])

    st.video(course_data["youtube"])