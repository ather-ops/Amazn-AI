# Imports
import os
from dotenv import load_dotenv
from smolagents import tool, CodeAgent, LiteLLMModel
from src.rag import ask_product_rag, ask_service_rag

load_dotenv()


# Product Tool
@tool
def product_search(query: str) -> str:
    """
    Search Amazon products using the product knowledge base.

    Args:
        query: The user's product-related question or request.

    Returns:
        A response generated from the Amazon product knowledge base.
    """
    result = ask_product_rag(query)
    return result[:2000]   


# Support Tool
@tool
def support_search(query: str) -> str:
    """
    Answer Amazon customer-support questions using the support knowledge base.

    Args:
        query: The user's customer-support question or request.

    Returns:
        A response generated from the Amazon support knowledge base.
    """
    result = ask_service_rag(query)
    return result[:2000]

# Defining the model
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found — check your .env file")

model = LiteLLMModel(
    model_id="groq/qwen/qwen3.8-27b",
    api_key=api_key,
    num_retries=3,
    timeout=60,
)

# Defining the tools
tools = [
    product_search,
    support_search
]

# Routing two tools
amazn_agent = CodeAgent(
    tools=tools,
    model=model,
    max_steps=4,
    verbosity_level=1,
)
