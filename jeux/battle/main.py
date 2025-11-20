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

def jouer_tour(joueur1, joueur2):
    """Joue un tour de la bataille."""
    if not joueur1 or not joueur2:
        return None, None

    carte_joueur1 = joueur1.pop(0)
    carte_joueur2 = joueur2.pop(0)

    print(f"Joueur 1 joue : {carte_joueur1}")
    print(f"Joueur 2 joue : {carte_joueur2}")

    return carte_joueur1, carte_joueur2

def main():
    """Fonction principale du jeu."""
    paquet = creer_paquet()
    melanger_paquet(paquet)
    joueur1, joueur2 = distribuer_cartes(paquet)

    jouer_tour(joueur1, joueur2)

if __name__ == "__main__":
    main()
