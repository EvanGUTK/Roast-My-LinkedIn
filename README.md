# Roast-My-LinkedIn

**LinkedIn Profile Roast & Toast** — An AI-powered tool that gives your profile or resume a funny roast and then constructive senior-dev advice. Perfect for internship season.

---

## The Vibe

Everyone’s grinding for internships. You’ve polished your LinkedIn and resume, but you still wonder: *What would a senior engineer actually think?*

**Roast-My-LinkedIn** answers that in two ways:

1. **Roast** — A sharp, funny (and a bit harsh) take on your profile. No sugar-coating; it’s the roast you didn’t know you needed.
2. **Toast** — Actionable, senior-dev style feedback: what’s working, what to tweak, and how to stand out.

Upload a screenshot of your LinkedIn profile or resume, and get both perspectives in one place. It’s a fun, social way to get real feedback and show you can ship API + image-based tools.

---

## Features

| Feature | Description |
|--------|-------------|
| **Image upload** | Drag-and-drop or select a screenshot of your LinkedIn profile or resume |
| **Roast** | AI-generated roast: witty, direct, and a little brutal |
| **Toast** | AI-generated constructive feedback and improvement tips |
| **Vision LLM** | Uses a vision-capable model to “read” your profile from the image |
| **API choice** | Designed to work with **Google Gemini** or **OpenAI** (GPT-4 Vision) |

---

## Tech Stack

- **Frontend / app**: [Streamlit](https://streamlit.io/) — fast UI, `st.file_uploader` for images
- **AI / vision**: Vision-capable LLM via **Gemini API** or **OpenAI API** (image + text)
- **Language**: Python 3.x
- **Concepts**: API integration, image upload, prompt engineering, dual “personas” (roast vs toast)

---

## How It Works (User Flow)

1. User opens the Streamlit app.
2. User uploads an image (screenshot of LinkedIn profile or resume) via `st.file_uploader`.
3. App sends the image (and a “roast” prompt) to the vision LLM → user sees the **Roast**.
4. App sends the same image (and a “toast” prompt) to the vision LLM → user sees the **Toast**.
5. User can upload again for another round of feedback.

---

## API Options

The app is designed to support either (or both, with a toggle):

- **Google Gemini** — Vision models (e.g. Gemini 1.5 Pro / Flash) with image input.
- **OpenAI** — GPT-4 Vision (or compatible) for image + text prompts.

Environment variables (e.g. `GEMINI_API_KEY`, `OPENAI_API_KEY`) will be used for keys; no keys in the repo.

---

## Project Structure (Planned)

```
Roast-My-LinkedIn/
├── README.md
├── requirements.txt      # streamlit, google-generativeai / openai, etc.
├── .env.example          # API key placeholders
├── app.py                # Streamlit entrypoint (uploader + roast/toast UI)
└── prompts.py            # Roast & toast prompt templates (optional)
```

*(Structure may evolve as the app is built.)*

---

## Setup (When Implemented)

1. **Clone the repo**
   ```bash
   git clone https://github.com/EvanGUTK/Roast-My-LinkedIn.git
   cd Roast-My-LinkedIn
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   - Copy `.env.example` to `.env`
   - Add your `GEMINI_API_KEY` and/or `OPENAI_API_KEY`

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## Why This Project?

- **Relevant** — Tied to internship prep and profile/resume feedback.
- **Technical** — Streamlit, file upload, vision APIs, and prompt design.
- **Fun** — Roast + toast makes it shareable and memorable.
- **Portfolio-ready** — Demonstrates API integration and image handling in a single small project.

---

## Contributing

Ideas and contributions are welcome: prompt tweaks, support for more models, or UI improvements. Open an issue or a pull request.

---

## License

MIT (or your preferred license — update as needed).

---

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the app framework
- [Google Gemini](https://ai.google.dev/) and [OpenAI](https://platform.openai.com/) for vision APIs
- Everyone grinding for internships — may your roasts be funny and your toasts be helpful.

---

*Roast-My-LinkedIn — Get roasted, get better.*
