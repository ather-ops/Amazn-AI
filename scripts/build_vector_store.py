import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
from src.data_loader import load_dataset
from src.chunking import create_chunks
from src.vectordb import (
    create_langchain_documents,
    load_langchain_embedding,
    create_vector_store,
    save_vector_store
)
from src.config import VECTOR_STORE_PATH

def main():
    print("=" * 60)
    print("BUILDING AMAZN AI VECTOR DATABASE")
    print("=" * 60)

    # Load Dataset
    df = load_dataset()
    print("Dataset Loaded")

    # Create Chunks
    chunks, metadata, ids = create_chunks(df)
    print(f"Chunks Created : {len(chunks)}")

    # Create LangChain Documents
    documents = create_langchain_documents(
        chunks,
        metadata
    )
    print(f"Documents Created : {len(documents)}")

    # Load Embedding Model
    embedding_model = load_langchain_embedding()
    print("Embedding Model Loaded")

    # Create Vector Store
    vector_store = create_vector_store(
        documents,
        embedding_model
    )
    print("Vector Store Created")

    # Save Vector Store
    save_vector_store(
        vector_store,
        VECTOR_STORE_PATH
    )

    print("\nVector Store Successfully Saved!")


if __name__ == "__main__":
    main()