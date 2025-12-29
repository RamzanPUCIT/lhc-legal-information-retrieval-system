import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs, names = [], []

for f in os.listdir("lhc_clean"):
    if f.endswith(".txt"):
        docs.append(open(f"lhc_clean/{f}", encoding="utf-8").read())
        names.append(f)

tfidf = TfidfVectorizer().fit_transform(docs + ["illegal detention"])
scores = cosine_similarity(tfidf[-1], tfidf[:-1])[0]

for n, s in sorted(zip(names, scores), key=lambda x: x[1], reverse=True):
    print(n, round(s, 3))
