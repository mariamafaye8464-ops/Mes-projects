def traiter_donnee(valeur):
    print(f"valeur: {valeur}")
    """Traite différemment selon le type"""
# Si c'est un int ou float : multiplier par 2
    if isinstance(valeur, (int, float)):
        return valeur * 2
# Si c'est un str : mettre en majuscules
    elif isinstance(valeur, str):
        return valeur.upper()
# Si c'est une list : retourner sa longueur # Si c'est une list : retourner sa longueur
    elif isinstance(valeur, list):
        return len(valeur)
# Sinon : afficher "Type non supporté"
    else:
        return "Type non supporté"
#tester avec des valeurs
print(traiter_donnee(5))          
print(traiter_donnee(3.14))       
print(traiter_donnee("hello"))    
print(traiter_donnee([1,2,3]))    
print(traiter_donnee(True))       

   
