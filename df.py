import os
import sys
SRC_DIR = "./Collection"

# Dictionnaire pour stocker la fréquence documentaire
document_frequency = {}

if len(sys.argv) != 2:
    print("Usage: python df.py <file_extension>, ex : .stem")
    sys.exit(1)

# On parcourt tous les fichiers dans le dossier
for filename in os.listdir(SRC_DIR):
    print(filename)
    print(sys.argv[1])
    if filename.endswith(sys.argv[1]):

        print(f"Processing file: {filename}")
        with open(os.path.join(SRC_DIR, filename), "r", encoding="utf8") as f:
            text = f.read()
        
        # On récupère les mots uniques dans le document, si un mot apparait deux fois dans le même document, on ne le compte qu'une fois.
        words = set(word.strip() for word in text.split(" ") if word.strip())
        
        # On met à jour la fréquence documentaire pour chaque mot
        for word in words:
            document_frequency[word] = document_frequency.get(word, 0) + 1

# On écrit les résultats dans le fichier df.txt
filename = "df"+sys.argv[1]+".txt"
with open(filename, "w", encoding="utf8") as f:
    for word, df in document_frequency.items():
        f.write(f"#{word} #{df}\n")