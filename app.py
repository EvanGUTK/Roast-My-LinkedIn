"""
Roast-My-LinkedIn — Upload a LinkedIn/resume screenshot, get a Roast + Toast from Gemini.
"""
import os
from io import BytesIO

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# Page config
st.set_page_config(
    page_title="Roast-My-LinkedIn",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Missing **GEMINI_API_KEY**. Add it to `.env` or your environment.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# Model with vision; gemini-2.5-flash-lite has free-tier quota (15 RPM, 1000 RPD)
MODEL_NAME = "gemini-2.5-flash-lite"
model = genai.GenerativeModel(MODEL_NAME)

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
    st.stop()

# Show image
img = Image.open(uploaded).convert("RGB")
st.image(img, use_container_width=True, caption="Your upload")

if st.button("Get Roast & Toast", type="primary"):
    with st.spinner("Roasting…"):
        roast = run_vision(ROAST_PROMPT, img)
    with st.spinner("Toasting…"):
        toast = run_vision(TOAST_PROMPT, img)

    st.subheader("😈 Roast")
    st.markdown(roast)

    st.subheader("🍞 Toast")
    st.markdown(toast)
