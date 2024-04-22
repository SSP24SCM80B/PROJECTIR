import os
import pickle
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Determine the path to index.pkl
index = os.path.join(os.path.dirname(__file__), '..' ,'spiders', 'index.pkl')

# Load the index.pkl file
with open(index, 'rb') as f:
    index = pickle.load(f)

# Continue with your Flask app setup
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([doc['document'] for doc in index.values()])

Webapp = Flask(__name__)

@Webapp.route('/query', methods=['POST'])
def query():
    queryJson = request.json
    query = queryJson.get('query', '')

    Vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(Vector, tfidf_matrix).flatten()
   #change k value here to get top k results
    k = min(5, len(cosine_similarities))
    top_indices_of_k = cosine_similarities.argsort()[-k:][::-1]

    results = [{'cosine_similarity': cosine_similarities[idx], 
                'document_name': index[idx]['document_name'],} for idx in  top_indices_of_k]
    return jsonify(results)


if __name__ == '__main__':
   Webapp.run(debug=True)