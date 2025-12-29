import pickle
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
doc_names = pickle.load(open("doc_names.pkl", "rb"))

print("=== Legal Document Search System ===")
print("Type 'exit' to quit\n")

while True:
    query = input("Enter query: ").strip().lower()

    if query == "exit":
        print("Exiting system...")
        break

    if len(query) < 3:
        print("❌ Please enter a meaningful query (min 3 letters)")
        continue

    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, tfidf_matrix)[0]

    results = [(d, s) for d, s in zip(doc_names, scores) if s > 0]

    if not results:
        print("⚠️ No relevant documents found")
        continue

    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop Results:")
    for d, s in results[:5]:
        print(d, round(s, 3))

    print("-" * 30)
