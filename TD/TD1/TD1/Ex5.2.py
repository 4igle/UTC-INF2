INF2 = {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 ,
"etudiant_5" : 8 , "etudiant_6" : 14 , "etudiant_7" : 16 , "etudiant_8" : 12 ,
"etudiant_9" : 13 , "etudiant_10" : 15 , "etudiant_11" : 14 , "etudiant_112" : 9 ,
"etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 , "etudiant_16" : 7 ,
"etudiant_17" : 12 , "etudiant_18" : 15 , "etudiant_19" : 9 , "etudiant_20" : 17}

etudiantsAdmis = dict([(clef, INF2[clef]) for clef in INF2 if (INF2[clef]) >= 10])
etudiantsNonAdmis = dict([(clef, INF2[clef]) for clef in INF2 if (INF2[clef]) < 10])

a = 0
moyenne_admis = 0
for i in etudiantsAdmis:
    a += 1
    moyenne_admis += etudiantsAdmis[i]
moyenne_admis /= a

a = 0
moyenne_non_admis = 0
for i in etudiantsNonAdmis:
    a += 1
    moyenne_non_admis += etudiantsNonAdmis[i]
moyenne_non_admis /= a

print('Voici le dictionnaire des admis : ')
print(etudiantsAdmis)
print(f"Leur moyenne est de : {moyenne_admis}")
print()
print('Voici le dictionnaire des non admis : ')
print(etudiantsNonAdmis)
print(f"Leur moyenne est de : {moyenne_non_admis}")