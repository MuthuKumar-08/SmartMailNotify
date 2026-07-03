"""
Gemini AI Client
"""

from google import genai

from config.settings import GEMINI_API_KEY
from ai.prompts import summary_prompt

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_summary(subject, snippet):
    """
    Generate an AI summary for an email.
    """

    prompt = summary_prompt(subject, snippet)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()