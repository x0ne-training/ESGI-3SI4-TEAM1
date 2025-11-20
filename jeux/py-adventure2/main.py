# py-adventure - un mini jeu d'aventure textuel

def afficher_salle(salle):
    """
    Affiche les informations de la salle actuelle.
    """
    print(f"\n--- {salle['nom']} ---")
    print(salle['description'])

def main():
    """
    Fonction principale du jeu.
    """
    carte = {
        'clairiere': {
            'nom': 'La Clairière du Départ',
            'description': "Vous êtes dans une clairière paisible. La lumière du soleil filtre à travers les arbres. Un chemin mène vers le nord.",
            'sorties': {'nord': 'foret'}
        },
        'foret': {
            'nom': 'La Forêt Sombre',
            'description': "Vous pénétrez dans une forêt dense. Les arbres sont hauts et bloquent la lumière. Un frisson parcourt votre échine. Le chemin du retour est au sud.",
            'sorties': {'sud': 'clairiere'}
        }
    }

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
