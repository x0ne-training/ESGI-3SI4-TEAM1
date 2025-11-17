# main.py
# Début de notre jeu d'aventure textuelle

# Boucle principale du jeu
while True:
    choix = input("> ").lower() # .lower() pour ne pas être sensible à la casse (majuscules/minuscules)

    if choix == "quitter":
        break # On sort de la boucle
    else:
        print(f"Commande inconnue : '{choix}'")

print("Merci d'avoir joué !")
