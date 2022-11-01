import string
x = input("Entrez un texte : ")
lettres = 0
voyelles = 0
chiffres = 0
for i in x:
    if i in string.ascii_letters: lettres += 1
    if i in "aeiouyAEIOUY": voyelles += 1
    if i in string.digits: chiffres+= 1

print(f"Il y a {lettres} lettres dans le texte")
print(f"Il y a {voyelles} voyelles dans le texte")
print(f"Il y a {chiffres} chiffres dans le texte")
print(f"Il y a {len(x)} caractères dans le texte")