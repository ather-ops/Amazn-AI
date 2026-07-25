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

from src.llm import load_llm
from src.prompt import prompt

print("=" * 70)
print("AMAZN AI MODULE TEST")
print("=" * 70)

# Load Dataset
df = load_dataset()
print("Dataset Loaded")

# Chunking
chunks, metadata, ids = create_chunks(df)
print(f"Chunks Created : {len(chunks)}")
print(f"Metadata       : {len(metadata)}")
print(f"IDs            : {len(ids)}")

# Embeddings
model = load_embedding_model()
embeddings = create_embeddings(
    model,
    chunks
)

print(f"Embedding Shape : {embeddings.shape}")

# LangChain Documents
documents = create_langchain_documents(
    chunks,
    metadata
)

print(f"Documents Created : {len(documents)}")

# Vector Store
embedding_model = load_langchain_embedding()
vector_store = create_vector_store(
    documents,
    embedding_model
)
print("Vector Store Created")

# Save Vector Store
save_vector_store(
    vector_store,
    "vector_store/faiss_index"
)
print("Vector Store Saved")

# Similarity Search
results = similarity_search(
    vector_store,
    "gaming laptop",
    k=3
)
print("\nTop Results\n")
for i, doc in enumerate(results, 1):
    print("=" * 70)
    print(f"Result {i}")
    print("Product :", doc.metadata["product_name"])
    print("Price   :", doc.metadata["discounted_price"])
    print("Rating  :", doc.metadata["rating"])
    print("Link    :", doc.metadata.get("product_link", "N/A"))
    print("Image   :", doc.metadata.get("img_link", "N/A"))

# Prompt
print("\nPrompt Loaded Successfully")
print(type(prompt))

# Gemini
llm = load_llm()
print("Gemini Loaded Successfully")
print(llm)

print("\n" + "=" * 70)
print("ALL MODULES WORKING SUCCESSFULLY")
print("=" * 70)