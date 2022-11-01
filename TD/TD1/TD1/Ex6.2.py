import string
x = input("Entrez un texte : ")
lettres = 0
stats = {}
for i in string.ascii_lowercase: stats[i] = 0
for i in x.lower():
    if i in string.ascii_letters:
        stats[i] += 1
        lettres += 1
#tri = dict(sorted(stats.items(), key=lambda item: item[1]))
#liste = [(item, tri[item]) for item in tri.keys()]
liste = sorted(stats.items(), key=lambda item: item[1])
liste.reverse()
for i in liste:
    print(f"La fréquence de la lettre {i[0]} est : {100 * i[1] / lettres}%")

y = x.split()
moyenne = 0
for i in y:
    moyenne += len(i)

print(f"Nombre de mots : {len(y)}")
print(f"Longueur moyenne des mots : {moyenne/len(y)}")


