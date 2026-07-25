from dotenv import load_dotenv
import os

# Tr  s for ChatGoogleGenerativeAI to handle different langchain versions
try:
    from langchain.chat_models import ChatGoogleGenerativeAI
except Exception:
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
    except Exception as e:
        # Provide a clear error if the optional dependency is missing or cannot be resolved
        raise ImportError(
            "Failed to import 'ChatGoogleGenerativeAI'. Please install the appropriate package (e.g. `langchain` or `langchain-google-genai`) "
            "or ensure it's available in your environment. Original error: {}".format(e)
        )
def load_llm():
    """
    Load Gemini model.
    Returns:
        ChatGoogleGenerativeAI
    """
    # Load .env file
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please check your .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=api_key
    )

    print("Gemini loaded successfully.")
    return llm