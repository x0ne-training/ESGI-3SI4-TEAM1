# Poker Game
import random
from collections import Counter

COULEURS = ('Coeur', 'Carreau', 'Pique', 'Trefle')
VALEURS_RANG = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

def creer_paquet():
    """Cree un paquet de 52 cartes."""
    return [(valeur, couleur) for valeur in VALEURS_RANG for couleur in COULEURS]

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

def evaluer_main(main):
    """Evalue la force d'une main de poker."""
    valeurs = sorted([VALEURS_RANG[carte[0]] for carte in main])
    couleurs = [carte[1] for carte in main]
    valeur_counts = Counter(valeurs)
    valeurs_uniques = sorted(valeur_counts.keys())

    is_flush = len(set(couleurs)) == 1
    is_straight = len(valeurs_uniques) == 5 and (valeurs_uniques[-1] - valeurs_uniques[0] == 4)

    if is_straight and is_flush and valeurs_uniques[-1] == 14:
        return (10, "Quinte Flush Royale")
    # Plus d'évaluations à venir

    return (0, "Carte la plus haute")

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

    score_joueur, nom_main_joueur = evaluer_main(main_joueur)
    print(f"Vous avez : {nom_main_joueur}")


if __name__ == "__main__":
    main()
