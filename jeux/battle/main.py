import random

def creer_paquet():
    """Crée un paquet de 52 cartes."""
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trefle']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    paquet = []
    for couleur in couleurs:
        for valeur in valeurs:
            paquet.append(f"{valeur} de {couleur}")
    return paquet

def melanger_paquet(paquet):
    """Mélange le paquet de cartes."""
    random.shuffle(paquet)

def distribuer_cartes(paquet):
    """Distribue les cartes entre deux joueurs."""
    joueur1 = paquet[:26]
    joueur2 = paquet[26:]
    return joueur1, joueur2

def valeur_carte(carte):
    """Retourne la valeur numérique d'une carte."""
    valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
    valeur_str = carte.split(' ')[0]
    return valeurs[valeur_str]

def jouer_partie():
    """Fonction principale du jeu de la bataille."""
    paquet = creer_paquet()
    melanger_paquet(paquet)
    joueur1, joueur2 = distribuer_cartes(paquet)
    tour = 0

    while joueur1 and joueur2:
        tour += 1
        print(f"\n--- Tour {tour} ---")
        print(f"Joueur 1 a {len(joueur1)} cartes, Joueur 2 a {len(joueur2)} cartes.")

        carte_joueur1 = joueur1.pop(0)
        carte_joueur2 = joueur2.pop(0)

        print(f"Joueur 1 joue : {carte_joueur1}")
        print(f"Joueur 2 joue : {carte_joueur2}")

        valeur1 = valeur_carte(carte_joueur1)
        valeur2 = valeur_carte(carte_joueur2)

        cartes_en_jeu = [carte_joueur1, carte_joueur2]

        if valeur1 > valeur2:
            print("Joueur 1 gagne le tour.")
            joueur1.extend(cartes_en_jeu)
        elif valeur2 > valeur1:
            print("Joueur 2 gagne le tour.")
            joueur2.extend(cartes_en_jeu)
        else:
            print("Bataille !")
            while valeur1 == valeur2:
                if len(joueur1) < 2 or len(joueur2) < 2:
                    if len(joueur1) > len(joueur2):
                        joueur1.extend(cartes_en_jeu)
                        joueur1.extend(joueur2)
                        joueur2.clear()
                    else:
                        joueur2.extend(cartes_en_jeu)
                        joueur2.extend(joueur1)
                        joueur1.clear()
                    break

                cartes_en_jeu.append(joueur1.pop(0))
                cartes_en_jeu.append(joueur2.pop(0))

                carte_joueur1 = joueur1.pop(0)
                carte_joueur2 = joueur2.pop(0)

                cartes_en_jeu.extend([carte_joueur1, carte_joueur2])

                print(f"Joueur 1 joue : {carte_joueur1}")
                print(f"Joueur 2 joue : {carte_joueur2}")

                valeur1 = valeur_carte(carte_joueur1)
                valeur2 = valeur_carte(carte_joueur2)

                if valeur1 > valeur2:
                    print("Joueur 1 gagne la bataille.")
                    joueur1.extend(cartes_en_jeu)
                    break
                elif valeur2 > valeur1:
                    print("Joueur 2 gagne la bataille.")
                    joueur2.extend(cartes_en_jeu)
                    break

    if not joueur1:
        print("\nJoueur 2 a gagné la partie !")
    else:
        print("\nJoueur 1 a gagné la partie !")

if __name__ == "__main__":
    jouer_partie()
