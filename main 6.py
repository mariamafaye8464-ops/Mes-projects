# Generer un rapport de vente
ferme = "Ferme Touba"
nombre_poulets = 500
prix_unitaire = 3500
revenu_total = nombre_poulets * prix_unitaire
# Creez un rapport formate
print("=" * 40)
print(f"_____ {ferme} _____") # Centrer le nom
print("=" * 40)
print(f"Poulets vendus : {nombre_poulets} poulets")
print(f"Prix unitaire : {prix_unitaire} FCFA")
print(f"Revenu total : {revenu_total} FCFA")
print("=" * 40)
