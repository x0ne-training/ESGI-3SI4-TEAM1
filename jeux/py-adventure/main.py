# main.py

# État du jeu
position_joueur = "entrée"

# Boucle principale du jeu
while True:
    # Affiche la description de la salle actuelle
    if position_joueur == "entrée":
        print("\nVous êtes à l'entrée sombre d'une grotte.")
        print("Un courant d'air froid vient d'un tunnel à votre GAUCHE.")
        print("Un faible écho résonne depuis un chemin à votre DROITE.")
        print("Que faites-vous ? (gauche, droite, quitter)")

    choix = input("> ").lower()

    if choix == "quitter":
        break
    else:
        print(f"Commande inconnue : '{choix}'")

print("Merci d'avoir joué !")
