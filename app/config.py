# Configurations for handling environment variables and other settings for the application
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash" 

MAX_RETRIES = 2
REQUEST_TIMEOUT = 15