# src/search.py
from typing import List, Dict, Any
from src.embedding import embed_texts
from src.vector_store import get_or_create_collection

def search_query(
    question: str,
    collection_name: str = "my-pdf-docs",
    k: int = 5,
) -> Dict[str, Any]:
    """
    Embed the question and return top‑k similar chunks from the vector store.

    Returns a dict with keys: documents, metadatas, distances
    """
    # 1. Embed the question
    query_vec = embed_texts([question])[0]

    # 2. Load the collection
    collection = get_or_create_collection(collection_name)

    # 3. Query Chroma
    results = collection.query(
        query_embeddings=[query_vec],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )
    # Unwrap single‑query results
    return {
        "documents": results["documents"][0],
        "metadatas":  results["metadatas"][0],
        "distances":  results["distances"][0],
    }
