# Prix de vente des poulets cette semaine
prix_semaine = [3500, 3600, 3500, 3700, 3800, 3600, 3500]
# Calculer l prix moyen
prix_moyen =sum(prix_semaine)  / len(prix_semaine)
print(f"Prix moyen: {prix_moyen:.0f} FCFA")
# Trouver le prix maximum
prix_max = max(prix_semaine)
print(f"Prix maximum: {prix_max} FCFA")
# Compter combien de jours le prix etait >= 3600
compteur = 0
for prix in prix_semaine:
    if prix >= 3600:
        compteur += 1
print(f"Jours avec prix >= 3600: {compteur}")