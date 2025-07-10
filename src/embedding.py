# src/embedding.py

'''''from InstructorEmbedding import INSTRUCTOR

# Load the InstructorEmbedding model
model = INSTRUCTOR("hkunlp/instructor-base")


def embed_texts(texts):
    """
    Generates embeddings for a list of text chunks using an instruction to guide the embedding purpose.

    Args:
        texts (List[str]): List of text strings to embed.

    Returns:
        List[List[float]]: Embedding vectors for the input texts.
    """
    instruction = "Represent the document for question answering"

    # Instructor model expects input as list of [instruction, text] pairs
    inputs = [[instruction, text] for text in texts]
    return model.encode(inputs)'''''
from sentence_transformers import SentenceTransformer

# Load a fast, lightweight embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    """
    Returns embeddings for a list of text chunks.
    """
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    return embeddings

