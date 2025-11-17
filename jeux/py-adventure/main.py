# main.py

# État du jeu
position_joueur = "entrée"

# Boucle principale du jeu
while True:
    if position_joueur == "entrée":
        print("\nVous êtes à l'entrée sombre d'une grotte.")
        print("Un courant d'air froid vient d'un tunnel à votre GAUCHE.")
        print("Un faible écho résonne depuis un chemin à votre DROITE.")
        print("Que faites-vous ? (gauche, droite)")

        choix = input("> ").lower()

        if choix == "gauche":
            position_joueur = "tunnel_venteux"
        elif choix == "droite":
            position_joueur = "salle_echo"
        elif choix == "quitter":
            break
        else:
            print("Je ne comprends pas cette direction.")

print("Merci d'avoir joué !")
