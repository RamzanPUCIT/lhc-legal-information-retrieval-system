import os

def phrase_search(p):
    return [f for f in os.listdir("lhc_clean")
            if f.endswith(".txt") and
            p.lower() in open(f"lhc_clean/{f}", encoding="utf-8").read()]

print("Matches:", phrase_search("illegal detention"))