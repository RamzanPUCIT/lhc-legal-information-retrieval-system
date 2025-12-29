import os
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [open(f"lhc_clean/{f}", encoding="utf-8").read()
        for f in os.listdir("lhc_clean") if f.endswith(".txt")]

tfidf = TfidfVectorizer().fit_transform(docs)

print("TF-IDF ready | Docs:", tfidf.shape[0], "Words:", tfidf.shape[1])
