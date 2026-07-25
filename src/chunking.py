import pandas as pd
from nltk.tokenize import sent_tokenize

def sentence_splitting(text: str, max_sentences: int = 2):
    """
    Split text into sentence chunks.
    Args:
        text (str): Input text.
        max_sentences (int): Number of sentences per chunk.
    Returns:
        list: List of text chunks.
    """
    if pd.isna(text):
        return []
    sentences = sent_tokenize(str(text))
    chunks = []
    for i in range(0, len(sentences), max_sentences):
        chunk = " ".join(sentences[i:i + max_sentences]).strip()
        if chunk:
            chunks.append(chunk)
    return chunks


def create_chunks(df):
    """
    Create chunks, metadata and unique IDs.
    Args:
        df (pd.DataFrame): Cleaned Amazon dataset.
    Returns:
        tuple:
            all_chunks (list)
            metadata_chunks (list)
            ids (list)
    """
    all_chunks = []
    metadata_chunks = []
    ids = []
    for _, row in df.iterrows():
        # Rich text used for embeddings
        combined_text = f"""
Product Name: {row.get("product_name", "")}
Category:
{row.get("category", "")}

Description:
{row.get("about_product", "")}
Average Rating:
{row.get("rating", "")}
Customer Reviews:
{row.get("review_content", "")}
""".strip()
        chunks = sentence_splitting(combined_text)
        for chunk_index, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata = {
                # Product Information
                "product_id": row.get("product_id"),
                "product_name": row.get("product_name"),
                "category": row.get("category"),

                # Pricing
                "discounted_price": row.get("discounted_price"),
                "actual_price": row.get("actual_price"),
                "discount_percentage": row.get("discount_percentage"),

                # Ratings
                "rating": row.get("rating"),
                "rating_count": row.get("rating_count"),

                # Product Details
                "about_product": row.get("about_product"),
                "review_title": row.get("review_title"),
                "review_content": row.get("review_content"),

                # Images & Links
                "product_link": row.get("product_link"),
                "img_link": row.get("img_link")
            }

            metadata_chunks.append(metadata)
            ids.append(
                f"{row.get('product_id')}_chunk_{chunk_index}"
            )
    return all_chunks, metadata_chunks, ids