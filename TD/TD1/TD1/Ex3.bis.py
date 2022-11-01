temperatures = []
for i in range(1, 13):
    temperatures.append(int(input(f"Ajoutez la température du mois {i} : ")))

print(f"Le minimum est : {min(temperatures)}")
print(f"Le maximum est : {max(temperatures)}")

plus_proche_zero = temperatures[0]

for i in range(12):
    if abs(temperatures[i]) <= abs(plus_proche_zero) and temperatures[i] < plus_proche_zero:
        plus_proche_zero = temperatures[i]

print(f"Le plus proche de zéro est : {plus_proche_zero}")