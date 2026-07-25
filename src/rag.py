from src.prompt import prompt
def rag_with_llm(
    query,
    vector_store,
    embedding_model,
    llm,
    top_k=3,
    category=None,
    min_price=None,
    max_price=None,
    rating=None,
    product_name=None,
):
    # Step 1 : Embed Query
    query_embedding = embedding_model.encode([query])[0]
    # Step 2 : Retrieve
    retrieved_docs = vector_store.similarity_search_by_vector(
        query_embedding,
        k=top_k * 3
    )
    # Step 3 : Metadata Filtering
    filtered_docs = []
    for doc in retrieved_docs:
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
            and meta.get("discounted_price", 99999999) > max_price
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

        filtered_docs.append(doc)

        if len(filtered_docs) >= top_k:
            break

    # Step 4 : Build Context
    context = ""
    for doc in filtered_docs:
        context += f"""
Product Name:
{doc.metadata.get("product_name")}
Category:
{doc.metadata.get("category")}
Price:
{doc.metadata.get("discounted_price")}
Actual Price:
{doc.metadata.get("actual_price")}
Rating:
{doc.metadata.get("rating")}

Product Link:
{doc.metadata.get("product_link")}
Image Link:
{doc.metadata.get("img_link")}
Description:
{doc.page_content}

"""
    # Step 5 : LLM
    chain = prompt | llm
    response = chain.invoke(
        {
            "context": context,
            "question": query,
        }
    )
    # Step 6 : Return
    return response.content, filtered_docs