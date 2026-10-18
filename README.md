<div align="center">

<a href="#-pipeline"><img src="assets/readme/hero.svg" width="100%" alt="1,000 judgments, one search bar: animated overview of the LHC legal search engine"/></a>

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

![Domain](https://img.shields.io/badge/Domain-Legal%20Tech-141E30?style=flat-square)
![Task](https://img.shields.io/badge/Task-Information%20Retrieval-35577D?style=flat-square)
![Corpus](https://img.shields.io/badge/Corpus-1000%20judgments-F2C94C?style=flat-square)
![Course](https://img.shields.io/badge/M.Phil%20AI-PUCIT-1f6f8b?style=flat-square)

</div>

---

## 📌 Overview

Finding a relevant precedent among thousands of court judgments is slow when all you have is a folder of PDFs. This project builds a **complete search engine for Lahore High Court (LHC) judgments**, from collecting the documents to ranking them for a user's query.

It scrapes judgment PDFs from the LHC public judgments portal, converts them to text, cleans and indexes them, and ranks documents with **TF-IDF + cosine similarity**. Users search through a **Flask web app** that shows the top-10 matches with their relevance scores and lets them open or download the original judgment.

<table>
<tr>
<td align="center"><b>1,000</b><br/>judgments</td>
<td align="center"><b>13</b><br/>pipeline steps</td>
<td align="center"><b>3</b><br/>interfaces<br/><sub>web · desktop · CLI</sub></td>
<td align="center"><b>Top-10</b><br/>ranked results</td>
<td align="center"><b>1-click</b><br/>open / download PDF</td>
</tr>
</table>

---

## ✨ Highlights

<table>
<tr>
<td width="50%"><a href="#-pipeline"><img src="assets/readme/card-01-data.svg" width="100%" alt="1,000 Lahore High Court judgments downloaded"/></a></td>
<td width="50%"><a href="#-ir-techniques-implemented"><img src="assets/readme/card-02-index.svg" width="100%" alt="Inverted index: each word points to the judgments that contain it"/></a></td>
</tr>
<tr>
<td width="50%"><a href="#how-a-search-request-flows"><img src="assets/readme/card-03-ranking.svg" width="100%" alt="Cosine ranking of TF-IDF vectors"/></a></td>
<td width="50%"><a href="#-interfaces"><img src="assets/readme/card-04-interfaces.svg" width="100%" alt="Three interfaces: Flask web app, Tkinter desktop app and CLI"/></a></td>
</tr>
</table>

---

## 🔄 Pipeline

```mermaid
flowchart LR
    A["🌐 LHC judgments portal"] -->|"requests"| B["📄 lhc_pdf/<br/>1,000 PDFs"]
    B -->|"PyMuPDF"| C["📝 lhc_text/<br/>raw text"]
    C -->|"lowercase · remove digits<br/>and punctuation"| D["🧹 lhc_clean/<br/>clean text"]
    D --> E["📚 Inverted index"]
    D --> F["🔢 TF-IDF matrix"]
    E --> G[("💾 .pkl files")]
    F --> G
    G --> H["🔎 Query → TF-IDF vector<br/>→ cosine similarity"]
    H --> I["🏆 Top-10 ranked judgments"]
```

### How a search request flows

```mermaid
sequenceDiagram
    actor U as User
    participant W as Flask app
    participant M as TF-IDF model
    participant S as PDF store
    U->>W: Submit query (e.g. "illegal detention")
    W->>W: Validate (minimum 3 characters)
    W->>M: vectorizer.transform(query)
    M-->>W: Cosine scores for all documents
    W-->>U: Top-10 judgments with scores
    U->>W: Click Open or Download
    W->>S: Fetch original PDF
    S-->>U: Judgment PDF
```

---

## 🧰 IR Techniques Implemented

The project is built as a step-by-step series of scripts, each adding one classical IR building block:

| Step | Script | What it does |
|:--:|:--|:--|
| 1 | `Step_1_Scrap.py` | Downloads judgment PDFs from the LHC public portal |
| 2 | `Step_2_pdf_to_text.py` | Extracts text from every PDF with PyMuPDF |
| 3 | `Step_3_Cleaning.py` | Lowercases, removes digits and punctuation, normalises whitespace |
| 4 | `Step_4_Indexing.py` | Builds an inverted index (term → document IDs) |
| 5 | `Step_5_Bool.py` | Boolean retrieval with AND / OR / NOT (demonstrated on a sample index) |
| 6 | `Step_6_phrase_matching.py` | Exact phrase search over the cleaned corpus |
| 7 | `Step_7_wildcard_query.py` | Prefix wildcard matching such as `viol*` (demonstrated on a sample index) |
| 8 | `Step_8_TFIDF.py` | TF-IDF vectorisation of the whole corpus |
| 9 | `Step_9_cosine_similarity.py` | Ranks documents by cosine similarity to a query |
| 10 | `Step_10_save_results.py` | Persists the vectorizer, TF-IDF matrix, document names and inverted index |
| 11 | `Step_11_load_and_search.py` | Loads the saved model and runs a search |
| 12 | `Step_12_final_search.py` | Interactive command-line search (top-5) |
| 13 | `Step_13_search_ui.py` | Tkinter desktop search app (top-10) |
| — | `app.py` | **Flask web app** with ranked results, open and download actions |

---

## 💻 Interfaces

| Interface | Entry point | Highlights |
|:--|:--|:--|
| 🌐 **Web app** | `app.py` + `templates/` + `static/` | Ranked table, relevance score, open PDF in browser, download PDF |
| 🖱️ **Desktop app** | `Step_13_search_ui.py` | Dark-themed Tkinter window, top-10 results with scores |
| ⌨️ **CLI** | `Step_12_final_search.py` | Fast terminal search loop, type `exit` to quit |

All three reject queries shorter than 3 characters and hide documents with zero similarity, so users never see irrelevant noise.

<!--
  Tip: add a screenshot or GIF of the web app here, e.g.
  <img src="assets/demo.gif" width="90%" alt="Search demo"/>
-->

---

## 🚀 Getting Started

```bash
git clone https://github.com/RamzanPUCIT/lhc-legal-information-retrieval-system.git
cd lhc-legal-information-retrieval-system
pip install requests pymupdf scikit-learn flask
```

```bash
python Step_1_Scrap.py            # 1. download judgments into lhc_pdf/
python Step_2_pdf_to_text.py      # 2. extract text into lhc_text/
python Step_3_Cleaning.py         # 3. clean text into lhc_clean/
python Step_10_save_results.py    # 4. build TF-IDF + inverted index, save .pkl files
python app.py                     # 5. start the web app → http://127.0.0.1:5000
```

> [!NOTE]
> Judgment PDFs, extracted text and the generated `.pkl` model files are git-ignored, so run steps 1–4 once before starting the app. Please keep the scraping rate modest out of respect for the court's public server.

---

## 🗂️ Repository Structure

```
lhc-legal-information-retrieval-system/
├── Step_1_Scrap.py ... Step_13_search_ui.py   # Step-by-step IR pipeline
├── app.py                                      # Flask web application
├── templates/
│   └── index.html                              # Search page
├── static/
│   └── style.css                               # Styling
├── .gitignore
├── assets/readme/                              # Animated README graphics (SVG)
└── README.md
```

---

## 🔭 Future Work

- [ ] Evaluate ranking quality with a labelled query set (Precision@k, MAP, nDCG)
- [ ] Add BM25 and compare it against TF-IDF
- [ ] Dense retrieval with legal-domain sentence embeddings, then hybrid (sparse + dense) search
- [ ] Retrieval-Augmented Generation: an LLM assistant that answers legal questions and cites the retrieved judgments
- [ ] Containerise with Docker and deploy as a public demo

---

## 👨‍💻 Author

**Muhammad Ramzan** · M.Phil Artificial Intelligence, PUCIT (University of the Punjab), Lahore

[![LinkedIn](https://img.shields.io/badge/LinkedIn-ramzan--ai-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ramzan-ai)
[![GitHub](https://img.shields.io/badge/GitHub-RamzanPUCIT-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamzanPUCIT)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:founders786@gmail.com)

<div align="center">

⭐ **If this project helped you, consider giving it a star!** ⭐


</div>
