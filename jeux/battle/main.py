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

def jouer_tour(joueur1, joueur2):
    """Joue un tour de la bataille."""
    if not joueur1 or not joueur2:
        return None, None, None

    carte_joueur1 = joueur1.pop(0)
    carte_joueur2 = joueur2.pop(0)

    print(f"Joueur 1 joue : {carte_joueur1}")
    print(f"Joueur 2 joue : {carte_joueur2}")

    valeur1 = valeur_carte(carte_joueur1)
    valeur2 = valeur_carte(carte_joueur2)

    if valeur1 > valeur2:
        print("Joueur 1 gagne le tour.")
        joueur1.extend([carte_joueur1, carte_joueur2])
    elif valeur2 > valeur1:
        print("Joueur 2 gagne le tour.")
        joueur2.extend([carte_joueur1, carte_joueur2])
    else:
        print("Bataille !")

    return joueur1, joueur2

def main():
    """Fonction principale du jeu."""
    paquet = creer_paquet()
    melanger_paquet(paquet)
    joueur1, joueur2 = distribuer_cartes(paquet)

    joueur1, joueur2 = jouer_tour(joueur1, joueur2)

    print(f"\nJoueur 1 a {len(joueur1)} cartes.")
    print(f"Joueur 2 a {len(joueur2)} cartes.")

if __name__ == "__main__":
    main()
