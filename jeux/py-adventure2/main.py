# py-adventure - un mini jeu d'aventure textuel complet

def afficher_aide():
    """Affiche la liste des commandes disponibles."""
    print("\n--- Commandes disponibles ---")
    print("  nord, sud, est, ouest : Pour vous déplacer.")
    print("  aller [direction]     : Alternative pour le déplacement.")
    print("  regarder              : Décrit la salle où vous êtes.")
    print("  regarder [objet]      : Examine un objet.")
    print("  prendre [objet]       : Ramasse un objet.")
    print("  utiliser [objet]      : Tente d'utiliser un objet de votre inventaire.")
    print("  inventaire            : Affiche le contenu de votre inventaire.")
    print("  parler à [personnage] : Engage la conversation.")
    print("  aide                  : Affiche cette aide.")
    print("  quitter               : Quitte le jeu.")
    print("---------------------------")

def afficher_salle(salle):
    """Affiche les informations complètes de la salle actuelle."""
    print(f"\n--- {salle['nom']} ---")
    print(salle['description'])
    if salle['objets']:
        print("Vous voyez ici : " + ", ".join(salle['objets']))
    if salle['personnage']:
        print(f"Il y a quelqu'un ici : {salle['personnage']}.")

def main():
    """Fonction principale du jeu."""
    # --- Définition du monde du jeu ---
    carte = {
        'clairiere': {
            'nom': 'La Clairière du Réveil',
            'description': "Vous vous réveillez dans une clairière baignée de lumière. Un chemin s'enfonce dans une forêt sombre au nord.",
            'sorties': {'nord': 'foret'},
            'objets': [],
            'personnage': 'vieux sage'
        },
        'foret': {
            'nom': 'La Forêt Sombre',
            'description': "Les arbres sont si denses que la lumière peine à percer. À l'est, une vieille porte en bois est incrustée dans un chêne massif.",
            'sorties': {'sud': 'clairiere', 'est': {'destination': 'grotte', 'verrouillee': True}},
            'objets': ['cle en bronze'],
            'personnage': None
        },
        'grotte': {
            'nom': 'Grotte Secrète',
            'description': "L'air est frais et sent la terre humide. Au centre de la petite grotte, un coffre repose sur une pierre plate.",
            'sorties': {'ouest': 'foret'},
            'objets': ['tresor'],
            'personnage': None
        }
    }
    objets = {
        'cle en bronze': {'description': "Une petite clé en bronze. Elle semble très ancienne."},
        'tresor': {'description': "Un coffre magnifiquement orné. Il est lourd !"}
    }
    personnages = {
        'vieux sage': {'dialogue': "Pour trouver le trésor, il vous faudra une clé. On dit qu'elle est perdue quelque part dans la forêt..."}
    }

    # --- État initial du jeu ---
    salle_actuelle_id = 'clairiere'
    inventaire = []
    jeu_termine = False

    # --- Démarrage du jeu ---
    print("Bienvenue dans Py-Adventure !")
    print("Votre objectif : Trouver le trésor caché.")
    print("Tapez 'aide' pour voir la liste des commandes.")
    afficher_salle(carte[salle_actuelle_id])

    # --- Boucle de jeu principale ---
    while not jeu_termine:
        commande_brute = input("> ").lower().strip()
        mots = commande_brute.split()
        if not mots:
            continue
        
        verbe = mots[0]
        cible = " ".join(mots[1:]) if len(mots) > 1 else ""

        if verbe in ["aller", "go"]:
            verbe = cible # "aller nord" devient "nord"
            cible = ""

        # --- Traitement des commandes ---
        if verbe == "quitter":
            print("Merci d'avoir joué. À bientôt !")
            jeu_termine = True
        elif verbe == "aide":
            afficher_aide()
        elif verbe in ['nord', 'sud', 'est', 'ouest']:
            salle_actuelle = carte[salle_actuelle_id]
            if verbe in salle_actuelle['sorties']:
                sortie = salle_actuelle['sorties'][verbe]
                if isinstance(sortie, dict) and sortie.get('verrouillee'):
                    print("Cette voie est verrouillée.")
                else:
                    destination = sortie['destination'] if isinstance(sortie, dict) else sortie
                    salle_actuelle_id = destination
                    afficher_salle(carte[salle_actuelle_id])
            else:
                print("Vous ne pouvez pas aller par là.")
        elif verbe == "regarder":
            if not cible:
                afficher_salle(carte[salle_actuelle_id])
            elif cible in objets and (cible in inventaire or cible in carte[salle_actuelle_id]['objets']):
                print(objets[cible]['description'])
            else:
                print(f"Il n'y a pas de '{cible}' à regarder ici.")
        elif verbe == "prendre":
            if not cible:
                print("Prendre quoi ?")
            elif cible in carte[salle_actuelle_id]['objets']:
                carte[salle_actuelle_id]['objets'].remove(cible)
                inventaire.append(cible)
                print(f"Vous avez pris : {cible}.")
                if cible == 'tresor':
                    print("\nFÉLICITATIONS ! Vous avez trouvé le trésor et remporté la partie !")
                    jeu_termine = True
            else:
                print(f"Il n'y a pas de '{cible}' ici.")
        elif verbe == "inventaire":
            if not inventaire:
                print("Votre inventaire est vide.")
            else:
                print("Vous transportez : " + ", ".join(inventaire))
        elif verbe == "utiliser":
            if not cible:
                print("Utiliser quoi ?")
            elif cible not in inventaire:
                print(f"Vous n'avez pas de '{cible}'.")
            elif salle_actuelle_id == 'foret' and cible == 'cle en bronze':
                porte = carte['foret']['sorties']['est']
                if porte.get('verrouillee'):
                    porte['verrouillee'] = False
                    print("Vous insérez la clé dans la serrure de la porte. Avec un *clic*, elle se déverrouille !")
                else:
                    print("La porte est déjà déverrouillée.")
            else:
                print("Rien ne se passe.")
        elif verbe == "parler":
            perso_cible = " ".join(mots[2:]) if len(mots) > 2 and mots[1] == "à" else cible
            if not perso_cible:
                print("Parler à qui ?")
            elif perso_cible == carte[salle_actuelle_id]['personnage']:
                print(f"Le {perso_cible} dit : \"{personnages[perso_cible]['dialogue']}\"")
            else:
                print(f"Il n'y a personne de ce nom ici.")
        else:
            print(f"Je ne comprends pas la commande '{verbe}'. Tapez 'aide' pour la liste des commandes.")

if __name__ == "__main__":
    main()
