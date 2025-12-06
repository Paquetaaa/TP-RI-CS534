import sys
import math

if len(sys.argv) < 3:
    print("Usage: python3 queryVector.py <extension> \"requete\"")
    sys.exit(1)

EXT = sys.argv[1]
QUERY = sys.argv[2].lower().split()

VOC_FILE = f"./vocabulary/vocabulaire{EXT}.txt"
DF_FILE = f"./df/df{EXT}.txt"
LIST_FILE = "./cacm/Collection"

# Charger vocabulaire
vocab = [w.strip() for w in open(VOC_FILE, encoding="utf8")]
term_id = {w: i+1 for i, w in enumerate(vocab)}

# Charger DF
df = {}
for line in open(DF_FILE, encoding="utf8"):
    w, d = line.split()
    w = w.lstrip("#")
    d = d.lstrip("#")
    df[w] = int(d)

# Nombre total de docs
print("Lecture de la liste des documents...")
with open(LIST_FILE, "r", encoding="utf8") as f:
    print(f"Fichier : {LIST_FILE}")
    documents = [line.strip() for line in f if line.strip()]
print(f"Nombre de documents à traiter : {len(documents)}")

print(f"Documents à traiter : {len(documents)} fichiers")
N = len(documents)
print(f"Nombre total de documents : {N}")

# TF de la requête
tf = {}
for w in QUERY:
    if w in term_id:
        tf[w] = tf.get(w, 0) + 1

#TF-IDF de la requête
query_vector = {}
for w in tf:
    idf = math.log(N / df.get(w, 1))
    query_vector[term_id[w]] = tf[w] * idf


## On renvoie le query_vector, a chaque terme son tID et son poids calculé avec TF-IDF
print(query_vector)

