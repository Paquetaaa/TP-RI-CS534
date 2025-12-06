import os
import re

# Dossier contenant les fichiers d'entrée
input_dir = "Collection"

# Parcours des fichiers du dossier
for filename in os.listdir(input_dir):
    if filename.startswith("CACM-") and not (filename.endswith(".stp") or filename.endswith(".flt") or filename.endswith(".clean")):
        file_path = os.path.join(input_dir, filename)

        # Lecture du fichier
        with open(file_path, "r", encoding="utf8") as f:
            text = f.read()

        # --- Nettoyage ---
        text = text.lower()                      # tout en minuscule
        text = text.translate(str.maketrans("àâäéèêëîïù", "aaaeeeeiiu"))                   # suppression des accents
        text = re.sub(r"[^a-z\s]", " ", text)    # garder uniquement lettres et espaces
        text = re.sub(r"\s+", " ", text).strip() # un seul espace

        # Nouveau nom de fichier (même dossier, extension .clean)
        new_filename = filename + ".clean"
        output_path = os.path.join(input_dir, new_filename)

        # Écriture du texte nettoyé
        with open(output_path, "w", encoding="utf8") as out:
            out.write(text)

        print(f"→ {new_filename} créé")

print("\nNettoyage terminé !")