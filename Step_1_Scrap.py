import requests
from pathlib import Path
from datetime import datetime

TOTAL_PDFS = 1000
SAVE_FOLDER = Path("lhc_pdf")
START_NUMBER = 6500

SAVE_FOLDER.mkdir(exist_ok=True)

def make_url(year, num):
    return f"http://sys.lhc.gov.pk/appjudgments/{year}LHC{num}.pdf"

def download_pdf(url):
    name = url.split("/")[-1]
    path = SAVE_FOLDER / name

    if path.exists():
        return False

    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200 and "pdf" in r.headers.get("Content-Type", "").lower():
            path.write_bytes(r.content)
            return True
    except:
        pass

    return False

downloaded = 0
year = datetime.now().year

while downloaded < TOTAL_PDFS and year >= 2000:
    num = START_NUMBER

    while downloaded < TOTAL_PDFS and num > 0:
        url = make_url(year, num)
        if download_pdf(url):
            downloaded += 1
            print(f"{downloaded} PDFs downloaded")
        num -= 1

    year -= 1

print("Download Complete")
