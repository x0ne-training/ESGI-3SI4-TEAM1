# main.py
# Projet pour créer le jeu Snake en mode texte.
import copy
import os
import random

# --- Constantes ---
LARGEUR = 20
HAUTEUR = 10
SERPENT_SYMBOLE = "O"
NOURRITURE_SYMBOLE = "*"

# --- État du jeu ---
serpent = [[HAUTEUR // 2, LARGEUR // 4], [HAUTEUR // 2, LARGEUR // 4 - 1]]
nourriture = [random.randint(0, HAUTEUR-1), random.randint(0, LARGEUR-1)]
direction = "DROITE" 
score = 0
partie_terminee = False

# --- Fonctions ---
def effacer_ecran():
    """Efface le contenu de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_grille(grille, serpent_a_afficher, nourriture_a_afficher, score_a_afficher):
    """Prépare et affiche la grille de jeu complète."""
    effacer_ecran()
    # On fait une copie pour ne pas altérer la grille de base
    grille_affichee = copy.deepcopy(grille)
    
    # Placer le serpent
    for segment in serpent_a_afficher:
        grille_affichee[segment[0]][segment[1]] = SERPENT_SYMBOLE
        
    # Placer la nourriture
    grille_affichee[nourriture_a_afficher[0]][nourriture_a_afficher[1]] = NOURRITURE_SYMBOLE
    
    # Affichage final
    print("--- JEU DU SERPENT ---")
    print(f"Score : {score_a_afficher}")
    print("+" + "-" * LARGEUR + "+")
    for ligne in grille_affichee:
        print("|" + "".join(ligne) + "|")
    print("+" + "-" * LARGEUR + "+")

# --- Initialisation ---
grille_jeu = [[" " for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

print("Bienvenue dans Snake !")
print("Utilisez 'z' (haut), 'q' (gauche), 's' (bas), 'd' (droite) pour vous déplacer.")
input("Appuyez sur Entrée pour commencer...")

# --- Boucle Principale ---
while not partie_terminee:
    afficher_grille(grille_jeu, serpent, nourriture, score)
    
    choix = input("Votre direction (z,q,s,d) + Entrée : ").lower()
    if choix == 'z': direction = "HAUT"
    elif choix == 'q': direction = "GAUCHE"
    elif choix == 's': direction = "BAS"
    elif choix == 'd': direction = "DROITE"

    # Calculer la nouvelle tête en fonction de la direction
    tete_y, tete_x = serpent[0]
    if direction == "HAUT": nouvelle_tete = [tete_y - 1, tete_x]
    elif direction == "BAS": nouvelle_tete = [tete_y + 1, tete_x]
    elif direction == "GAUCHE": nouvelle_tete = [tete_y, tete_x - 1]
    elif direction == "DROITE": nouvelle_tete = [tete_y, tete_x + 1]

    # Vérification des conditions de défaite
    if (nouvelle_tete[0] < 0 or nouvelle_tete[0] >= HAUTEUR or
        nouvelle_tete[1] < 0 or nouvelle_tete[1] >= LARGEUR):
        print("\nCollision avec un mur !")
        partie_terminee = True
        continue
    
    if nouvelle_tete in serpent:
        print("\nVous vous êtes mordu la queue !")
        partie_terminee = True
        continue

    # Mise à jour du serpent
    serpent.insert(0, nouvelle_tete)

    # Vérifier si le serpent a mangé
    if serpent[0] == nourriture:
        score += 10
        # S'assurer que la nouvelle nourriture n'apparaît pas sur le serpent
        while nourriture in serpent:
            nourriture = [random.randint(0, HAUTEUR-1), random.randint(0, LARGEUR-1)]
    else:
        serpent.pop() # Si on ne mange pas, la queue rétrécit

# --- Fin de partie ---
print(f"GAME OVER. Score final : {score}")
print("Merci d'avoir joué !")
