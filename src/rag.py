from src.prompt import load_prompt
def retrieve_documents(
    vector_store,
    query,
    top_k=3
):
    return vector_store.similarity_search(
        query=query,
        k=top_k * 3
    )

def filter_documents(
    documents,
    top_k=3,
    category=None,
    min_price=None,
    max_price=None,
    rating=None,
    product_name=None,
):
# Filter retrieved documents using metadata.
    filtered = []
    for doc in documents:
        meta = doc.metadata
        if (
            category
            and category.lower()
            not in str(meta.get("category", "")).lower()
        ):
            continue
        if (
            min_price is not None
            and meta.get("discounted_price", 0) < min_price
        ):
            continue
        if (
            max_price is not None
            and meta.get("discounted_price", float("inf")) > max_price
        ):
            continue
        if (
            rating is not None
            and meta.get("rating", 0) < rating
        ):
            continue
        if (
            product_name
            and product_name.lower()
            not in str(meta.get("product_name", "")).lower()
        ):
            continue
        filtered.append(doc)
        if len(filtered) >= top_k:
            break
    return filtered
def build_context(documents):
# Build context passed to the LLM.
    contexts = []
    for doc in documents:
        meta = doc.metadata
        contexts.append(
            f"""
Product Name: {meta.get("product_name")}
Category: {meta.get("category")}
Discounted Price: {meta.get("discounted_price")}
Actual Price: {meta.get("actual_price")}
Rating: {meta.get("rating")}
Rating Count: {meta.get("rating_count")}
Product Link:
{meta.get("product_link")}
Image Link:
{meta.get("img_link")}
Description:
{doc.page_content}
"""
        )
    return "\n\n".join(contexts)


def rag_with_llm(
    query,
    vector_store,
    llm,
    top_k=3,
    category=None,
    min_price=None,
    max_price=None,
    rating=None,
    product_name=None,
):

     # Complete RAG Pipeline.
    retrieved_docs = retrieve_documents(
        vector_store,
        query,
        top_k
    )
    # Metadata Filtering
    filtered_docs = filter_documents(
        retrieved_docs,
        top_k=top_k,
        category=category,
        min_price=min_price,
        max_price=max_price,
        rating=rating,
        product_name=product_name,
    )

    if not filtered_docs:
        return (
            "I couldn't find a matching product in the current Amazon dataset.",
            []
        )
    # Build Context
    context = build_context(filtered_docs)
    # Prompt
    prompt = load_prompt()
    chain = prompt | llm
    response = chain.invoke(
        {
            "context": context,
            "question": query
        }
    )
    # Return
    return response.content, filtered_docs