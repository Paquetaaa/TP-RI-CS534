import sys
import re

if len(sys.argv) < 4:
    print("Usage: python searchTF.py <extension> \"query\" <Documents number>")
    sys.exit(1)

DOC_NUMBER = int(sys.argv[3])
EXT = sys.argv[1]
QUERY = sys.argv[2].lower().split()

INDEX_FILE = f"./IndexInverse/indexInverse{EXT}.txt"
TF_FILE = f"./VecteurTF/vecteurTF{EXT}.txt"

# Charger index inversé
index_inv = {}
for line in open(INDEX_FILE, encoding="utf8"):
    tID, docs = line.split(":")
    tID = int(tID)
    docs = list(map(int, docs.split()))
    index_inv[tID] = docs
print(f"Index inversé chargé : {len(index_inv)} termes")

# Charger TF par document
tf_doc = {}
for line in open(TF_FILE, encoding="utf8"):
    parts = line.split()
    doc_base = line.replace(EXT, "")
    # Extraire le numéro après le tiret
    match = re.search(r'(\d+)', doc_base)
    if match:
        docID = int(match.group(1))
    else:
        print(f"Nom de fichier inattendu : {line}")
        continue
    vec = {int(t.split(":")[0]): int(t.split(":")[1]) for t in parts[1:]}
    tf_doc[docID] = vec
print(f"TF des documents chargé : {len(tf_doc)} documents")

scores = {}



# On simplifie : on retrouve directement les tID via vocabulaire
VOC_FILE = f"./vocabulary/vocabulaire{EXT}.txt"
vocab = [w.strip() for w in open(VOC_FILE)]
term_id = {w:i+1 for i,w in enumerate(vocab)}

for w in QUERY:
    if w not in term_id:
        continue
    tID = term_id[w]

    if tID not in index_inv:
        continue

    for doc in index_inv[tID]:
        scores[doc] = scores.get(doc, 0) + tf_doc[doc].get(tID, 0)

# Trier
results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

for doc, score in results[:DOC_NUMBER]:
    ## On affiche les 3 meilleurs résultats
    print(f"Doc {doc} - score {score:.4f}")

with open("resultatsTFquery.html", "w", encoding="utf8") as out:
    out.write("<h1>Résultats de la recherche</h1>\n<ul>\n")
    for doc, score in results[:DOC_NUMBER]:
        out.write(
            f'<li><a href="./Collection/{doc}{EXT}">Document {doc}</a> '
            f' – score {score:.4f}</li>\n')
    out.write("</ul>\n")
print("Résultats écrits dans resultatsTFquery.html")
