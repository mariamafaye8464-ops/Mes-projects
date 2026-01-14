# creez un programme qui gere un carnet de contacts
contacts = []
# une fonction pour ajouter un contact
def  ajouter_contact(nom,telephone,email):
    nouveau_contact = {
        "nom":nom,
        "telephone":telephone,
        "email":email
    }
    contacts.append(nouveau_contact)
    print("contact ajouté avec sucées")
# une fonction pour afficher tous les contacts
def afficher_contacts():
    if not contacts :
        print("le carnet est vide")
    else:
        for contact in contacts:
            print("Nom :", contact["nom"])
            print("Téléphone :", contact["telephone"])
            print("Email :", contact["email"])
            print("-" * 30)
# une fonction pour chercher un conctact par nom
def chercher_contact(nom):
    for contact in contacts:
        if contact['nom']== nom:
            print("Contact trouvé")
            print("Nom :", contact["nom"])
            print("Téléphone :", contact["telephone"])
            print("Email :", contact["email"])
            return
    print("Contact non trouvé.")
    
    
   # afficher_contacts()

   # chercher_contact("Fatou")
def main():
    
    while True : 
        nom=""
        telephone=""
        email=""
        choix=int(input("votre choix"))
        if choix== 1 :
            nom=input("nom")
            telephone=input("telephone")
            email=input("email")
            ajouter_contact(nom,telephone,email)
        elif choix== 2 :
            afficher_contacts()
        elif choix== 3 :
            nom=input("Nom du contact a chercher :")
            chercher_contact(nom)
main()