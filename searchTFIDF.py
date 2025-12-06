import sys
import math
import re

if len(sys.argv) < 4:
    print("Usage: python3 searchTFIDF.py <extension> \"query\" <Documents number>")
    sys.exit(1)

EXT = sys.argv[1]
QUERY = sys.argv[2].lower().split()
DOC_NUMBER = int(sys.argv[3])

VOC_FILE = f"./vocabulary/vocabulaire{EXT}.txt"
DF_FILE = f"./df/df{EXT}.txt"
LIST_FILE = "./cacm/Collection"
DOC_TFIDF = f"./VecteurTFIDF/vecteurTFIDF{EXT}.txt"
INDEX_FILE = f"./IndexInverse/indexInverse{EXT}.txt"



# On récupère le vocabulaire et le DF

vocab = [w.strip() for w in open(VOC_FILE, encoding="utf8")]
term_id = {w: i+1 for i, w in enumerate(vocab)}

df = {}
for line in open(DF_FILE, encoding="utf8"):
    a, b = line.split()
    w = a.lstrip("#")
    d = b.lstrip("#")
    df[w] = int(d)

# On récupère le nombre total de documents

print("Lecture de la liste des documents...")
with open(LIST_FILE, "r", encoding="utf8") as f:
    print(f"Fichier : {LIST_FILE}")
    documents = [line.strip() for line in f if line.strip()]
N = len(documents)
print(f"Nombre total de documents : {N}")


# Construction du vecteur TF-IDF de la requête
tf_req = {}
for w in QUERY:
    if w in term_id:
        tf_req[w] = tf_req.get(w, 0) + 1

query_vec = {}
for w, tf in tf_req.items():
    idf = math.log(N / df.get(w, 1))
    query_vec[term_id[w]] = tf * idf


# On récupère les vecteurs TF-IDF des documents

tfidf_docs = {}
for line in open(DOC_TFIDF, encoding="utf8"):
    parts = line.split()

    ##doc = int(parts[0])
    doc_name = parts[0]
    # Retirer l'extension
    doc_base = doc_name.replace(EXT, "")
    # Extraire le numéro après le tiret
    match = re.search(r'(\d+)', doc_base)
    if match:
        docID = int(match.group(1))
    else:
        print(f"Nom de fichier inattendu : {doc_base}")
        continue

    weights = {int(p.split(":")[0]): float(p.split(":")[1]) for p in parts[1:]}
    tfidf_docs[docID] = weights

# Calcul de score, avecc TF-IDF
scores = {}

for doc, vec in tfidf_docs.items():
    score = 0
    for tID, wq in query_vec.items():
        wd = vec.get(tID, 0)
        score += wq * wd
    if score > 0:
        scores[doc] = score

# Trie et affiche le 5 docuemnts les plus pertinents
results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

for doc, score in results[:DOC_NUMBER]:
    print(f"Doc {doc} - score {score:.4f}")

with open("resultatsTF-IDFquery.html", "w", encoding="utf8") as out:

    out.write("<h1>Résultats de la recherche</h1>\n<ul>\n")
    for doc, score in results[:DOC_NUMBER]:
        out.write(
            f'<li><a href="./Collection/{doc}{EXT}">Document {doc}</a> '
            f' – score {score:.4f}</li>\n')
    out.write("</ul>\n")
print("Résultats enregistrés dans resultatsTF-IDFquery.html")
