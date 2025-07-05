import re
import nltk
import spacy
from langchain.text_splitter import RecursiveCharacterTextSplitter

nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

# --- Chunking Strategies ---

def fixed_word_chunks(text, chunk_size=100):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def sliding_window_chunks(text, chunk_size=100, overlap=20):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

def sentence_chunks(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def paragraph_chunks(text):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs

def recursive_chunk(text, chunk_size=500, overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)
