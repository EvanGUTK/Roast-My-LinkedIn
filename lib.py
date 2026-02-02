"""Shared Gemini API key and helpers for Roast-My-LinkedIn."""
import os
import streamlit as st
import google.generativeai as genai

MODEL_NAME = "gemini-2.5-flash-lite"


def get_gemini_api_key():
    """Use Streamlit secrets (Cloud) or .env / environment (local)."""
    try:
        return st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    except Exception:
        return os.getenv("GEMINI_API_KEY")


def get_model():
    """Configure genai and return the GenerativeModel."""
    key = get_gemini_api_key()
    if not key:
        return None
    genai.configure(api_key=key)
    return genai.GenerativeModel(MODEL_NAME)


def run_chat(model, user_message: str, roast: str, toast: str, history: list) -> str:
    """Reply using roast/toast as context and conversation history."""
    context = f"""You are a helpful coach. Below is the ROAST and TOAST from a LinkedIn/resume review. Answer the user's follow-up questions using this context. Be concise and actionable.

ROAST:
{roast}

TOAST:
{toast}
"""
    conv = []
    for m in history:
        role = "user" if m["role"] == "user" else "model"
        conv.append(f"{role.capitalize()}: {m['content']}")
    conv.append(f"User: {user_message}")
    conv.append("Assistant:")
    prompt = context + "\n\n" + "\n\n".join(conv)
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 1024,
            },
        )
        if response and response.text:
            return response.text.strip()
        return "I couldn't generate a reply. Try again."
    except Exception as e:
        return f"Error: {e}"
