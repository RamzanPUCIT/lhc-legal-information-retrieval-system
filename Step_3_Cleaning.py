import os, re

os.makedirs("lhc_clean", exist_ok=True)

for f in os.listdir("lhc_text"):

    if f.endswith(".txt"):
        text = open(f"lhc_text/{f}", encoding="utf-8").read().lower()
        text = re.sub(r"\d+|[^\w\s]", "", text)
        text = re.sub(r"\s+", " ", text)

        open(f"lhc_clean/{f}", "w", encoding="utf-8").write(text.strip())
        print("Cleaned:", f)

print("Text preprocessing done")
