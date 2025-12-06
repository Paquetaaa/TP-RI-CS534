import os
import sys

SRC_DIR = "./Collection"

vocabulaire = {}


if len(sys.argv) != 2:
    print("Usage: python count.py <file_extension>, ex : .stem")
    sys.exit(1)

# Lecture de la liste des fichiers
for filename in os.listdir(SRC_DIR):
    if filename.endswith(sys.argv[1]):
        print(f"Processing file: {filename}")

        with open(os.path.join(SRC_DIR, filename), "r", encoding="utf8") as f:
            text = f.read()

        for word in text.split():
            if word:  # ignore chaînes vides
                vocabulaire[word] = vocabulaire.get(word, 0) + 1

# Tri par fréquence décroissante
sorted_vocab = sorted(vocabulaire.items(), key=lambda x: x[1], reverse=True)

# Écriture des résultats
OUTPUT_FILE = "count" + sys.argv[1]+ ".txt"
with open(OUTPUT_FILE, "w", encoding="utf8") as f:
    for rank, (word, count) in enumerate(sorted_vocab, start=1):
        f.write(f"{rank} {count} {word}\n")

print(f"Vocabulaire size: {len(vocabulaire)} words.")
print(f"Résultats écrits dans {OUTPUT_FILE}")
