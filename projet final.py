def afficher_menu():
#Affiche le menu principal
# Votre code ici
    print("="*40)
    print("SYSTEME DE GESTION AGRICOLE")
    print("="*40)
    print("1.Ajouter un nouveau cycle d'elevage")
    print("2.Afficher tous les cycles")
    print("3.Afficher les statistiques globales")
    print("4.Trouver le meilleur cycle")
    print("5.calculer les previsions")
    print("6.Quitter")
    print("="*40)
def ajouter_cycle(liste_cycles):
#Demande les infos et ajoute un nouveau cycle
# Votre code ici
    print("NOUVEAU CYCLE D'ELEVAGE")
    nom=input("Nom du cycle : ")
    nb_poussins=int(input("Nombre de poussins : "))
    prix_poussin=float(input("Prix unitaire d'un poussin (FCFA) : "))
    cout_total_aliment=float(input("Cout_aliment  (FCFA) : "))
    cout_des_vaccins=float(input("Cout_vaccins (FCFA) : "))
    autres_couts=float(input("Autres couts (FCFA) : "))
    nb_jours=int(input("Nombre de jours d'elevage : "))
    nb_poulets_vendus=int(input("Nombre de poulets vendus : "))
    prix_vente_unitaire=float(input("Prix de vente unitaire (FCFA) : "))
    # calcule directement ces valeur en ecrivant d'autre fonction qui afffecteront la valeur correspondante a la variable
    # benefice=int(input("Benefice (FCFA) :"))
    # taux_retour=float(input(" Taux de retour :" ))
    # taux_mortalite=float(input("Taux de mortalite :"))
    evaluation=str(input("Evaluation  :" ))

    cycle = {
        "nom":nom ,
        "nb_poussins":nb_poussins,
        "prix_poussin":prix_poussin,
        "cout_total_aliment":cout_total_aliment,
        "cout_des_vaccins":cout_des_vaccins,
        "autres_couts":autres_couts,
        "nb_jours":nb_jours,
        "nb_poulets_vendus":nb_poulets_vendus,
        "prix_vente_unitaire":prix_vente_unitaire,
        # "benefice":benefice,
        # "taux_retour":taux_retour,
        # "taux_mortalite": taux_mortalite,
        "evaluation":evaluation,
    }
    liste_cycles.append(cycle)

def calculer_cout_total(nb_poussins, prix_poussin, aliment, vaccins, autres):
#Calcule le cout total de production,
# Votre code ici
    cout_poussins=nb_poussins*prix_poussin
    cout_total=cout_poussins+aliment+vaccins+autres
    return cout_total
def calculer_revenu_total(nb_vendus ,prix_vente):
#calcul le revenu total
    revenu=nb_vendus*prix_vente
def calculer_benefice(revenu, depenses):
#Calcule le benefice net
# Votre code ici
    benefice = revenu - depenses
    return benefice
def calculer_taux_mortalite(nb_initial, nb_vendu):
#Calcule le taux de mortalite en %
# Votre code ici
    nb_morts=nb_initial-nb_vendu
    taux_mortalite=(nb_morts/nb_initial)*100
    return taux_mortalite
def calculer_taux_retour(benefice, investissement):
#Calcule le taux de retour sur investissement en %
# Votre code ici
    if investissement==0 :
        return 0
    taux=(benefice/investissement)*100
    return taux
def evaluer_rentabilite(taux_retour):
#Evalue la rentabilite : Excellent/Bon/Faible/Perte
# Votre code ici
    if taux_retour > 50 :
        return "Excellent"
    elif taux_retour > 30 :
        return "Bon"
    elif taux_retour > 0 :
        return "Faible"
    else:
        return "Perte"
def afficher_tous_cycles(liste_cycles):
#Affiche tous les cycles enregistres"""
# Votre code ici
    if len(liste_cycles) == 0 :
        print("Aucun cycle enregistre")
        return
    print("\n=== TOUS LES CYCLES D'ELEVAGE ===")
    print("Nom       Nombre de poussins      Benefice (FCFA)     Taux de retour (%)     Taux de mortalite (%)    Evaluation")
    for cycle in liste_cycles :
        print(f"{cycle['nom']}       {cycle['nb_poussins']}       {cycle['benefice']}       {cycle['taux_retour']}       {cycle['taux_mortalite']}       {cycle['evaluation']}")


def afficher_statistiques(liste_cycles):
#Calcule et affiche les statistiques globales
# Votre code ici
        if len(liste_cycles) == 0:
            print("Aucun cycle enregistre")
            return
        total_cycles = len(liste_cycles)
        benefice_total = sum(cycle['benefice'] for cycle in liste_cycles)
        benefice_moyen = benefice_total / total_cycles
        mortalite_moyenne = sum(cycle['taux_mortalite'] for cycle in liste_cycles) / total_cycles
        cycles_rentables = sum(1 for cycle in liste_cycles if cycle["benefice"] > 0)
        cycles_non_rentables = total_cycles - cycles_rentables
        taux_reussite = (cycles_rentables / total_cycles) * 100

        print("\n=== STATISTIQUES ===")

    # afficher_statistiques(cycles)
        # print("Nombre total de cycles :", cycle)
        print("Benefice total :", benefice_total, "FCFA")
        print("Benefice moyen :", round(benefice_moyen, 2), "FCFA")
        print("Taux de mortalite moyen :", round(mortalite_moyenne, 2), "%")
        print("Cycles rentables :", cycles_rentables)
        print("Cycles non rentables :", cycles_non_rentables)
        print("Taux de reussite :", round(taux_reussite, 2), "%")


def trouver_meilleur_cycle(liste_cycles):
#Trouve et affiche le meilleur cycle
# Votre code ici
    if len(liste_cycles) == 0:
        print("Aucun cycle enregistre")
        return

    meilleur = liste_cycles[0]

    for cycle in liste_cycles:
        if cycle['benefice'] > meilleur['benefice']:
            meilleur = cycle

    print("\n=== MEILLEUR CYCLE ===")
    print("Nom :", meilleur['nom'])
    print("Benefice :", meilleur['benefice'], "FCFA")
    print("Taux de retour :", meilleur['taux_retour'], "%")
    print("Taux de mortalite :", meilleur['taux_mortalite'], "%")
    print("Evaluation :", meilleur['evaluation'])

    # Test des statistiques (remplacer par votre fonction)

    
    

    # Test meilleur cycle (remplacer par votre fonction)


# Lancer le test
def calculer_previsions(liste_cycles):
    if len(liste_cycles) == 0:
        print("Aucune donnee historique disponible")
        return

    benefice_total = 0
    taux_retour_total = 0

    for cycle in liste_cycles:
        benefice_total += int(cycle["benefice"])
        taux_retour_total += cycle['taux_retour']

    benefice_moyen = benefice_total / len(liste_cycles)
    taux_retour_moyen = taux_retour_total / len(liste_cycles)

    print("\n=== PREVISIONS ===")
    print("Benefice previsionnel :", round(benefice_moyen, 2), "FCFA")
    print("Taux de retour previsionnel :", round(taux_retour_moyen, 2), "%")

    print("\n=== RECOMMANDATION ===")
    if taux_retour_moyen < 20:
        print("Rentabilite faible. Revoir les couts.")
    elif taux_retour_moyen < 40:
        print("Rentabilite moyenne. Peut etre amelioree.")
    else:
        print("Bonne rentabilite. Continuer ainsi.")



def quitter_programme():
    print("Merci d'avoir utilise le systeme de gestion avicole.")
    return False

#test_simple()
liste_cycles=[]
def main():
    print("=" * 40)
    print("BIENVENUE DANS LE SYSTEME DE GESTION AGRICOLE")
    print("=" * 40)
    while True:
        afficher_menu()
    
        choix=int(input("votre choix : "))  
        if choix == 1:
            ajouter_cycle(liste_cycles)

        elif choix == 2:
            afficher_tous_cycles(liste_cycles)

        elif choix == 3:
            afficher_statistiques(liste_cycles)

        elif choix == 4:
            trouver_meilleur_cycle(liste_cycles)

        elif choix == 5:
            calculer_previsions(liste_cycles)

        elif choix == 6:
            quitter_programme()
main()

