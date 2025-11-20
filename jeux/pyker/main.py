# Poker Game
import random

COULEURS = ('Coeur', 'Carreau', 'Pique', 'Trefle')
VALEURS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')

def creer_paquet():
    """Cree un paquet de 52 cartes."""
    paquet = []
    for couleur in COULEURS:
        for valeur in VALEURS:
            paquet.append((valeur, couleur))
    return paquet

def main():
    """
    Fonction principale du jeu.
    """
    print("Bienvenue au jeu de Poker !")
    paquet = creer_paquet()
    print(f"Le paquet a {len(paquet)} cartes.")

if __name__ == "__main__":
    main()
