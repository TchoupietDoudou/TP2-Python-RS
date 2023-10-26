import random

nombre_aleatoire = random.random()

if nombre_aleatoire < 2/3:
    resultat = "Pile"
else:
    resultat = "Face"

print(resultat)
