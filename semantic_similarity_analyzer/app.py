from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)
st_model = SentenceTransformer('all-MiniLM-L6-v2')  # Sentence Transformer model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    texts = [t.strip().lower() for t in data.get('texts', []) if t.strip()]
    mode = data.get('mode', 'st')  # st = sentence transformer, tfidf = TF-IDF

    if mode == 'st':
        embeddings = st_model.encode(texts, normalize_embeddings=True)
    elif mode == 'tfidf':
        vectorizer = TfidfVectorizer()
        embeddings = vectorizer.fit_transform(texts).toarray()
    else:
        return jsonify({'error': 'Unknown embedding mode'}), 400

    sim_matrix = cosine_similarity(embeddings)
    sim_matrix = np.round(sim_matrix * 100, 2).tolist()

    return jsonify({
        'similarity_matrix': sim_matrix
    })

if __name__ == '__main__':
    app.run(debug=True)
