# Creates, saves and loads the FAISS Vector Database.

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_core.documents import Document


def create_langchain_documents(chunks, metadata):
    """
    Convert chunks and metadata into LangChain Document objects.
    """
    documents = []
    for chunk, meta in zip(chunks, metadata):
        doc = Document(
            page_content=chunk,
            metadata=meta
        )
        documents.append(doc)
    return documents

def load_langchain_embedding():
    """
    Returns HuggingFace embedding model
    used by LangChain FAISS.
    """
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embedding_model

def create_vector_store(documents, embedding_model):
    """
    Creates FAISS vector database.
    Args:
        documents : List[Document]
        embedding_model
    Returns:
        FAISS Vector Store
    """
    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )
    return vector_store

def save_vector_store(vector_store, path):
    """
    Saves FAISS locally.
    """
    vector_store.save_local(path)
    print(f"\nVector Store saved at:\n{path}")


def load_vector_store(path, embedding_model):
    """
    Loads existing FAISS index.
    """
    vector_store = FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return vector_store

def similarity_search(
    vector_store,
    query,
    k=5
):
    """
    Returns top k similar documents.
    """
    results = vector_store.similarity_search(
        query=query,
        k=k
    )
    return results