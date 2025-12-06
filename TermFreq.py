# Nombre d'apparitions moyen par document d'un terme

import os

def term_frequency(term:str,extension:str):
    directory = "./Collection"
    total_count = 0
    doc_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath):
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                    data = text.split(" ")
                    count = 0
                    for word in data:
                        if word == term:
                            count = count + 1
                    total_count += count
                    doc_count += 1

    moyenne = total_count / doc_count if doc_count > 0 else 0
    return moyenne

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python TermFreq.py <term> <file_extension>, ex : .stem")
        sys.exit(1)

    term = sys.argv[1]
    extension = sys.argv[2]

    freq = term_frequency(term, extension)
    print(f"Le terme '{term}' apparait en moyenne {freq} fois par document avec l'extension '{extension}'.")