from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL
)

def load_llm():
    """
    Load and return the Gemini LLM.
    """
    if not GOOGLE_API_KEY:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please check your .env file."
        )
    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
    )
    print("Gemini loaded successfully.")
    return llm