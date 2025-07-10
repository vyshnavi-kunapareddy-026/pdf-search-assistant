
# 🤖 AI-Powered PDF Search Assistant

Tired of manually scanning through long PDFs just to find that one paragraph you need?
This assistant helps you **upload any PDF, ask questions about it, and get summaries** — all running *locally* on your machine.

---

## 🌟 What It Does

- 📂 Upload any PDF (books, papers, invoices — anything!)
- 🧠 Get a smart summary of what’s inside
- 💬 Ask it questions in plain English and get contextual answers
- 🔒 100% local — No API keys or internet needed

---

## 🛠️ Built With

- **Python** – backend logic
- **Gradio** – beautiful and simple user interface
- **PyMuPDF** – PDF text extraction
- **SentenceTransformers** – for embeddings
- **ChromaDB** – local vector search engine
- **Ollama** – runs your local LLM (e.g., Mistral, LLaMA3, Gemma)

---

## 🗂️ Project Structure

```
pdf-search-assistant/
├── src/                  # core logic
│   ├── pdf_reader.py     # PDF text extractor
│   └── qa_pipeline.py    # QA engine: embed, search, answer
├── ui/
│   └── app.py            # Gradio interface
├── data/                 # where your uploaded PDFs go
├── assets/               # images, icons, etc.
├── requirements.txt      # dependencies
├── .env.example
└── README.md             # this file
```

---

## 🚀 Getting Started

### 1. Clone and install dependencies

```bash
git clone https://github.com/your-username/pdf-search-assistant.git
cd pdf-search-assistant
pip install -r requirements.txt
```

### 2. Start Ollama with your model of choice

```bash
ollama run gemma:2b
```

(You can replace `gemma:2b` with `llama3`, `mistral`, or `yi` if installed)

### 3. Run the app

```bash
python ui/app.py
```

Go to [http://localhost:7860](http://localhost:7860) and start chatting with your PDF!

---

## 🧠 How It Works (Behind the Scenes)

1. We read the PDF and split it into text chunks.
2. Those chunks are converted into embeddings using SentenceTransformers.
3. ChromaDB helps us search for the most relevant chunks.
4. Your query + those chunks are sent to a local LLM via Ollama.
5. The model replies with a contextual answer.

It’s like ChatGPT — but with a memory of your document, and all on your machine.

---

## 🎯 Example Use Cases

- 🧾 Ask questions about academic papers
- 📚 Chat with textbooks or course notes
- 📄 Extract insights from contracts, reports, resumes
- 🧪 Summarize long technical documentation

---

## 🔮 What’s Next?

- Multiple PDF support
- Source references in answers
- More powerful summarization
- Streamed LLM responses

---

## 🧑‍💻 Author

Made by Vyshnavi Kunapareddy

---

## 🪪 License

MIT License – Free to use, modify, and share.
