# src/pdf_reader.py

import fitz  # PyMuPDF
from typing import List


def extract_text_by_page(pdf_path: str) -> List[str]:
    """
    Extracts text from each page of a PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        List[str]: List of text content per page.
    """
    page_texts = []
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()
            page_texts.append(text.strip())
        doc.close()
    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")

    return page_texts


def extract_full_text(pdf_path: str) -> str:
    """
    Extracts all text from the entire PDF as a single string.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: All text concatenated.
    """
    pages = extract_text_by_page(pdf_path)
    return "\n".join(pages)
