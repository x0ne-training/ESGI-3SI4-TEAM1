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

def main():
    """Fonction principale du jeu."""
    paquet = creer_paquet()
    melanger_paquet(paquet)
    joueur1, joueur2 = distribuer_cartes(paquet)

    print("Cartes du joueur 1:")
    print(joueur1)
    print("\nCartes du joueur 2:")
    print(joueur2)

if __name__ == "__main__":
    main()
