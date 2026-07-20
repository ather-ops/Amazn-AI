import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "cleaned",
    "amazon_cleaned.csv"
)
VECTOR_STORE_PATH = os.path.join(
    BASE_DIR,
    "vector_store",
    "faiss_index"
)
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gemini-2.5-flash"
TOP_K = 3
BATCH_SIZE = 80