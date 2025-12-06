import os

input_dir = "Collection"
stopwords_file = "cacm/common_words"

# Charger la liste des mots vides dans un set (rapide à chercher)
with open(stopwords_file, "r", encoding="utf8") as f:
    stopwords = set(word.strip().lower() for word in f if word.strip())

for fic in os.listdir(input_dir):
    if fic.endswith(".clean"):
        in_path = os.path.join(input_dir, fic)
        out_path = os.path.join(input_dir, fic.replace(".clean", ".nowords"))

        with open(in_path, "r", encoding="utf8") as fin:
            words = fin.read().split()

        # Filtrer les mots : garder seulement ceux qui NE sont PAS dans la stoplist
        filtered_words = [w for w in words if w not in stopwords]

        # Réécriture dans le fichier de sortie
        with open(out_path, "w", encoding="utf8") as fout:
            fout.write(" ".join(filtered_words))

        print(f"→ {fic} traité → {os.path.basename(out_path)}")

print("\nSuppression des mots vides terminée.")