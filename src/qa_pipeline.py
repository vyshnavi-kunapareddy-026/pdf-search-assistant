# src/qa_pipeline.py

from typing import List, Tuple
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import requests
import time


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks


class PDFQAEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.Client(Settings(anonymized_telemetry=False))
        self.collection = self.client.get_or_create_collection("pdf_chunks")
        self.chunks = []

    def build_vector_store(self, text: str):
        """
        Clear existing collection and build new vector store from chunks.
        """
        self.client.delete_collection("pdf_chunks")
        self.collection = self.client.get_or_create_collection("pdf_chunks")
        self.chunks = chunk_text(text)
        embeddings = self.model.encode(self.chunks, convert_to_numpy=True)

        for i, (chunk, embedding) in enumerate(zip(self.chunks, embeddings)):
            self.collection.add(
                documents=[chunk],
                embeddings=[embedding.tolist()],
                ids=[f"chunk-{i}"]
            )

    def _search(self, query: str, k: int = 5) -> List[str]:
        query_embedding = self.model.encode([query])[0].tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return results["documents"][0]

    def summarize(self, k: int = 10) -> str:
        summary_chunks = self.chunks[:k]
        prompt = (
            "Summarize the following document content:\n\n"
            + "\n\n".join(summary_chunks)
            + "\n\nSummary:"
        )
        return self._call_llm(prompt)

    def answer(self, query: str, history: List[Tuple[str, str]] = None) -> str:
        history = history or []
        top_chunks = self._search(query)
        context = "\n\n".join(top_chunks)
        dialogue = "\n".join([f"User: {q}\nAssistant: {a}" for q, a in history])
        prompt = f"{dialogue}\nUser: {query}\n\nContext:\n{context}\n\nAnswer:"
        return self._call_llm(prompt)

    def _call_llm(self, prompt: str) -> str:
        try:
            start = time.time()
            prompt_length = len(prompt)
            print(f"[DEBUG] Prompt length: {prompt_length} chars")

            # Use LLaMA for large prompts, Gemma for smaller ones
            model_name = "llama3" if prompt_length > 3000 else "gemma:2b"

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            duration = time.time() - start
            print(f"[LLM] ({model_name}) Response took {duration:.2f} seconds")
            response.raise_for_status()
            return response.json()["response"].strip()

        except Exception as e:
            print(f"[ERROR] LLM call failed: {e}")
            return "Sorry, I couldn't process that."