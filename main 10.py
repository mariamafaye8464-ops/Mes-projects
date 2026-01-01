# Creer une fonction pour calculer le cout total
def calculer_cout_total(nb_poulets, prix_poussin, cout_aliment,
cout_vaccins):
#Calcule le cout total de production
    cout_poussins = nb_poulets*prix_poussin
    total = cout_poussins + cout_aliment +cout_vaccins
    return total
# Tester la fonction
cout = calculer_cout_total(500, 520, 800000, 50000)
print(f"Cout total: {cout} FCFA")
