import copy
import re

file = open("input", "r")
data = file.readlines()
data = [line.strip() for line in data]

sum = 0

# Pour le coup je crois que ça va être plus facile
# On va chercher les A et vérifier si autour on a bien un X-MAS

for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        if data[i][j] == "A":
            if (data[i - 1][j - 1] == "M" and data[i + 1][j + 1] == "S") or (
                data[i - 1][j - 1] == "S" and data[i + 1][j + 1] == "M"
            ):
                if (data[i + 1][j - 1] == "M" and data[i - 1][j + 1] == "S") or (
                    data[i + 1][j - 1] == "S" and data[i - 1][j + 1] == "M"
                ):
                    sum += 1

sum

# Effectivement, plus rapide que la partie 1.
