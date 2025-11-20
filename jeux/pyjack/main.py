import random

def creer_deck():
    """Crée et retourne un paquet de 52 cartes."""
    couleurs = ['\u2665', '\u2666', '\u2660', '\u2663'] # Coeur, Carreau, Pique, Trèfle
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A']
    return [f"{valeur}{couleur}" for couleur in couleurs for valeur in valeurs]

def melanger_deck(deck):
    """Mélange le paquet de cartes."""
    random.shuffle(deck)

def tirer_carte(deck):
    """Tire la dernière carte du paquet."""
    return deck.pop()

def calculer_total(main):
    """Calcule et retourne le total des points d'une main."""
    total = 0
    nombre_as = 0
    valeurs_cartes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'V': 10, 'D': 10, 'R': 10, 'A': 11}
    for carte in main:
        valeur = carte[:-1]
        total += valeurs_cartes[valeur]
        if valeur == 'A':
            nombre_as += 1

    while total > 21 and nombre_as > 0:
        total -= 10
        nombre_as -= 1
    return total

def afficher_mains(joueur_main, croupier_main, fin_de_partie):
    """Affiche les mains du joueur et du croupier."""
    if fin_de_partie:
        print(f"Votre main : {' '.join(joueur_main)} (Total: {calculer_total(joueur_main)})")
        print(f"Main du croupier : {' '.join(croupier_main)} (Total: {calculer_total(croupier_main)})")
    else:
        print(f"Votre main : {' '.join(joueur_main)} (Total: {calculer_total(joueur_main)})")
        print(f"Main du croupier : {croupier_main[0]} [?]")

def determiner_gagnant(total_joueur, total_croupier, joueur_blackjack, croupier_blackjack):
    """Détermine et retourne le message du gagnant."""
    if joueur_blackjack and not croupier_blackjack:
        return "Blackjack ! Vous gagnez !"
    elif not joueur_blackjack and croupier_blackjack:
        return "Le croupier a un Blackjack. Vous perdez."
    elif total_joueur > 21:
        return "Vous avez dépassé 21. Le croupier gagne."
    elif total_croupier > 21:
        return "Le croupier a dépassé 21. Vous gagnez !"
    elif total_joueur > total_croupier:
        return "Vous gagnez !"
    elif total_croupier > total_joueur:
        return "Le croupier gagne."
    else:
        return "Égalité."

def tour_joueur(deck, joueur_main):
    """Gère le tour du joueur."""
    while calculer_total(joueur_main) <= 21:
        choix = input("Voulez-vous 'tirer' ou 'rester' ? ")
        if choix.lower() == 'tirer':
            joueur_main.append(tirer_carte(deck))
            print(f"Votre main : {' '.join(joueur_main)} (Total: {calculer_total(joueur_main)})")
        elif choix.lower() == 'rester':
            break
        else:
            print("Choix invalide.")

def tour_croupier(deck, croupier_main):
    """Gère le tour du croupier."""
    while calculer_total(croupier_main) < 17:
        croupier_main.append(tirer_carte(deck))

def jouer_partie():
    """Exécute une partie de Blackjack."""
    deck = creer_deck()
    melanger_deck(deck)

    joueur_main = [tirer_carte(deck), tirer_carte(deck)]
    croupier_main = [tirer_carte(deck), tirer_carte(deck)]

    total_joueur = calculer_total(joueur_main)
    total_croupier = calculer_total(croupier_main)

    joueur_blackjack = total_joueur == 21 and len(joueur_main) == 2
    croupier_blackjack = total_croupier == 21 and len(croupier_main) == 2

    afficher_mains(joueur_main, croupier_main, False)

    if not (joueur_blackjack or croupier_blackjack):
        tour_joueur(deck, joueur_main)
        if calculer_total(joueur_main) <= 21:
            tour_croupier(deck, croupier_main)

    print("\n--- RÉSULTATS ---")
    afficher_mains(joueur_main, croupier_main, True)

    total_joueur = calculer_total(joueur_main)
    total_croupier = calculer_total(croupier_main)
    print(determiner_gagnant(total_joueur, total_croupier, joueur_blackjack, croupier_blackjack))


def main():
    """Fonction principale pour lancer le jeu."""
    print("Bienvenue au Blackjack !")
    while True:
        jouer_partie()
        rejouer = input("\nVoulez-vous rejouer ? (oui/non) ")
        if rejouer.lower() != 'oui':
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    main()
