# Systeme d'alerte temperature du poulailler
temperature = 32
if temperature > 35:
    print("DANGER : Temperature trop elevee !")
elif temperature == 28:
    print("Temperature normale")
else:
    print("Temperature basse, rechauffer")