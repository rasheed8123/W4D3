import fitz  # PyMuPDF
import streamlit as st
from chunking import *

st.set_page_config(page_title="RAG Chunking Strategy Visualizer", layout="wide")
st.title("📄 RAG Chunking Strategy Visualizer")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
text = ""

if uploaded_file:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    st.subheader("📃 Extracted Text Sample")
    st.text_area("Text Preview", text[:2000] + "...", height=200)

    # Choose strategy
    strategy = st.selectbox("🔧 Choose Chunking Strategy", [
        "Fixed Word Count",
        "Sliding Window",
        "Sentence-Based",
        "Paragraph-Based",
        "Recursive Chunking"
    ])

    # Choose parameters
    if strategy == "Fixed Word Count":
        chunk_size = st.slider("Chunk size (words)", 20, 500, 100, step=10)
        chunks = fixed_word_chunks(text, chunk_size)

    elif strategy == "Sliding Window":
        chunk_size = st.slider("Chunk size (words)", 20, 500, 100)
        overlap = st.slider("Overlap (words)", 0, chunk_size - 1, 20)
        chunks = sliding_window_chunks(text, chunk_size, overlap)

    elif strategy == "Sentence-Based":
        chunks = sentence_chunks(text)

    elif strategy == "Paragraph-Based":
        chunks = paragraph_chunks(text)

    elif strategy == "Recursive Chunking":
        chunk_size = st.slider("Chunk size (characters)", 100, 1000, 500, step=50)
        overlap = st.slider("Overlap (characters)", 0, 300, 50, step=10)
        chunks = recursive_chunk(text, chunk_size, overlap)

    # Show explanation
    st.subheader("ℹ️ Strategy Explanation")
    explanation = {
        "Fixed Word Count": "Splits the text into fixed-size word chunks. Fast but may break sentence meaning.",
        "Sliding Window": "Creates overlapping chunks to preserve context. Useful for semantic search.",
        "Sentence-Based": "Splits using sentence boundaries. Good for QA and summarization.",
        "Paragraph-Based": "Preserves paragraph structure. Great for manuals or structured documents.",
        "Recursive Chunking": "Smart splitting that respects newlines and punctuation. Used in LangChain."
    }
    st.info(explanation[strategy])

    # Show chunks
    st.subheader(f"🧩 Chunks Generated: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        with st.expander(f"Chunk {i+1}"):
            st.write(chunk)
            st.code(f"Words: {len(chunk.split())} | Characters: {len(chunk)}")
