import sys
import os
import math

if len(sys.argv) != 2:
    print("Usage: python vecteurTFIDF.py <extension>")
    print("Exemples : .clean   .nowords   .stem")
    sys.exit(1)

EXT = sys.argv[1]
SRC_DIR = "./Collection"
LIST_FILE = f"./cacm/Collection"

VOC_FILE = f"./vocabulary/vocabulaire{EXT}.txt"
DF_FILE = f"./df/df{EXT}.txt"  
OUTPUT = f"vecteurTFIDF{EXT}.txt"

 
# Chargement du vocabulaire


if not os.path.exists(VOC_FILE):
    print(f"Erreur : vocabulaire introuvable : {VOC_FILE}")
    sys.exit(1)

vocab = []
with open(VOC_FILE, "r", encoding="utf8") as f:
    for line in f:
        w = line.strip()
        if w:
            vocab.append(w)

term_id = {w: i+1 for i, w in enumerate(vocab)}

print(f"[OK] Vocabulaire chargé ({len(vocab)} termes).")

 
#Chargement des DF
 

if not os.path.exists(DF_FILE):
    print(f"Erreur : fichier DF introuvable : {DF_FILE}")
    sys.exit(1)

df = {}
## Le format du fichier df est : #mot #df on doit bien enlever les '#'
with open(DF_FILE, "r", encoding="utf8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        
        w = parts[0].lstrip("#")   # enlever les '#'
        d = parts[1].lstrip("#")   

        if w in term_id:
            df[w] = int(d)


 
# Nombre total de documents
 
with open(LIST_FILE, "r", encoding="utf8") as f:
    print(f"Fichier : {LIST_FILE}")
    documents = [line.strip() for line in f if line.strip()]

N = len(documents)
print(f"[OK] Nombre de documents : {N}")

 
#Calcul de l’IDF
 
## On utilise la formule IDF = log(N / df)
idf = {}
for w in vocab:
    if w in df and df[w] > 0:
        idf[w] = math.log(N / df[w])
    else:
        idf[w] = 0.0

 
##Génération des vecteurs TF-IDF
 

with open(OUTPUT, "w", encoding="utf8") as out:

    for doc in documents:

        filepath = os.path.join(SRC_DIR, doc)

        with open(filepath, "r", encoding="utf8") as f:
            words = f.read().split()

        # --- TF ---
        tf = {}
        for w in words:
            if w in term_id:
                tf[w] = tf.get(w, 0) + 1

        # --- TF-IDF ---
        vector = []
        for w in tf:
            tfidf = tf[w] * idf[w]
            if tfidf > 0:
                vector.append(f"{term_id[w]}:{tfidf:.6f}")

        ## On trie par ID du terme
        vector.sort(key=lambda x: int(x.split(":")[0]))

        # docID = nom du fichier sans extension
        doc_id = doc.replace(EXT, "")
        out.write(f"{doc_id} " + " ".join(vector) + "\n")

print(f"[OK] Fichier TF-IDF généré : {OUTPUT}")
