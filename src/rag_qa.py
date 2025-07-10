# src/rag_qa.py

import ollama
from src.search import search_query

def answer_question_rag(question: str, collection_name: str = "my-pdf-docs", k: int = 5) -> str:
    # Step 1: Retrieve top-k relevant chunks
    hits = search_query(question, collection_name, k)
    context = "\n\n".join(hits["documents"])

    # Step 2: Create prompt
    prompt = f"""You are a helpful assistant. Answer the user's question using only the context below.

Context:
{context}

Question: {question}
Answer:"""

    # Step 3: Query Ollama (Mistral model)
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip()
