# py-adventure - un mini jeu d'aventure textuel

def afficher_salle(salle):
    """
    Affiche les informations de la salle actuelle.
    """
    print(f"Vous êtes dans : {salle['nom']}")

def main():
    """
    Fonction principale du jeu.
    """
    # Définition de la carte du jeu
    carte = {
        'clairiere': {
            'nom': 'une clairière ensoleillée',
            'sorties': {'nord': 'foret_sombre'}
        },
        'foret_sombre': {
            'nom': 'une forêt sombre et dense',
            'sorties': {'sud': 'clairiere'}
        }
    }

    # Position initiale du joueur
    salle_actuelle = 'clairiere'

    print("Bienvenue dans Py-Adventure !")
    print("Tapez 'quitter' pour fermer le jeu.")
    print("Commandes de déplacement : 'nord', 'sud', 'est', 'ouest'.")

    afficher_salle(carte[salle_actuelle])

    while True:
        commande = input("> ").lower().strip()

        if commande == "quitter":
            print("Merci d'avoir joué. À bientôt !")
            break

        # Logique de déplacement
        elif commande in ['nord', 'sud', 'est', 'ouest']:
            if commande in carte[salle_actuelle]['sorties']:
                salle_actuelle = carte[salle_actuelle]['sorties'][commande]
                afficher_salle(carte[salle_actuelle])
            else:
                print("Vous ne pouvez pas aller par là.")
        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
