noms = ['boris', 'jean', 'simon', 'anna', 'jeanne', 'brandon',
'theo', 'brahim', 'marion', 'leila', 'lancelot', 'quentin',
'kevin', 'john', 'louise', 'paul', 'sarah', 'christophe',
'marielle', 'oriane', 'luc']

dico = dict()

for item in noms:
    for pos, lettre in enumerate(item):
        if (lettre, pos) not in dico:
            dico[(lettre, pos)] = [item]
        else:
            dico[(lettre, pos)].append(item)
print(dico)

l = input("Lettre : ")
p = int(input("Position : "))

if (l, p) in dico.keys():
    print(l, p, dico[(l, p)])
else :
    print(f"La lettre \"{l}\" n'est jamais en position {p} dans la liste donnée")