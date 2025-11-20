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

def melanger_paquet(paquet):
    """Melange le paquet de cartes."""
    random.shuffle(paquet)

def main():
    """
    Fonction principale du jeu.
    """
    print("Bienvenue au jeu de Poker !")
    paquet = creer_paquet()
    melanger_paquet(paquet)
    print("Le paquet a ete melange.")

if __name__ == "__main__":
    main()
