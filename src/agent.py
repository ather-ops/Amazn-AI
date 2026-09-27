# Imports
import os
from dotenv import load_dotenv
from groq import Groq
from smolagents import tool,CodeAgent,LiteLLMModel
from src.rag import ask_product_rag, ask_service_rag

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
    return ask_product_rag(query)

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
    return ask_service_rag(query)
print("All works perfectly!")

# Defining the model
model = LiteLLMModel(
    model_id="groq/qwen/qwen3.8-27b",
    api_key=os.getenv("GROQ_API_KEY")
)

# Defining the tools
tools=[
    product_search,
    support_search
]


# Routing two tools
amazn_agent=CodeAgent(
    tools=tools,
    model=model,
    max_steps=5
)
