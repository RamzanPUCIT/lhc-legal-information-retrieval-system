import pickle
import tkinter as tk
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import messagebox

# ================= LOAD SAVED DATA =================
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
doc_names = pickle.load(open("doc_names.pkl", "rb"))

# ================= SEARCH FUNCTION =================
def search():
    query = entry.get().strip().lower()
    results.delete(1.0, tk.END)

    if len(query) < 3:
        messagebox.showwarning(
            "Invalid Query",
            "Please enter a meaningful legal query (min 3 characters)"
        )
        return

    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, tfidf_matrix)[0]

    ranked = [(d, s) for d, s in zip(doc_names, scores) if s > 0]
    ranked.sort(key=lambda x: x[1], reverse=True)

    if not ranked:
        results.insert(tk.END, "❌ No relevant legal documents found.\n")
        return

    for i, (doc, score) in enumerate(ranked[:10], 1):
        results.insert(
            tk.END,
            f"{i}. {doc}\n   Similarity Score: {round(score,3)}\n\n"
        )

# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("AI Legal Document Search System")
root.geometry("900x650")
root.config(bg="#0f172a")

# ================= HEADER =================
header = tk.Frame(root, bg="#020617", height=120)
header.pack(fill="x")

tk.Label(
    header,
    text="AI LEGAL DOCUMENT SEARCH SYSTEM",
    bg="#020617",
    fg="#38bdf8",
    font=("Segoe UI", 24, "bold")
).pack(pady=(25, 5))

tk.Label(
    header,
    text="Developed by Muhammad Ramzan",
    bg="#020617",
    fg="white",
    font=("Segoe UI", 16, "bold")
).pack()

tk.Label(
    header,
    text="PUCIT | M.Phil Artificial Intelligence | AI Project",
    bg="#020617",
    fg="#94a3b8",
    font=("Segoe UI", 12)
).pack(pady=5)

# ================= SEARCH PANEL =================
panel = tk.Frame(root, bg="#020617", bd=2, relief="ridge")
panel.pack(pady=25, padx=40, fill="x")

tk.Label(
    panel,
    text="Enter Legal Search Query",
    bg="#020617",
    fg="white",
    font=("Segoe UI", 14, "bold")
).pack(anchor="w", padx=20, pady=10)

entry = tk.Entry(panel, font=("Segoe UI", 15))
entry.pack(padx=20, pady=10, fill="x")

tk.Button(
    panel,
    text="SEARCH DOCUMENTS",
    font=("Segoe UI", 13, "bold"),
    bg="#22c55e",
    fg="black",
    height=2,
    command=search
).pack(pady=15)
# EXIT BUTTON (CLEAR & CENTER)
tk.Button(
    panel,
    text="EXIT APPLICATION",
    font=("Segoe UI", 12, "bold"),
    bg="#ef4444",
    fg="white",
    height=2,
    width=20,
    command=root.destroy
).pack(pady=(0, 20))

# ================= RESULTS AREA =================
results_frame = tk.Frame(root, bg="#0f172a")
results_frame.pack(padx=40, pady=10, fill="both", expand=True)

tk.Label(
    results_frame,
    text="Search Results",
    bg="#0f172a",
    fg="#38bdf8",
    font=("Segoe UI", 16, "bold")
).pack(anchor="w")

results = tk.Text(
    results_frame,
    font=("Consolas", 12),
    bg="#020617",
    fg="white",
    insertbackground="white",
    height=14,
    bd=2,
    relief="sunken"
)
results.pack(pady=10, fill="both", expand=True)

# ================= FOOTER (WITH EXIT BUTTON) =================
footer = tk.Frame(root, bg="#020617", height=70)
footer.pack(fill="x", side="bottom")

tk.Label(
    footer,
    text="© Muhammad Ramzan | AI Legal Search Engine | PUCIT",
    bg="#020617",
    fg="#94a3b8",
    font=("Segoe UI", 10)
).pack(pady=5)

tk.Button(
    footer,
    text="EXIT",
    font=("Segoe UI", 11, "bold"),
    bg="#ef4444",
    fg="white",
    width=14,
    command=root.destroy
).pack(pady=5)

# ================= RUN APP =================
root.mainloop()
