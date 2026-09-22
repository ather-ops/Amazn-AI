# Step 1: Imports
import faiss
import pandas as pd
import json
from sentence_transformers import SentenceTransformer
from src.llm  import ask_amazon as generate_answer
from src.paths import(
    FAISS_INDEX_PATH,
    DOCUMENTS_PATH,
    METADATA_PATH
)
index = faiss.read_index(str(FAISS_INDEX_PATH))
with open(DOCUMENTS_PATH,"rb", encoding="utf-8") as f:
    documents=json.load(f)
metadata=pd.read_pickle(METADATA_PATH)
model=SentenceTransformer("all-MiniLM-L6-v2")
print(index.ntotal)
print(len(documents))

def retrieve_queries(query, top_k=5):
    query_embd = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embd, top_k)
    results = []
    for score, idx in zip(distances[0], indices[0]):
        if idx == -1:
            continue
        results.append({
            "document": documents[idx],
            "metadata": metadata.iloc[idx].to_dict(),
            "distance": float(score),
        })
    return results

def ask_amazn(query):
    results = retrieve_queries(query)
    context = "\n\n -- \n\n".join(
        f"""{r["document"]}
Product ID   : {r["metadata"].get("product_id")}
Product Link : {r["metadata"].get("product_link")}
Product Img  : {r["metadata"].get("img_link")}
"""
        for r in results
    )
    return generate_answer(query, context)

# test query
query="Suggest a Samsung Type C cable"
print(ask_amazn(query))
