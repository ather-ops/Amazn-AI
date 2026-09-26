# artifacts
import faiss
import json
from sentence_transformers import SentenceTransformer
from src.llm import ask_amazon as generate_answer
from src.paths import (
    FAISS_INDEX_PATH,
    DOCUMENTS_PATH,
    METADATA_PATH,
)
from src.paths import (SUPPORT_INDEX_PATH,
    CHUNKS_PATH)
model = SentenceTransformer("all-MiniLM-L6-v2")
# Product Rag
index = faiss.read_index(str(FAISS_INDEX_PATH))
with open(DOCUMENTS_PATH, "r", encoding="utf-8") as f:
    documents = json.load(f)
with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

# Service Rag
support_index=faiss.read_index(str(SUPPORT_INDEX_PATH))
with open(CHUNKS_PATH,"r",encoding="utf-8") as file:
    support_chunks=json.load(file)

# Product Rag retrive
def retrieve_product_queries(query, top_k=5):
    query_embd = model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")
    faiss.normalize_L2(query_embd)
    distances, indices = index.search(query_embd, top_k)
    results = []
    for score, idx in zip(distances[0], indices[0]):
        if idx == -1:
            continue
        results.append({
            "document": documents[idx],
            "metadata": metadata[idx],
            "distance": float(score)
        })

    return results

# ask Product Rag
def ask_product_rag(query):
    results = retrieve_product_queries(query)
    context = "\n\n -- \n\n".join(
        f"""{r["document"]}
Product ID   : {r["metadata"].get("product_id")}
Product Link : {r["metadata"].get("product_link")}
Product Img  : {r["metadata"].get("img_link")}
"""
        for r in results
    )
    return generate_answer(query, context)

# test product rag
query="Suggest a Samsung Type C cable"
print(ask_product_rag(query))

# service rag retrival
def retrive_service_quires(query,top_k=5):
    query_embed=model.encode([query],convert_to_numpy=True).astype("float32")
    faiss.normalize_L2(query_embed)
    distances,indices=support_index.search(query_embed,top_k)
    results=[]
    for  score,idx in zip(distances[0],indices[0]):
        if idx == -1:
            continue
        results.append({
            "chunks":support_chunks[idx],
            "distances":float(score)
        })
    return results
# Test the servicebRag
def ask_service_rag(query):
    results = retrive_service_quires(query)
    context = "\n\n---\n\n".join(
        f"""Source: Support PDF, Page {r["chunk"]["page"]}{r["chunk"]["text"]}
"""
        for r in results
    )
    return generate_answer(query, context)
