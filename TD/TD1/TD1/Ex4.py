x = int(input("Nombre 1 : "))
y = int(input("Nombre 2 : "))
for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        print(f"{i} est un diviseur commun à {x} et {y}")