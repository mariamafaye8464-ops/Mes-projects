total_poulets = 500
capacite_caisse = 12
caisses_pleines = total_poulets // capacite_caisse
poulets_restants = total_poulets%capacite_caisse
print("Nombre de caisses pleines :", caisses_pleines)
print("Poulets restant pour la dernière caisse :", poulets_restants)