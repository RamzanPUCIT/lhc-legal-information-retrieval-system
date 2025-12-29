import os, pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# ---------- rebuild data (simple & safe) ----------

docs, doc_names = [], []

for f in os.listdir("lhc_clean"):
    if f.endswith(".txt"):
        docs.append(open(f"lhc_clean/"+f, encoding="utf-8").read())
        doc_names.append(f)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# inverted index (simple)
inverted_index = {}
for i, text in enumerate(docs):
    for w in set(text.split()):
        inverted_index.setdefault(w, []).append(i+1)

# ---------- save everything ----------

pickle.dump(inverted_index, open("inverted_index.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(tfidf_matrix, open("tfidf_matrix.pkl", "wb"))
pickle.dump(doc_names, open("doc_names.pkl", "wb"))

print("Step-10: All data saved successfully")
