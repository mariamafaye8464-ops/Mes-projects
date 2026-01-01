# Systeme de vaccination
age_poulet = 15 # jours
vaccin_1_fait = True
vaccin_2_fait = False
# Un poulet peut etre vendu si :
# - Il a au moins 45 jours
# - ET les deux vaccins sont faits
if age_poulet >= 45 and vaccin_1_fait and vaccin_2_fait:
    print("Poulet pret pour la vente")
else:
    print("Poulet pas encore pret")