personne={
    "nom":"Dupont",
    "prenom":"jean",
    "age":30
}
# 1. Afficher le nom
print(personne["nom"])
# 2. Ajouter une clé "ville" avec la valeur "Paris"
personne["ville"]="paris"
print(personne)
# 3. Modifier l'âge à 31
personne["age"]=31
print(personne)
# 4. Afficher toutes les clés avec .keys()
print(personne.keys())
# 5. Afficher toutes les valeurs avec .values()
print(personne.values())
# 6. Vérifier si "email" existe dans le dictionnaire
mot="email"
if mot in personne:
    print("le mot exixte dans le dictionnaire")
else:
    print("le mot n'existe pas dans le dictionnaire")