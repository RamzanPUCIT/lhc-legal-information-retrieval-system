import pickle
from sklearn.metrics.pairwise import cosine_similarity

# load saved data
inverted_index = pickle.load(open("inverted_index.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
doc_names = pickle.load(open("doc_names.pkl", "rb"))

# user query
query = "illegal detention"

# vectorize query
query_vec = vectorizer.transform([query])

# cosine similarity
scores = cosine_similarity(query_vec, tfidf_matrix)[0]

# show top results
results = sorted(zip(doc_names, scores), key=lambda x: x[1], reverse=True)

print("Top Relevant Documents:")
for doc, score in results[:10]:
    print(doc, round(score, 3))
