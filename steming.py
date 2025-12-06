import os
from nltk.stem import PorterStemmer

input_dir = "Collection"
stopwords_file = "cacm/common_words"

ps = PorterStemmer()

# Charger la liste des mots vides dans un set (rapide à chercher)
with open(stopwords_file, "r", encoding="utf8") as f:
    stopwords = set(word.strip().lower() for word in f if word.strip())

for fic in os.listdir(input_dir):
    if fic.endswith(".nowords"):
        in_path = os.path.join(input_dir, fic)
        out_path = os.path.join(input_dir, fic.replace(".nowords", ".stem"))

        with open(in_path, "r", encoding="utf8") as fin:
            words = fin.read().split()
            
        stemmed_words = stems = [ps.stem(word) for word in words]
        
        # Réécriture dans le fichier de sortie
        with open(out_path, "w", encoding="utf8") as fout:
            fout.write(" ".join(stemmed_words))

        print(f"→ {fic} traité → {os.path.basename(out_path)}")

print("\nSuppression des mots vides terminée.")