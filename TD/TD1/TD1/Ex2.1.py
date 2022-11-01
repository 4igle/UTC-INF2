x = int(input("Nombre de valeurs : "))
moyenne = 0
for i in range(1, x+1):
    valeur = float(input(f"Entrez la valeur {i} : "))
    moyenne += valeur
moyenne /= x
print(f"La moyenne est de : {moyenne}")