from pathlib import Path
PROJECT_ROOT=Path(__file__).resolve().parent.parent

VECTOR_STORE_DIR=PROJECT_ROOT/"vector_store"
FAISS_INDEX_PATH=VECTOR_STORE_DIR/"product_index.faiss"
DOCUMENTS_PATH=VECTOR_STORE_DIR/"product_documents.json"
METADATA_PATH=VECTOR_STORE_DIR/"product_metadata.json"
SUPPORT_INDEX_PATH=VECTOR_STORE_DIR/"support_index.faiss"
CHUNKS_PATH=VECTOR_STORE_DIR/"support_chunks.json"

print("Paths woks Sucessfully!")
