import os

index = {}
doc_id = 0

for f in os.listdir("lhc_clean"):

    if f.endswith(".txt"):
        doc_id += 1
        words = open(f"lhc_clean/{f}", encoding="utf-8").read().split()

        for w in set(words):
            index.setdefault(w, []).append(doc_id)

print("Inverted index ready")
print("Unique words:", len(index))
