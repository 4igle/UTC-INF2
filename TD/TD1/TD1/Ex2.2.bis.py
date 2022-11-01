x = int(input("Nombre de valeurs : "))
valeurs = []
moyenne = 0
for i in range(1, x+1):
    nb = float(input(f"Entrez la valeur {i} : "))
    valeurs.append(nb)
    moyenne += nb

moyenne -= min(valeurs) + max(valeurs)
moyenne /= x-2
print(f"La moyenne centrée est de : {moyenne}")