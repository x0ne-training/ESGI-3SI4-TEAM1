# py-adventure - un mini jeu d'aventure textuel

def afficher_salle(salle):
    print(f"\n--- {salle['nom']} ---")
    print(salle['description'])
    if salle['objets']:
        print("Vous voyez ici : " + ", ".join(salle['objets']))

def main():
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
            'objets': ['lanterne éteinte']
        }
    }
    objets = {
        'épée rouillée': {'description': "Une vieille épée. Elle a connu de meilleurs jours mais peut encore être utile."},
        'pomme': {'description': "Une pomme rouge et juteuse. Elle semble délicieuse."},
        'lanterne éteinte': {'description': "Une lanterne à huile en laiton. Elle est vide."}
    }
    salle_actuelle_id = 'clairiere'
    inventaire = []

    print("Bienvenue dans Py-Adventure !")
    afficher_salle(carte[salle_actuelle_id])

    while True:
        commande_brute = input("> ").lower().strip()
        mots = commande_brute.split()
        if not mots: continue
        commande = mots[0]
        
        if commande == "quitter":
            print("Merci d'avoir joué. À bientôt !"); break
        elif commande in ['nord', 'sud', 'est', 'ouest']:
            if commande in carte[salle_actuelle_id]['sorties']:
                salle_actuelle_id = carte[salle_actuelle_id]['sorties'][commande]
                afficher_salle(carte[salle_actuelle_id])
            else:
                print("Vous ne pouvez pas aller par là.")
        elif commande == "regarder":
            if len(mots) > 1:
                cible = " ".join(mots[1:])
                if cible in inventaire or cible in carte[salle_actuelle_id]['objets']:
                    print(objets[cible]['description'])
                else:
                    print(f"Vous ne voyez pas de '{cible}' ici.")
            else:
                afficher_salle(carte[salle_actuelle_id])
        elif commande == "prendre":
            if len(mots) > 1:
                objet = " ".join(mots[1:])
                if objet in carte[salle_actuelle_id]['objets']:
                    carte[salle_actuelle_id]['objets'].remove(objet)
                    inventaire.append(objet)
                    print(f"Vous avez pris : {objet}.")
                else:
                    print(f"Il n'y a pas de '{objet}' ici.")
            else:
                print("Prendre quoi ?")
        elif commande == "inventaire":
            if not inventaire: print("Votre inventaire est vide.")
            else: print("Vous transportez : " + ", ".join(inventaire))
        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
