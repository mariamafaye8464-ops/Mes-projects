# Compteur de jours jusqu'a la vente
age_actuel = 1
age_vente = 45
while age_actuel>age_vente :
    print(f'Jour {age_actuel}: Encore {age_vente - age_actuel} jours')
age_actuel += 1
print("Poulets prets pour la vente !")