"""
RMLT — Chat about your roast & toast (Gemini-style).
"""
import streamlit as st
from lib import get_gemini_api_key, get_model, run_chat

# Gemini-like dark theme for this page
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #1a1a1a;
    }
    .rmlt-header {
        color: #e8eaed;
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 0.25rem;
    }
    .rmlt-prompt {
        color: #e8eaed;
        font-size: 2rem;
        font-weight: 500;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Need API key
if not get_gemini_api_key():
    st.error("Missing **GEMINI_API_KEY**. Set it in Streamlit Cloud Secrets or in `.env` locally.")
    st.stop()

model = get_model()

# Need roast & toast from main page
if not st.session_state.get("roast") or not st.session_state.get("toast"):
    st.markdown('<p class="rmlt-header">Hi</p>', unsafe_allow_html=True)
    st.markdown('<p class="rmlt-prompt">Feedback</p>', unsafe_allow_html=True)
    st.info("Get a **Roast & Toast** on the home page first, then come back here to ask questions.")
    if st.button("← Back to Roast-My-LinkedIn"):
        st.switch_page("app.py")
    st.stop()

# Gemini-style header
st.markdown('<p class="rmlt-header">Hi</p>', unsafe_allow_html=True)
st.markdown('<p class="rmlt-prompt">Feedback</p>', unsafe_allow_html=True)

# Chat history
for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "✨"):
        st.markdown(msg["content"])

# Input: placeholder "Ask RMLT"
if prompt := st.chat_input("Ask RMLT"):
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant", avatar="✨"):
        with st.spinner("Thinking..."):
            reply = run_chat(
                model,
                prompt,
                st.session_state.roast,
                st.session_state.toast,
                st.session_state.chat_messages[:-1],
            )
        st.markdown(reply)
    st.session_state.chat_messages.append({"role": "assistant", "content": reply})
    st.rerun()
