temp = float(input("Température 1 : "))
zero = temp
min = temp
max = temp
for i in range(2, 13):
    temp = float(input(f"Température {i} : "))
    if temp < min: min = temp
    if temp > max: max = temp
    if (abs(temp) < zero) or (abs(temp) == zero and temp < zero): zero = temp #si même distance à 0 alors le plus petit sera négatif
print(f"Le minimum est : {min}")
print(f"Le maximum est : {max}")
print(f"Le plus proche de zéro est : {zero}")