import os
import sys

# Add root path so src imports work
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import gradio as gr
from src.pdf_reader import extract_full_text
from src.qa_pipeline import PDFQAEngine

qa_engine = PDFQAEngine()
chat_history = []


def upload_pdf(file):
    if file is None:
        return "❌ Please upload a PDF file first."
    text = extract_full_text(file.name)
    qa_engine.build_vector_store(text)
    return "✅ PDF uploaded and indexed successfully!"


def summarize_pdf():
    return qa_engine.summarize(k=10)


def chat(query):
    response = qa_engine.answer(query, history=chat_history)
    chat_history.append((query, response))
    return chat_history


with gr.Blocks() as demo:
    gr.Markdown("# 📄 AI PDF Chat Assistant\nChat with your documents easily!")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🛠 Upload & Process")
            pdf_file = gr.File(label="Upload your PDF", file_types=[".pdf"])
            upload_button = gr.Button("📤 Upload & Process PDF")
            upload_status = gr.Textbox(label="", interactive=False)

            gr.Markdown("### 📚 Get a Summary")
            summary_button = gr.Button("🧠 Summarize PDF")
            summary_output = gr.Textbox(label="Summary", lines=10)

        with gr.Column(scale=2):
            gr.Markdown("### 💬 Ask Questions")
            chatbot = gr.Chatbot()
            user_input = gr.Textbox(label="Your Question", placeholder="Ask something about the PDF...")
            send_button = gr.Button("➡️ Ask")

    # Function Bindings
    upload_button.click(upload_pdf, inputs=[pdf_file], outputs=[upload_status])
    summary_button.click(summarize_pdf, outputs=[summary_output])
    send_button.click(chat, inputs=[user_input], outputs=[chatbot])

demo.launch()
