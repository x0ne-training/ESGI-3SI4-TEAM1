# py-adventure - un mini jeu d'aventure textuel

def main():
    """
    Fonction principale du jeu.
    """
    print("Bienvenue dans Py-Adventure !")
    print("Tapez 'quitter' pour fermer le jeu.")

    while True:
        # Attend l'entrée du joueur
        commande = input("> ").lower().strip()

        # Vérifie si le joueur veut quitter
        if commande == "quitter":
            print("Merci d'avoir joué. À bientôt !")
            break
        # Gère les commandes inconnues
        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
