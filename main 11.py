# Creer une fonction plus complexe
def evaluer_rentabilite(benefice):
#Evalue si le projet est rentable
    if benefice > 500000:
         return "Excellent"
    elif benefice > 200000:
         return "Bon"
    elif benefice > 0:
         return "Faible"
    else:
         return "Perte"
# Utilisation
evaluation = evaluer_rentabilite(430000)
print(f"Evaluation: {evaluation}")