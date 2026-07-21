from src.data_loader import load_dataset
from src.chunking import create_chunks

from src.embeddings import (
    load_embedding_model,
    create_embeddings,
)

from src.vectordb import (
    load_langchain_embedding,
    create_vector_store,
    save_vector_store,
    similarity_search,
    create_langchain_documents
)

df = load_dataset()
chunks, metadata, ids = create_chunks(df)
model = load_embedding_model()
embeddings = create_embeddings(
    model,
    chunks
)
documents = create_langchain_documents(
    chunks,
    metadata
)
print(f"Documents : {len(documents)}")

embedding_model = load_langchain_embedding()
vector_store = create_vector_store(
    documents,
    embedding_model
)

print("Vector Store Created")

# Save

save_vector_store(
    vector_store,
    "vector_store/faiss_index"
)

results = similarity_search(
    vector_store,
    "gaming laptop",
    k=3
)

print("\nTop Results\n")
for i, doc in enumerate(results, 1):
    print("=" * 60)
    print(f"Result {i}")

    print(doc.metadata["product_name"])
    print(doc.metadata["discounted_price"])
    print(doc.metadata["rating"])