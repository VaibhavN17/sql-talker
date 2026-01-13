import os
import google.generativeai as genai


def _get_api_key():
    # Support common env var names
    return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")


API_KEY = _get_api_key()

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")


def generate_text(prompt: str) -> str:
    """Generate text using Gemini. If no API key is configured, raise a helpful error.

    This makes the failure explicit and gives the user instructions to set
    the environment variable in `.env` (GEMINI_API_KEY) or in their shell.
    """
    if not API_KEY:
        raise EnvironmentError(
            "No Gemini API key configured. Set GEMINI_API_KEY in your environment or .env. "
            "Example: GEMINI_API_KEY=your_api_key. See README for details."
        )

    response = model.generate_content(prompt)
    return response.text.strip()
