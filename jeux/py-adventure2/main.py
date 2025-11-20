def afficher_salle(salle):
    print(f"\n--- {salle['nom']} ---")
    print(salle['description'])
    if salle['objets']: print("Vous voyez ici : " + ", ".join(salle['objets']))
    if salle['personnage']: print(f"Il y a quelqu'un ici : {salle['personnage']}.")

def main():
    carte = {
        'clairiere': {'nom': 'La Clairière', 'description': "...", 'sorties': {'nord': 'foret'}, 'objets': ['pomme'], 'personnage': 'vieux sage'},
        'foret': {'nom': 'La Forêt Sombre', 'description': "...", 'sorties': {'sud': 'clairiere', 'est': {'destination': 'grotte', 'verrouillee': True, 'cle': 'cle en bronze'}}, 'objets': ['cle en bronze'], 'personnage': None},
        'grotte': {'nom': 'Grotte Humide', 'description': "...", 'sorties': {'ouest': 'foret'}, 'objets': ['tresor'], 'personnage': None}
    }
    objets = {'pomme': {}, 'cle en bronze': {}, 'tresor': {}}
    personnages = {'vieux sage': {'dialogue': "Le trésor vous attend !"},}
    salle_actuelle_id = 'clairiere'
    inventaire = []
    jeu_termine = False

    print("Bienvenue dans Py-Adventure !")
    afficher_salle(carte[salle_actuelle_id])

    while not jeu_termine:
        commande_brute = input("> ").lower().strip()
        mots = commande_brute.split()
        if not mots: continue
        commande = mots[0]
        
        if commande == "quitter": print("Merci d'avoir joué."); jeu_termine = True
        elif commande == "prendre":
            if len(mots) > 1:
                objet = " ".join(mots[1:])
                if objet in carte[salle_actuelle_id]['objets']:
                    carte[salle_actuelle_id]['objets'].remove(objet)
                    inventaire.append(objet)
                    print(f"Vous avez pris : {objet}.")
                    # Condition de victoire
                    if objet == 'tresor':
                        print("\nFélicitations ! Vous avez trouvé le trésor !")
                        print("Vous avez gagné la partie.")
                        jeu_termine = True
                else: print(f"Il n'y a pas de '{objet}' ici.")
            else: print("Prendre quoi ?")
        # ... (autres commandes : déplacement, utiliser, regarder, etc.) ...
        # ... (le code des autres commandes est identique au commit précédent) ...
        elif commande == "regarder":
            # ... (code de regarder inchangé)
            if len(mots) > 1:
                cible = " ".join(mots[1:])
                if cible in inventaire or cible in carte[salle_actuelle_id]['objets']:
                    print(objets[cible]['description'])
                else: print(f"Vous ne voyez pas de '{cible}' ici.")
            else: afficher_salle(carte[salle_actuelle_id])
        elif commande == "prendre":
            # ... (code de prendre inchangé)
            if len(mots) > 1:
                objet = " ".join(mots[1:])
                if objet in carte[salle_actuelle_id]['objets']:
                    carte[salle_actuelle_id]['objets'].remove(objet)
                    inventaire.append(objet)
                    print(f"Vous avez pris : {objet}.")
                else: print(f"Il n'y a pas de '{objet}' ici.")
            else: print("Prendre quoi ?")
        elif commande == "inventaire":
            # ... (code d'inventaire inchangé)
            if not inventaire: print("Votre inventaire est vide.")
        elif commande in ['nord', 'sud', 'est', 'ouest']:
            salle_actuelle = carte[salle_actuelle_id]
            if commande in salle_actuelle['sorties']:
                sortie = salle_actuelle['sorties'][commande]
                if isinstance(sortie, dict):
                    if sortie['verrouillee']: print("Cette voie est verrouillée.")
                    else: salle_actuelle_id = sortie['destination']; afficher_salle(carte[salle_actuelle_id])
                else: salle_actuelle_id = sortie; afficher_salle(carte[salle_actuelle_id])
            else: print("Vous ne pouvez pas aller par là.")
        elif commande == "utiliser":
             if len(mots) > 1:
                objet_a_utiliser = " ".join(mots[1:])
                if objet_a_utiliser in inventaire:
                    if salle_actuelle_id == 'foret' and objet_a_utiliser == 'cle en bronze':
                        porte = carte['foret']['sorties']['est']
                        if porte['verrouillee']:
                            porte['verrouillee'] = False
                            print("Vous utilisez la clé. La porte en bois s'ouvre.")
                        else: print("La porte est déjà ouverte.")
                    else: print(f"Vous ne pouvez pas utiliser '{objet_a_utiliser}' ici.")
                else: print(f"Vous n'avez pas de '{objet_a_utiliser}'.")
             else: print("Utiliser quoi ?")
        else:
             if commande not in ["prendre", "quitter"]:
                 print("Commande inconnue.")

if __name__ == "__main__":
    main()