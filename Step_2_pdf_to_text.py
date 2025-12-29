import os
import pymupdf

PDF_DIR = "lhc_pdf"
TXT_DIR = "lhc_text"
os.makedirs(TXT_DIR, exist_ok=True)

for pdf in os.listdir(PDF_DIR):
    if pdf.endswith(".pdf"):
        doc = pymupdf.open(f"{PDF_DIR}/{pdf}")
        text = ""

        for page in doc:
            text += page.get_text()

        if text.strip():
            with open(f"{TXT_DIR}/{pdf[:-4]}.txt", "w", encoding="utf-8") as f:
                f.write(text)

        print("Done:", pdf)

print("PDF → Text completed FAST")
