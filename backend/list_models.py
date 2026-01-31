from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from your .env file

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Listing all models your API key can access:")

for m in client.models.list():
    print(m.name)
