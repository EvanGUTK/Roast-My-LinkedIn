"""
Roast-My-LinkedIn — Upload a LinkedIn/resume screenshot, get a Roast + Toast from Gemini.
"""
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

from lib import get_gemini_api_key, get_model

load_dotenv()

# Page config
st.set_page_config(
    page_title="Roast-My-LinkedIn",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Session state for roast/toast (chat lives on RMLT page)
if "roast" not in st.session_state:
    st.session_state.roast = None
if "toast" not in st.session_state:
    st.session_state.toast = None
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Configure Gemini (works with Streamlit Cloud secrets or .env locally)
if not get_gemini_api_key():
    st.error(
        "Missing **GEMINI_API_KEY**. Add it to `.env` locally or to **Streamlit Cloud → App → Settings → Secrets** when deployed."
    )
    st.stop()

model = get_model()

# Prompts
ROAST_PROMPT = """You are a brutally honest, funny senior engineer reviewing this LinkedIn profile or resume screenshot.
Give a short, sharp ROAST: witty, a bit harsh, call out generic buzzwords, empty sections, or cringe. Be entertaining, not mean-spirited. Keep it to 2–4 short paragraphs."""

TOAST_PROMPT = """You are a supportive senior engineer giving constructive feedback on this LinkedIn profile or resume screenshot.
Give a short TOAST: what's working, what to improve, and 3–5 specific, actionable tips to stand out (e.g., wording, structure, keywords, clarity). Be encouraging and practical. Keep it to 2–4 short paragraphs."""


def run_vision(prompt: str, image: Image.Image) -> str:
    """Call Gemini with image + prompt and return the text response."""
    try:
        response = model.generate_content(
            [image, prompt],
            generation_config={
                "temperature": 0.8,
                "max_output_tokens": 1024,
            },
        )
        if response and response.text:
            return response.text.strip()
        return "No response generated. Try again."
    except Exception as e:
        return f"Error: {e}"


# UI
st.title("🔥 Roast-My-LinkedIn")
st.caption("Upload a screenshot of your LinkedIn profile or resume. Get roasted, then get real advice.")

uploaded = st.file_uploader(
    "Upload screenshot (PNG or JPG)",
    type=["png", "jpg", "jpeg"],
    help="Screenshot of your LinkedIn profile or resume.",
)

if uploaded is None:
    st.info("👆 Upload an image to get started.")
else:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, width="stretch", caption="Your upload")

    if st.button("Get Roast & Toast", type="primary"):
        with st.spinner("Roasting…"):
            roast = run_vision(ROAST_PROMPT, img)
        with st.spinner("Toasting…"):
            toast = run_vision(TOAST_PROMPT, img)
        st.session_state.roast = roast
        st.session_state.toast = toast
        st.session_state.chat_messages = []
        st.rerun()

    if st.session_state.roast and st.session_state.toast:
        st.subheader("😈 Roast")
        st.markdown(st.session_state.roast)
        st.subheader("🍞 Toast")
        st.markdown(st.session_state.toast)
        st.page_link("pages/1_RMLT.py", label="💬 Chat with RMLT", icon="✨")

# Footer
st.divider()
st.markdown(
    "[LinkedIn](https://www.linkedin.com/in/evan-goodman-089762244/) · "
    "[GitHub](https://github.com/EvanGUTK) · **v1.1** · Coded by **Evan Goodman**"
)
