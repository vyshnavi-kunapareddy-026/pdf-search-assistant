# src/index_manager.py
from src.pdf_reader import extract_text_by_page
from src.chunker import chunk_text
from src.embedding import embed_texts
from src.vector_store import get_or_create_collection, add_chunks_to_collection

def ingest_pdf(pdf_path: str, collection_name: str = "my-pdf-docs"):
    pages = extract_text_by_page(pdf_path)
    chunks = chunk_text(pages)
    embeddings = embed_texts(chunks)

    collection = get_or_create_collection(collection_name)
    add_chunks_to_collection(collection, chunks, embeddings, source=pdf_path)
    return collection
