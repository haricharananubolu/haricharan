import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

# Fallback check if user forgot to set the API key
if not API_KEY:
    raise ValueError("API Key missing! Please check your .env file.")