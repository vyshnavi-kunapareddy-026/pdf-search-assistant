# src/chunker.py

from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(pages: List[str], chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """
    Splits a list of page texts into token-aware chunks using LangChain's splitter.

    Args:
        pages (List[str]): List of raw page texts.
        chunk_size (int): Max chunk size (in tokens/chars).
        chunk_overlap (int): Overlap between chunks.

    Returns:
        List[str]: List of chunked text blocks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    full_text = "\n".join(pages)
    chunks = splitter.split_text(full_text)
    return chunks
