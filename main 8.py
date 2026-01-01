# Calculer le cout total sur 45 jours
cout_par_jour = 15000 # FCFA
cout_total = 0
for jour in range(1 , 44): # 45 jours
    cout_total += cout_par_jour
print(f"Cout total sur 45 jours: {cout_total} FCFA")