import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python plot.py <extension>  (ex: .flt)")
    sys.exit(1)

count_file = f"./count/count{sys.argv[1]}.txt"

ranks = []
frequencies = []

# Lecture du fichier count
with open(count_file, "r", encoding="utf8") as f:
    for line in f:
        if not line.strip():
            continue
        parts = line.strip().split(" ")
        rank = int(parts[0])
        freq = int(parts[1])

        ranks.append(rank)
        frequencies.append(freq)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(ranks, frequencies)
plt.xlabel("Rang du mot")
plt.ylabel("Fréquence du mot")
plt.title(f"Loi de Zipf — {sys.argv[1]}")
### On utilise l'échelle log-log puisque d'après la loi de Zipft, fréquence ≈ 1 / rang donc affichage loglog on devrait obtenir une droite
plt.yscale("log")
plt.xscale("log")  
plt.grid(True)

plt.show()
