# Créez un jeu où :
# 1. L'ordinateur choisit un nombre aléatoire entre 1 et 100

# 2. L'utilisateur doit le deviner

# 3. Le programme indique si le nombre est plus grand ou plus petit

# 4. Comptez le nombre de tentatives
import random
# À compléter
nombre_secret: int= random.randint(1,100)
tentatives = 0
while True:
        nombre = int(input("Devinez le nombre (entre 1 et 100) : "))
        tentatives += 1

        if nombre < nombre_secret:
            print(f"Trop petit , car le nombre est : ,{nombre_secret}")
        elif nombre > nombre_secret:
            print("Trop grand , car le nombre est :",{nombre_secret} )
        else:
            print(f"Bravo ! Vous avez trouvé en {tentatives} tentatives.")