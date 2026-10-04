# Imports
import os
from dotenv import load_dotenv
from smolagents import tool, CodeAgent, LiteLLMModel
from src.rag import ask_product_rag, ask_service_rag
from src.orders import get_order
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

# oder search tool
@tool
def order_search(order_id: str) -> str:
    """
    Search the Amazon Orders Google Sheet using an order ID.
    Args:
        order_id: The unique order ID to search for, such as ORD1098.
    Returns:
        The complete order information if the order exists,
        otherwise a message saying the order was not found.
    """
    order = get_order(order_id)
    return str(order)
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
    support_search,
    order_search

]
# Fast agent for simple queries
fast_agent = CodeAgent(
    tools=tools,
    model=model,
    max_steps=2,
    verbosity_level=0,
)

# Extended agent for queries requiring multiple tool calls
extended_agent = CodeAgent(
    tools=tools,
    model=model,
    max_steps=10,
    verbosity_level=0,
)


# Adaptive agent execution
def run_agent(query: str) -> str:
    try:
        return str(fast_agent.run(query))
    except Exception:
        return str(extended_agent.run(query))
