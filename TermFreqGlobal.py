### DEPRECATED ####


from TermFreq import term_frequency
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python3 TermFreqGlobal.py <file_extension>, ex : .stem")
    sys.exit(1)

SRC_DIR = "./vocabulary"
INPUT_FILE = os.path.join(SRC_DIR, f"vocabulaire{sys.argv[1]}.txt")
OUTPUT_FILE = f"TermFrequencyGlobal{sys.argv[1]}.txt"

if not os.path.exists(INPUT_FILE):
    print(f"Le fichier {INPUT_FILE} n'existe pas.")
    sys.exit(1)

with open(INPUT_FILE, "r", encoding="utf8") as a, open(OUTPUT_FILE, "w", encoding="utf8") as f:
    for line in a:
        print("Processing word:", line.strip())
        word = line.strip()
        frequency = term_frequency(word, sys.argv[1])
        f.write(f"{word} {frequency}\n")

    


## Quelle est la definition du df, pourquoi on iutilise idf dans le calucle dans la fonction de correspondance ?
## 2 Quel est l'inter de mettre l'ideicateur sur la longueur du ducument ? Des qu'on a un document plus long, on va avoir plus de termes, donc la frequence des termes va etre plus elevee. Donc on va favoriser les documents longs. On n e veut donc pasfavoriser les documents longs. Aussi, dans les fonctions de correspondance, a chauqe fois qu'on rajoute une poccurence du meme termes, il faut qu'il ait un peu moins de poids, on utilise souvent le log du df.