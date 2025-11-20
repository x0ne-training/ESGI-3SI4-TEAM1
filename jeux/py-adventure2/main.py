# py-adventure - un mini jeu d'aventure textuel

def afficher_salle(salle):
    print(f"\n--- {salle['nom']} ---")
    print(salle['description'])
    if salle['objets']: print("Vous voyez ici : " + ", ".join(salle['objets']))
    if salle['personnage']: print(f"Il y a quelqu'un ici : {salle['personnage']}.")

def main():
    carte = {
        'clairiere': {
            'nom': 'La Clairière', 'description': "...", 'personnage': 'vieux sage',
            'sorties': {'nord': 'foret'}, 'objets': ['pomme']
        },
        'foret': {
            'nom': 'La Forêt Sombre', 'description': "Vous êtes dans une forêt dense. Une vieille porte en bois est incrustée dans un grand chêne à l'est.",
            'sorties': {'sud': 'clairiere', 'est': {'destination': 'grotte', 'verrouillee': True, 'cle': 'cle en bronze'}},
            'objets': ['cle en bronze'], 'personnage': None
        },
        'grotte': {
            'nom': 'Grotte Humide', 'description': "L'air est frais et humide. Vous entendez le son de gouttes d'eau.",
            'sorties': {'ouest': 'foret'}, 'objets': ['tresor'], 'personnage': None
        }
    }
    objets = {
        'pomme': {'description': "..."}, 'cle en bronze': {'description': "Une petite clé en bronze, visiblement ancienne."},
        'tresor': {'description': "Un coffre rempli de pièces d'or !"}
    }
    personnages = {'vieux sage': {'dialogue': "Cherchez la clé dans la forêt pour ouvrir le chemin..."}}
    salle_actuelle_id = 'clairiere'
    inventaire = []

    print("Bienvenue dans Py-Adventure !")
    afficher_salle(carte[salle_actuelle_id])

    while True:
        commande_brute = input("> ").lower().strip()
        mots = commande_brute.split()
        if not mots: continue
        commande = mots[0]
        
        if commande == "quitter": print("Merci d'avoir joué."); break
        elif commande in ['nord', 'sud', 'est', 'ouest']:
            salle_actuelle = carte[salle_actuelle_id]
            if commande in salle_actuelle['sorties']:
                sortie = salle_actuelle['sorties'][commande]
                if isinstance(sortie, dict): # C'est une porte/sortie spéciale
                    if sortie['verrouillee']:
                        print("Cette voie est verrouillée.")
                    else:
                        salle_actuelle_id = sortie['destination']
                        afficher_salle(carte[salle_actuelle_id])
                else: # Sortie normale
                    salle_actuelle_id = sortie
                    afficher_salle(carte[salle_actuelle_id])
            else:
                print("Vous ne pouvez pas aller par là.")
        # ... (commandes regarder, prendre, inventaire, parler inchangées) ...
        else: print("Commande inconnue.")

if __name__ == "__main__":
    main()
