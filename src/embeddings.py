from src.config import EMBEDDING_MODEL
from sentence_transformers import SentenceTransformer

def load_embedding_model():
    """
    Load the Sentence Transformer model.
    """
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    return model

def create_embeddings(model, all_chunks, batch_size=64):
    """
    Convert text chunks into embeddings.
    """
    embeddings = model.encode(
        all_chunks,
        batch_size=batch_size,
        show_progress_bar=True
    )
    return embeddings