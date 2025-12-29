import pickle, os
from flask import Flask, render_template, request, send_from_directory
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# load saved data
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
doc_names = pickle.load(open("doc_names.pkl", "rb"))

PDF_FOLDER = "lhc_pdf"

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    message = ""

    if request.method == "POST":
        query = request.form["query"].strip().lower()

        # empty / very small query
        if len(query) < 3:
            message = "❌ Please enter a meaningful query (at least 3 characters)."

        else:
            q_vec = vectorizer.transform([query])
            scores = cosine_similarity(q_vec, tfidf_matrix)[0]

            ranked = [(doc, score) for doc, score in zip(doc_names, scores) if score > 0]
            ranked.sort(key=lambda x: x[1], reverse=True)

            if ranked:
                results = ranked[:10]
            else:
                message = "⚠️ No relevant documents found for your query."

    return render_template(
        "index.html",
        results=results,
        query=query,
        message=message
    )

@app.route("/open/<filename>")
def open_pdf(filename):
    pdf_name = filename.replace(".txt", ".pdf")
    return send_from_directory(PDF_FOLDER, pdf_name)

@app.route("/download/<filename>")
def download_pdf(filename):
    pdf_name = filename.replace(".txt", ".pdf")
    return send_from_directory(PDF_FOLDER, pdf_name, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
