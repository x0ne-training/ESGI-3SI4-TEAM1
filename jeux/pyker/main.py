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

def distribuer_cartes(paquet, nombre):
    """Distribue un certain nombre de cartes."""
    cartes = []
    for _ in range(nombre):
        cartes.append(paquet.pop())
    return cartes

def main():
    """
    Fonction principale du jeu.
    """
    print("Bienvenue au jeu de Poker !")
    paquet = creer_paquet()
    melanger_paquet(paquet)

    main_joueur = distribuer_cartes(paquet, 5)
    main_croupier = distribuer_cartes(paquet, 5)

    print(f"Votre main: {main_joueur}")
    print(f"Main du croupier: {main_croupier}")

if __name__ == "__main__":
    main()
