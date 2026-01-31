from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
print("API KEY:", API_KEY)

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Initialize FastAPI
app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    try:
        # Use a valid model from your list
        result = client.models.generate_content(
            model="models/gemini-2.5-flash",  # ✅ change this to a valid model
            contents=req.message
        )

        return {"reply": result.text}

    except Exception as e:
        print("Gemini Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
