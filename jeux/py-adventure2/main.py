# py-adventure - un mini jeu d'aventure textuel

def afficher_salle(salle):
    """
    Affiche les informations de la salle actuelle.
    """
    print(f"\n--- {salle['nom']} ---")
    print(salle['description'])
    if salle['objets']:
        print("Vous voyez ici : " + ", ".join(salle['objets']))

def main():
    """
    Fonction principale du jeu.
    """
    carte = {
        'clairiere': {
            'nom': 'La Clairière du Départ',
            'description': "Vous êtes dans une clairière paisible...",
            'sorties': {'nord': 'foret'},
            'objets': ['épée rouillée', 'pomme']
        },
        'foret': {
            'nom': 'La Forêt Sombre',
            'description': "Vous pénétrez dans une forêt dense...",
            'sorties': {'sud': 'clairiere'},
            'objets': []
        }
    }
    salle_actuelle_id = 'clairiere'
    inventaire = []

    print("Bienvenue dans Py-Adventure !")
    print("Commandes : 'nord', 'sud', 'prendre [objet]', 'inventaire', 'quitter'.")

    afficher_salle(carte[salle_actuelle_id])

    while True:
        commande_brute = input("> ").lower().strip()
        mots = commande_brute.split()
        if not mots:
            continue
        commande = mots[0]
        
        if commande == "quitter":
            print("Merci d'avoir joué. À bientôt !")
            break
        elif commande in ['nord', 'sud', 'est', 'ouest']:
            if commande in carte[salle_actuelle_id]['sorties']:
                salle_actuelle_id = carte[salle_actuelle_id]['sorties'][commande]
                afficher_salle(carte[salle_actuelle_id])
            else:
                print("Vous ne pouvez pas aller par là.")
        elif commande == "prendre":
            if len(mots) > 1:
                objet_a_prendre = " ".join(mots[1:])
                salle_actuelle = carte[salle_actuelle_id]
                if objet_a_prendre in salle_actuelle['objets']:
                    salle_actuelle['objets'].remove(objet_a_prendre)
                    inventaire.append(objet_a_prendre)
                    print(f"Vous avez pris : {objet_a_prendre}.")
                else:
                    print(f"Il n'y a pas de '{objet_a_prendre}' ici.")
            else:
                print("Prendre quoi ?")
        elif commande == "inventaire":
            if not inventaire:
                print("Votre inventaire est vide.")
            else:
                print("Vous transportez : " + ", ".join(inventaire))
        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
