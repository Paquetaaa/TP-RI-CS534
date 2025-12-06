import sys
import os
import re

# Vérification arguments
if len(sys.argv) != 2:
    print("Usage: python3 indexInverse.py <extension> (.stem/.nowords/.clean)")
    sys.exit(1)

EXT = sys.argv[1]
SRC_DIR = "./Collection"
LIST_FILE = f"./cacm/Collection"

VOC_FILE = f"./vocabulary/vocabulaire{EXT}.txt"
OUTPUT = f"indexInverse{EXT}.txt"

## On récupère le vocabulaire

vocab = []
with open(VOC_FILE, "r", encoding="utf8") as f:
    for line in f:
        w = line.strip()
        if w:
            vocab.append(w)

term_id = {w: i+1 for i, w in enumerate(vocab)}

print(f"Vocabulaire : {len(vocab)} termes")

## On charge tous les documetns de la collection

print("Lecture de la liste des documents...")
with open(LIST_FILE, "r", encoding="utf8") as f:
    print(f"Fichier : {LIST_FILE}")
    documents = [line.strip() for line in f if line.strip()]
print(f"Nombre de documents à traiter : {len(documents)}")

print(f"Documents à traiter : {len(documents)} fichiers")

## Extraction des paires (termeID, docID)

pairs = []

for doc in documents:
    # Retirer l'extension
    doc_base = doc.replace(EXT, "")
    # Extraire le numéro après le tiret
    match = re.search(r'(\d+)', doc_base)
    if match:
        docID = int(match.group(1))
    else:
        print(f"Nom de fichier inattendu : {doc}")
        continue
    path = os.path.join(SRC_DIR, doc)
    with open(path, "r", encoding="utf8") as f:
        words = set(f.read().split())      # set = présence unique, pas de doublons

    for w in words:
        if w in term_id:
            pairs.append((term_id[w], docID))

print(f"Extraction des paires : {len(pairs)} paires")


# Tri selon (termeID, docID)


pairs.sort(key=lambda x: (x[0], x[1]))

### Ecriture du résultat dans le fichier d'index inversé

with open(OUTPUT, "w", encoding="utf8") as out:

    current_term = None
    current_docs = []

    for tID, dID in pairs:
        if tID != current_term:
            # écrire l’ancien groupe
            if current_term is not None:
                out.write(f"{current_term} : {' '.join(map(str, current_docs))}\n")

            # réinitialiser
            current_term = tID
            current_docs = []

        # ajouter doc sans doublon
        if not current_docs or current_docs[-1] != dID:
            current_docs.append(dID)

    # dernier terme
    if current_term is not None:
        out.write(f"{current_term} : {' '.join(map(str, current_docs))}\n")

print(f"Index inversé généré -> {OUTPUT}")
