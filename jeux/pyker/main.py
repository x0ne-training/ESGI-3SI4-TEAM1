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
    print(f"\nMain de {nom_joueur}:")
    for i, (valeur, couleur) in enumerate(main):
        print(f"  {i+1}) {valeur} de {couleur}")

def evaluer_main(main):
    """Evalue la force d'une main de poker."""
    valeurs = sorted([VALEURS_RANG[c[0]] for c in main], reverse=True)
    couleurs = [c[1] for c in main]
    valeur_counts = Counter(valeurs)
    counts = sorted(valeur_counts.values(), reverse=True)
    valeurs_uniques = sorted(list(set(valeurs)), reverse=True)

    is_flush = len(set(couleurs)) == 1
    is_straight = len(valeurs_uniques) == 5 and (valeurs_uniques[0] - valeurs_uniques[4] == 4)

    if is_straight and is_flush: return (9, "Quinte Flush", valeurs_uniques)
    if counts[0] == 4: return (8, "Carre", valeurs_uniques)
    if counts == [3, 2]: return (7, "Full", valeurs_uniques)
    if is_flush: return (6, "Couleur", valeurs_uniques)
    if is_straight: return (5, "Quinte", valeurs_uniques)
    if counts[0] == 3: return (4, "Brelan", valeurs_uniques)
    if counts == [2, 2, 1]: return (3, "Double Paire", valeurs_uniques)
    if counts[0] == 2: return (2, "Paire", valeurs_uniques)
    return (1, "Carte Haute", valeurs_uniques)

def determiner_gagnant(main_joueur, main_croupier):
    """Determine le gagnant entre deux mains."""
    score_joueur, nom_main_joueur, valeurs_joueur = evaluer_main(main_joueur)
    score_croupier, nom_main_croupier, valeurs_croupier = evaluer_main(main_croupier)

    print(f"\nVous avez : {nom_main_joueur}")
    print(f"Le croupier a : {nom_main_croupier}")

    if score_joueur > score_croupier:
        return "joueur"
    if score_croupier > score_joueur:
        return "croupier"
    # En cas d'egalite, on compare les valeurs des cartes
    for v_j, v_c in zip(valeurs_joueur, valeurs_croupier):
        if v_j > v_c: return "joueur"
        if v_c > v_j: return "croupier"
    return "egalite"

def main():
    """
    Fonction principale du jeu.
    """
    argent_joueur = 100
    print("Bienvenue au jeu de Poker !")

    while argent_joueur > 0:
        print(f"\nVous avez {argent_joueur} jetons.")
        mise = int(input(f"Entrez votre mise (1-{argent_joueur}): "))
        if not 1 <= mise <= argent_joueur: continue

        argent_joueur -= mise
        pot = mise * 2

        paquet = creer_paquet()
        melanger_paquet(paquet)
        main_joueur = distribuer_cartes(paquet, 5)
        main_croupier = distribuer_cartes(paquet, 5)

        afficher_main(main_joueur, "Joueur")
        afficher_main(main_croupier, "Croupier")

        gagnant = determiner_gagnant(main_joueur, main_croupier)
        if gagnant == "joueur":
            print("Vous gagnez !")
            argent_joueur += pot
        elif gagnant == "croupier":
            print("Le croupier gagne.")
        else:
            print("Egalite.")
            argent_joueur += mise

        if argent_joueur == 0:
            print("Vous n'avez plus de jetons.")
            break

        continuer = input("Jouer un autre tour? (o/n): ").lower()
        if continuer != 'o':
            break

    print("Merci d'avoir joue !")

if __name__ == "__main__":
    main()
