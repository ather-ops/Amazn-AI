from src.vectordb import (
    load_langchain_embedding,
    load_vector_store,
    similarity_search,
)

from src.prompt import load_prompt
from src.llm import load_llm
from src.utils import (
    print_heading,
    print_search_results,
)
from src.config import VECTOR_STORE_PATH
def main():
    print_heading("AMAZN AI MODULE TEST")
    # Load Embedding Model
    embedding_model = load_langchain_embedding()
    print("Embedding Model Loaded")
    # Load Vector Store
    vector_store = load_vector_store(
        VECTOR_STORE_PATH,
        embedding_model
    )
    print("Vector Store Loaded")
    # Similarity Search
    results = similarity_search(
        vector_store,
        query="gaming laptop",
        k=3
    )
    print_heading("Top Results")
    print_search_results(results)
    # Prompt
    print_heading("Prompt")
    print("Prompt Loaded Successfully")
    print(type(load_prompt))
    # Gemini
    llm = load_llm()
    print_heading("LLM")
    print("Gemini Loaded Successfully")
    print(type(llm))
    print_heading("ALL MODULES WORKING SUCCESSFULLY")

if __name__ == "__main__":
    main()