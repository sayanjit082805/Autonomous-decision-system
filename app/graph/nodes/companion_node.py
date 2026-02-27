from app.services.gemini_client import generate_content
from app.services.retry import retry_on_exception


COMPANION_PROMPT = """
You are a friendly health assistant companion.

Your role:
- Engage in polite conversation.
- Provide emotional support.
- Offer general wellness encouragement.
- DO NOT provide medical diagnosis.
- DO NOT provide medication advice.
- DO NOT provide treatment plans.

If the user asks for medical advice, respond with:
"I'm here for general support. Let me route your concern to our clinical system."

Keep responses warm, concise, and supportive.

User input:
"""

@retry_on_exception
def call_model(prompt: str):
    return generate_content(prompt)

def companion_node(state):
    user_input = state["user_input"]

    prompt = COMPANION_PROMPT + user_input

    try:
        response = call_model(prompt)

        state["companion_output"] = response.strip()

    except Exception as e:
        state["companion_output"] = (
            "I'm here to support you. Let me connect you with the clinical system."
        )
        state["companion_error"] = str(e)

    return state