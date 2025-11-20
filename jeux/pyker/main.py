# Poker Game
import random

COULEURS = ('Coeur', 'Carreau', 'Pique', 'Trefle')
VALEURS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')

def creer_paquet():
    """Cree un paquet de 52 cartes."""
    return [(valeur, couleur) for couleur in COULEURS for valeur in VALEURS]

def melanger_paquet(paquet):
    """Melange le paquet de cartes."""
    random.shuffle(paquet)

def distribuer_cartes(paquet, nombre):
    """Distribue un certain nombre de cartes."""
    return [paquet.pop() for _ in range(nombre)]

def afficher_main(main, nom_joueur):
    """Affiche la main d'un joueur."""
    print(f"Main de {nom_joueur}:")
    for valeur, couleur in main:
        print(f"  {valeur} de {couleur}")

def main():
    """
    Fonction principale du jeu.
    """
    print("Bienvenue au jeu de Poker !")
    paquet = creer_paquet()
    melanger_paquet(paquet)

    main_joueur = distribuer_cartes(paquet, 5)
    main_croupier = distribuer_cartes(paquet, 5)

    afficher_main(main_joueur, "Joueur")
    afficher_main(main_croupier, "Croupier")

if __name__ == "__main__":
    main()
