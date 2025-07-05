# 🧠 Plagiarism Detector - Semantic Similarity Analyzer

This is a simple web-based tool to detect semantic similarity and potential plagiarism across multiple text inputs using embeddings. It supports both **Sentence Transformers** (semantic) and **TF-IDF** (lexical) models for comparison.

---

## 🌐 Features

- 📝 Dynamic input text boxes
- 🔍 Semantic similarity comparison using:
  - Sentence Transformers (pretrained)
  - TF-IDF vectorization
- 📊 Similarity matrix with percentage scores
- 🚨 Clone detection with >80% similarity highlighting
- 🔄 Switch between models via dropdown
- ⚡ Lightweight frontend using HTML + Flask backend

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/plagiarism-detector.git
cd plagiarism-detector
2. Create & Activate Virtual Environment
bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash

pip install -r requirements.txt
🚀 Run the App
bash

python app.py
Visit: http://localhost:5000

🧪 Example Use
Inputs:

vbnet

Text 1: I love apple
Text 2: Apple is good for health
Output Similarity Matrix:

pgsql

           | Text 1 | Text 2
----------------------------
Text 1     | 100%   | 59.42%
Text 2     | 59.42% | 100%
Similarity > 80% is highlighted as potential clone (configurable).

🧠 Embedding Models Used
Sentence Transformers:
all-MiniLM-L6-v2 – captures semantic meaning

Powered by Hugging Face sentence-transformers

TF-IDF:
Traditional word vectorizer

Captures lexical overlap, no deep meaning

📂 Project Structure
csharp

plagiarism-detector/
├── app.py                  # Flask backend
├── requirements.txt
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # (Optional) Styling
└── venv/                   # Virtual environment