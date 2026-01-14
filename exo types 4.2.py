# Créez une calculatrice qui :

# 1. Demande à l'utilisateur combien de notes il veut entrer
nb_notes = int(input("Combien de notes voulez-vous entrer ? "))

# 2. Stocke les notes dans une liste
notes=[]
for i in range(nb_notes):
    note = float(input(f"Entrez la note {i+1} (sur {nb_notes}) : "))
    notes.append(note)
# 3. Calcule et affiche la moyenne
moyenne = sum(notes) / len(notes)
print(f"La moyenne est : {moyenne}")

# 4. Affiche la note la plus haute et la plus basse 
print("Note la plus haute :", max(notes))
print("Note la plus basse :", min(notes))