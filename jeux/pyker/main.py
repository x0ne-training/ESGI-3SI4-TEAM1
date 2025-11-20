# Poker Game
import random
from collections import Counter

# Constantes pour les cartes
COULEURS = ('Coeur', 'Carreau', 'Pique', 'Trefle')
VALEURS_RANG = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

def creer_paquet():
    """Cree et retourne un paquet de 52 cartes."""
    return [(valeur, couleur) for valeur in VALEURS_RANG for couleur in COULEURS]

def melanger_paquet(paquet):
    """Melange le paquet de cartes en utilisant la bibliotheque random."""
    random.shuffle(paquet)

def distribuer_cartes(paquet, nombre):
    """Retire et retourne un nombre specifie de cartes du dessus du paquet."""
    return [paquet.pop() for _ in range(nombre)]

def afficher_main(main, nom_joueur):
    """Affiche les cartes dans la main d'un joueur de maniere lisible."""
    print(f"\n--- Main de {nom_joueur} ---")
    for i, (valeur, couleur) in enumerate(main):
        print(f"  {i+1}) {valeur} de {couleur}")

def evaluer_main(main):
    """Evalue une main de 5 cartes et retourne son rang, son nom et les valeurs triees."""
    valeurs = sorted([VALEURS_RANG[c[0]] for c in main], reverse=True)
    couleurs = [c[1] for c in main]
    valeur_counts = Counter(valeurs)
    counts = sorted(valeur_counts.values(), reverse=True)
    
    is_flush = len(set(couleurs)) == 1
    # La suite est verifiee en regardant si la difference entre la plus haute et la plus basse carte est de 4
    is_straight = len(set(valeurs)) == 5 and (max(valeurs) - min(valeurs) == 4)
    # Cas special pour la suite As-5
    if not is_straight and set(valeurs) == {14, 2, 3, 4, 5}:
        is_straight = True
        valeurs = [5, 4, 3, 2, 1] # Reordonner pour la comparaison

    if is_straight and is_flush: return (9, "Quinte Flush", valeurs)
    if counts[0] == 4: return (8, "Carre", valeurs)
    if counts == [3, 2]: return (7, "Full", valeurs)
    if is_flush: return (6, "Couleur", valeurs)
    if is_straight: return (5, "Quinte", valeurs)
    if counts[0] == 3: return (4, "Brelan", valeurs)
    if counts == [2, 2, 1]: return (3, "Double Paire", valeurs)
    if counts[0] == 2: return (2, "Paire", valeurs)
    return (1, "Carte Haute", valeurs)

def determiner_gagnant(main_joueur, main_croupier):
    """Compare deux mains et determine le gagnant."""
    res_joueur = evaluer_main(main_joueur)
    res_croupier = evaluer_main(main_croupier)
    
    print("\n--- Resultats ---")
    print(f"Joueur: {res_joueur[1]}")
    print(f"Croupier: {res_croupier[1]}")

    if res_joueur[0] > res_croupier[0]: return "joueur"
    if res_croupier[0] > res_joueur[0]: return "croupier"
    
    # En cas de meme rang, la carte la plus haute tranche
    for v_j, v_c in zip(res_joueur[2], res_croupier[2]):
        if v_j > v_c: return "joueur"
        if v_c > v_j: return "croupier"
    return "egalite"

def echanger_cartes_joueur(main, paquet):
    """Gere la logique pour que le joueur echange des cartes."""
    choix = input("Cartes a echanger (ex: 1 3, ou 0 pour passer) ? ")
    if choix == '0': return
    try:
        indices = sorted([int(i) - 1 for i in choix.split()], reverse=True)
        for idx in indices:
            if 0 <= idx < len(main):
                main.pop(idx)
        main.extend(distribuer_cartes(paquet, len(indices)))
    except (ValueError, IndexError):
        print("Entree invalide, aucun echange effectue.")

def ia_croupier_echange(main, paquet):
    """IA simple qui decide si le croupier doit echanger des cartes."""
    score, _, _ = evaluer_main(main)
    # Le croupier echange 3 cartes s'il a moins d'une paire
    if score < 2:
        print("Le croupier echange 3 cartes.")
        for _ in range(3): main.pop(0) # Retire les 3 plus hautes cartes
        main.extend(distribuer_cartes(paquet, 3))
    else:
        print("Le croupier ne change pas de cartes.")

def boucle_de_jeu():
    """La boucle principale qui gere les tours de jeu."""
    argent_joueur = 100
    while argent_joueur > 0:
        print("\n" + "="*30)
        print(f"Nouveau tour ! Vous avez {argent_joueur} jetons.")
        
        mise = 0
        while True:
            try:
                mise_str = input(f"Votre mise (1-{argent_joueur}, 0 pour quitter): ")
                mise = int(mise_str)
                if 0 <= mise <= argent_joueur: break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        
        if mise == 0: break
        
        argent_joueur -= mise
        pot = mise * 2
        paquet = creer_paquet()
        melanger_paquet(paquet)
        main_joueur = distribuer_cartes(paquet, 5)
        main_croupier = distribuer_cartes(paquet, 5)

        afficher_main(main_joueur, "Joueur")
        echanger_cartes_joueur(main_joueur, paquet)
        
        ia_croupier_echange(main_croupier, paquet)

        afficher_main(main_joueur, "Votre main finale")
        afficher_main(main_croupier, "Main finale du Croupier")
        
        gagnant = determiner_gagnant(main_joueur, main_croupier)
        if gagnant == "joueur":
            print("\n=> Vous gagnez !")
            argent_joueur += pot
        elif gagnant == "croupier":
            print("\n=> Le croupier gagne.")
        else:
            print("\n=> Egalite.")
            argent_joueur += mise

    print("\nFin du jeu. Merci d'avoir joue !")

def main():
    """Fonction principale pour lancer le jeu."""
    print("Bienvenue au jeu de Poker !")
    boucle_de_jeu()

if __name__ == "__main__":
    main()
