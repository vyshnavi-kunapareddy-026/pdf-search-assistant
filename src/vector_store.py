# src/vector_store.py
from typing import List
from chromadb import PersistentClient

chroma_client = PersistentClient(path="./chroma_store")


def get_or_create_collection(name="pdf_chunks"):
    return chroma_client.get_or_create_collection(
        name=name,
        embedding_function=None
    )


def add_chunks_to_collection(
    collection,
    chunks: List[str],
    embeddings: List[List[float]],
    source: str
):
    ids = [f"{source}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": source, "chunk": i} for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )
