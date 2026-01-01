# Demandez a l'utilisateur le nombre de poulets
nombre = input("Combien de poulets avez-vous ? ")
nombre_poulets =int(nombre) # Convertir en entier
# Demandez le prix unitaire
prix = input("Prix de vente par poulet (FCFA) : ")
prix_unitaire =float(prix) # Convertir en decimal (float)
# Calculez le revenu total
revenu_total = nombre_poulets*prix_unitaire
print("Votre revenu total sera de", revenu_total, "FCFA")
