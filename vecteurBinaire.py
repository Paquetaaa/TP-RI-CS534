import os
import sys



# Vérification des arguments
if len(sys.argv) != 2:
    print("Usage: python vecteurBinaire.py <extension>")
    print("Exemples : .clean   .nowords   .stem")
    sys.exit(1)


EXT = sys.argv[1]                      
SRC_DIR = "./Collection"
LIST_FILE = f"./cacm/Collection"
VOC_FILE = f"./vocabulary/vocabulaire{EXT}.txt"    
OUTPUT = f"vecteurBinaire{EXT}.txt"

#Charge le vocabulaire

if not os.path.exists(VOC_FILE):
    print(f"Erreur : fichier vocabulaire introuvable : {VOC_FILE}")
    sys.exit(1)

vocab = []
with open(VOC_FILE, "r", encoding="utf8") as f:
    print("Chargement du vocabulaire...")
    print(f"Fichier : {VOC_FILE}")
    for line in f:
        word = line.strip()
        if word:
            vocab.append(word)
print(f"Nombre de mots dans le vocabulaire : {len(vocab)}")

# Création du dictionnaire mot -> ID
print("Création du dictionnaire mot -> ID...")
term_id = {word: i+1 for i, word in enumerate(vocab)}
print("Dictionnaire créé.")
print(f"Exemple d'entrées : {list(term_id.items())[:5]}")

# Lecture de la liste des documents
print("Lecture de la liste des documents...")
with open(LIST_FILE, "r", encoding="utf8") as f:
    print(f"Fichier : {LIST_FILE}")
    documents = [line.strip() for line in f if line.strip()]
print(f"Nombre de documents à traiter : {len(documents)}")

# Création du fichier vecteur binaire
print("Génération du fichier de vecteurs binaires...")
with open(OUTPUT, "w", encoding="utf8") as out:

    for doc in documents:
        print(f"Traitement du document : {doc}")
        filepath = os.path.join(SRC_DIR, doc)

        with open(filepath, "r", encoding="utf8") as f:
            words = f.read().split()

        # Ensemble des mots présents dans le document
        present_words = set(w for w in words if w in term_id)
        print(f"Nombre de mots présents dans le vocabulaire : {len(present_words)}")

        # Convertir en termID:1
        binary_vector = [f"{term_id[w]}:1" for w in present_words]

        # Trier selon l'ID du terme
        binary_vector.sort(key=lambda x: int(x.split(":")[0]))

        # docID = nom du fichier sans extension
        doc_id = doc.split(".")[0]

        out.write(f"{doc_id} " + " ".join(binary_vector) + "\n")

print(f"Fichier {OUTPUT} généré.")
