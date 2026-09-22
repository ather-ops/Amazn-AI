from pathlib import Path
PROJECT_ROOT=Path(__file__).resolve().parent.parent

VECTOR_STORE_DIR=PROJECT_ROOT/"vector_store"
FAISS_INDEX_PATH=VECTOR_STORE_DIR/"product_indeex.faiss"
DOCUMENTS_PATH=VECTOR_STORE_DIR/"product_documents.json"
METADATA_PATH=VECTOR_STORE_DIR/"product_metedata.json"
