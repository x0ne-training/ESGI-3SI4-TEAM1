# main.py

position_joueur = "entrée"

while True:
    if position_joueur == "entrée":
        print("\nVous êtes à l'entrée sombre d'une grotte.")
        print("Actions possibles : gauche, droite")
        choix = input("> ").lower()
        if choix == "gauche": position_joueur = "tunnel_venteux"
        elif choix == "droite": position_joueur = "salle_echo"
        elif choix == "quitter": break
        else: print("Direction inconnue.")

    elif position_joueur == "tunnel_venteux":
        print("\nLe vent siffle dans ce tunnel étroit.")
        print("Vous pouvez seulement REVENIR sur vos pas.")
        choix = input("> ").lower()
        if choix == "revenir": position_joueur = "entrée"
        elif choix == "quitter": break
        else: print("Action impossible.")

    elif position_joueur == "salle_echo":
        print("\nVous êtes dans une grande salle. Le moindre bruit crée un écho assourdissant.")
        print("Vous pouvez REVENIR ou avancer vers une LUEUR au loin.")
        choix = input("> ").lower()
        if choix == "revenir": position_joueur = "entrée"
        elif choix == "lueur": print("C'est une impasse ! L'aventure s'arrête ici.") ; break # Fin simple
        elif choix == "quitter": break
        else: print("Action impossible.")

print("Merci d'avoir joué !")
