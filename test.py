"""
test.py

Integration test for AMAZN AI.
"""

from src.data_loader import load_dataset
from src.chunking import create_chunks

from src.embeddings import (
    load_embedding_model,
    create_embeddings,
)

from src.vectordb import (
    load_langchain_embedding,
    create_langchain_documents,
    create_vector_store,
    save_vector_store,
    similarity_search,
)

from src.prompt import load_prompt
from src.llm import load_llm

from src.utils import (
    print_heading,
    print_search_results,
)


def main():

    print_heading("AMAZN AI MODULE TEST")

    # ==========================================================
    # Dataset
    # ==========================================================

    df = load_dataset()
    print("Dataset Loaded")

    # ==========================================================
    # Chunking
    # ==========================================================

    chunks, metadata, ids = create_chunks(df)

    print(f"Chunks Created : {len(chunks)}")
    print(f"Metadata       : {len(metadata)}")
    print(f"IDs            : {len(ids)}")

    # ==========================================================
    # Embedding Model
    # ==========================================================

    embedding_model = load_embedding_model()

    embeddings = create_embeddings(
        embedding_model,
        chunks
    )

    print(f"✅ Embedding Shape : {embeddings.shape}")

    # ==========================================================
    # LangChain Documents
    # ==========================================================

    documents = create_langchain_documents(
        chunks,
        metadata
    )

    print(f"Documents Created : {len(documents)}")

    # ==========================================================
    # Vector Database
    # ==========================================================

    lc_embedding = load_langchain_embedding()

    vector_store = create_vector_store(
        documents,
        lc_embedding
    )

    print("Vector Store Created")

    save_vector_store(vector_store)

    print("Vector Store Saved")

    # ==========================================================
    # Similarity Search
    # ==========================================================

    results = similarity_search(
        vector_store,
        query="gaming laptop",
        k=3
    )

    print_heading("Top Results")

    print_search_results(results)

    # ==========================================================
    # Prompt
    # ==========================================================

    prompt = load_prompt()

    print_heading("Prompt")

    print("Prompt Loaded Successfully")
    print(type(prompt))

    # ==========================================================
    # Gemini LLM
    # ==========================================================

    llm = load_llm()

    print_heading("LLM")

    print("Gemini Loaded Successfully")
    print(type(llm))

    print_heading("ALL MODULES WORKING SUCCESSFULLY")


if __name__ == "__main__":
    main()