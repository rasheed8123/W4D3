# 🧠 RAG Chunking Strategy Visualizer

A web application that allows users to upload PDF documents and explore various chunking strategies used in Retrieval-Augmented Generation (RAG) pipelines. The tool provides visualizations, explanations, and metadata to better understand the trade-offs of different chunking methods.

---

## 🚀 Features

- 📄 **PDF Upload & Text Extraction**  
  Upload large PDFs and extract text using high-performance parsing (via PyMuPDF).

- 🧩 **Chunking Strategy Explorer**  
  Choose from various chunking methods including:
  - Fixed-size
  - Overlapping windows
  - Sentence-based
  - NLTK-based
  - spaCy-based
  - LangChain recursive strategy

- 📚 **Strategy Explanations**  
  Learn how each chunking method works and when to use it.

- 🔍 **Chunk Visualization**  
  See how text is split, view chunk size, overlap, and boundary preservation.

- 📊 **Metadata Display**  
  Each chunk shows:
  - Size (in characters/tokens)
  - Start & end indexes
  - Overlap count
  - Strategy used

---

## 🏗️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **PDF Parsing**: [PyMuPDF](https://pymupdf.readthedocs.io/)
- **NLP Processing**: [spaCy](https://spacy.io/), [NLTK](https://www.nltk.org/)
- **Chunking Engine**: [LangChain](https://python.langchain.com/)
- **Language**: Python 3.10+

---

## 📂 File Structure

rag_chunking_strategy/
├── app.py # Streamlit application logic
├── chunking.py # Core chunking strategy implementations
├── utils.py # Text extraction and utility functions
├── requirements.txt # All required Python packages
└── README.md # This file

yaml


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rag-chunking-visualizer.git
cd rag_chunking_strategy
2. Create Virtual Environment
bash

python -m venv venv
source venv/bin/activate  # on Linux/Mac
venv\Scripts\activate     # on Windows
3. Install Dependencies
bash

pip install -r requirements.txt
4. Run the App
bash

streamlit run app.py
📌 Chunking Strategies Explained
Strategy	Description
Fixed-size	Splits text into equal-length chunks
Overlapping	Like fixed-size but with sliding window overlap
Sentence-based	Splits by sentence boundaries (using spaCy or NLTK)
Recursive	Uses LangChain's RecursiveCharacterTextSplitter
Semantic-aware	Ensures coherent idea-based splits (future work)

🧪 Exploration Goals
Analyze which strategy works best for:

Retrieval accuracy

Latency

Semantic coherence

Observe effects of chunk size and overlap on retrieval performance

