x = int(input("Nombre de valeurs : "))
valeur = float(input("Entrez la valeur 1 : "))
moyenne = valeur
min = valeur
max = valeur
for i in range(2, x+1):
    valeur = float(input(f"Entrez la valeur {i} : "))
    moyenne += valeur
    if valeur < min: min = valeur
    if valeur > max: max = valeur
moyenne -= min+max
moyenne /= x-2
print(f"La moyenne centrée est de : {moyenne}")