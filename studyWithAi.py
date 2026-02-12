# study_room.py
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def studyRoom():
    # ---------------- 1. SETUP: Load API Key and Initialize Gemini Client ----------------
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        st.error("Missing GEMINI_API_KEY. Please check your .env file.")
        st.stop()

    client = genai.Client(api_key=API_KEY)

    # ---------------- 2. UI CONFIGURATION ----------------
    st.set_page_config(page_title="Study Assistant", layout="wide")
    st.title("📚 AI Study Assistant")
    st.caption("Summarize PDFs, Analyze Images, and Get Real-Life Examples")

    # ---------------- 3. SESSION STATE: Keep track of chat history ----------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ---------------- 4. CHAT INPUT: Handles text and file uploads (Images/PDFs) ----------------
    user_input = st.chat_input("Type a message or upload notes...", accept_file="multiple")
    if user_input:
        # Display user's text message
        with st.chat_message("user"):
            st.markdown(user_input.text)
            if hasattr(user_input, "files") and user_input.files:
                st.info(f"📎 {len(user_input.files)} file(s) uploaded.")

        # Save user message to history
        st.session_state.messages.append({"role": "user", "content": user_input.text})

        # ---------------- 5. PREPARE CONTENT FOR GEMINI ----------------
        gemini_contents = [user_input.text]

        if hasattr(user_input, "files"):
            for uploaded_file in user_input.files:
                with st.status(f"Processing {uploaded_file.name}...", expanded=False):
                    try:
                        google_file = client.files.upload(
                            file=uploaded_file,
                            config=types.UploadFileConfig(mime_type=uploaded_file.type)
                        )
                        gemini_contents.append(google_file)
                    except Exception as e:
                        st.error(f"File upload failed: {e}")

        # ---------------- 6. GENERATE RESPONSE ----------------
        with st.chat_message("assistant"):
            with st.spinner("Analyzing study material..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=gemini_contents,
                        config=types.GenerateContentConfig(
                            system_instruction=(
                                "You are a helpful study tutor. Summarize all inputs into "
                                "short, key points. Always explain complex concepts with "
                                "one simple real-life example."
                            )
                        )
                    )

                    # Display and Save response
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})

                except Exception as e:
                    st.error(f"Gemini API Error: {e}")
