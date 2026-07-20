"""
chunking.py
This module is responsible for:
1. Splitting long text into smaller chunks.
2. Creating chunk IDs.
3. Preparing metadata for Vector Database.
"""

import pandas as pd
from nltk.tokenize import sent_tokenize

def sentence_splitting(text: str, max_sentences: int = 2):
    """
    Split text into chunks based on number of sentences.
    Args:
        text (str): Input text
        max_sentences (int): Number of sentences per chunk
    Returns:
        list: List of text chunks
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
    Creates text chunks, metadata and unique IDs.
    Args:
        df (DataFrame)
    Returns:
        all_chunks
        metadata_chunks
        ids
    """
    all_chunks = []
    metadata_chunks = []
    ids = []
    for _, row in df.iterrows():
        combined_text = f"""
        {row.get("product_name","")}
        {row.get("about_product","")}
        {row.get("category","")}
        """
        chunks = sentence_splitting(combined_text)
        for index, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata = {
                "product_id": row.get("product_id"),
                "product_name": row.get("product_name"),
                "category": row.get("category"),
                "discounted_price": row.get("discounted_price"),
                "actual_price": row.get("actual_price"),
                "discount_percentage": row.get("discount_percentage"),
                "rating": row.get("rating"),
                "rating_count": row.get("rating_count"),
                "product_link": row.get("product_link"),
                "img_link": row.get("img_link")
            }
            metadata_chunks.append(metadata)
            ids.append(f"{row.get('product_id')}_chunk_{index}")
    return all_chunks, metadata_chunks, ids