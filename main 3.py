# Verification du stock d'aliment
stock_kg = 150
consommation_journaliere = 75
jours_restants = stock_kg / consommation_journaliere
# Completez les conditions
if jours_restants >= 7:
    print("Stock suffisant pour la semaine ")
elif jours_restants >= 3:
    print("commander bientot") # "Commander bientot"
else:
    print("URGENT : commander maintenant !") # "URGENT : commander maintenant !"