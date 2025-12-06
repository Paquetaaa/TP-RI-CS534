import os
import sys

SRC_DIR = "./Collection"
vocabulaire = set()

if len(sys.argv) != 2:
    print("Usage: python vocabulaire.py <file_extension>, ex : .stem")
    sys.exit(1)

for filename in os.listdir(SRC_DIR):
    print(sys.argv[1])
    if filename.endswith(sys.argv[1]):
        with open(os.path.join(SRC_DIR, filename), "r", encoding="utf8") as f:
            text = f.read()
        words = text.split(" ")
        vocabulaire.update(words)

vocabulaire = sorted(vocabulaire)
filename = "vocabulaire"+sys.argv[1]+".txt"
print(f"Writing vocabulary to {filename}...")
with open(filename, "w", encoding="utf8") as f:
    for word in vocabulaire:
        f.write(word + "\n")

print(f"Vocabulaire size: {len(vocabulaire)} words.")


