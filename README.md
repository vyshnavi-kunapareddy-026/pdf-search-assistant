pdf-search-assistant/        # → project root
│
├── .env.example             # sample env file (OPENAI_API_KEY, etc.)
├── .gitignore               # Python, venv, Streamlit, Docker, etc.
├── Dockerfile               # container recipe
├── README.md                # full project guide & screenshots
├── requirements.txt         # pinned packages for pip install
│
├── data/                    # small, static assets
│   └── eval.json            # handful of Q&A pairs for smoke‑tests
│
├── src/                     # importable Python package
│   ├── __init__.py
│   ├── config.py            # env + path helpers
│   ├── pdf_reader.py        # text extraction (PyMuPDF)
│   ├── chunker.py           # token‑aware text splitters
│   ├── embedding.py         # model‑agnostic embedder
│   ├── vector_store.py      # Chroma wrapper (add, query)
│   ├── qa_pipeline.py       # LangChain RetrievalQA glue
│   └── index_manager.py
|   |---vector_store.py
        rag_q.py
        search.py
│
├── ui/                      # Streamlit front‑end
│   ├── app.py               # main Streamlit app
│   └── utils.py             # UI helpers (theme, favicon, etc.)
│
├── tests/                   # pytest suite
│   ├── conftest.py
│   ├── test_ingest.py
│   ├── test_search.py
│   └── test_ui.py
│
└── assets/                  # logos, GIF demo, screenshots
    ├── logo.png
    └── demo.gif