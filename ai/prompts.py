"""
Prompt templates for Gemini AI.
"""


def summary_prompt(subject, snippet):
    """
    Create a prompt for email summarization.
    """

    return f"""
You are an intelligent email assistant.

Summarize the following email in a maximum of 3 short sentences.

Rules:
- Keep it concise.
- Mention important deadlines if present.
- Mention company name if present.
- Ignore greetings and signatures.
- Return plain text only.

Subject:
{subject}

Content:
{snippet}
"""