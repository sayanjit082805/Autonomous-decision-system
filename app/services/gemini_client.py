# Service to interact with the Gemini API for content generation
from google import genai
from app.config import GEMINI_API_KEY, MODEL_NAME, REQUEST_TIMEOUT

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_content(prompt: str):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return response.text