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
serpent = [[HAUTEUR // 2, LARGEUR // 4], [HAUTEUR // 2, LARGEUR // 4 - 1]] # Serpent de taille 2
nourriture = [random.randint(0, HAUTEUR-1), random.randint(0, LARGEUR-1)]
direction = "DROITE" 
partie_terminee = False

# --- Fonctions ---
def effacer_ecran(): os.system('cls' if os.name == 'nt' else 'clear')

def afficher_grille(grille, serpent_a_afficher, nourriture_a_afficher):
    effacer_ecran()
    grille_affichee = copy.deepcopy(grille)
    for segment in serpent_a_afficher:
        grille_affichee[segment[0]][segment[1]] = SERPENT_SYMBOLE
    grille_affichee[nourriture_a_afficher[0]][nourriture_a_afficher[1]] = NOURRITURE_SYMBOLE
    print("+" + "-" * LARGEUR + "+")
    for ligne in grille_affichee:
        print("|" + "".join(ligne) + "|")
    print("+" + "-" * LARGEUR + "+")

# --- Initialisation ---
grille_jeu = [[" " for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

# --- Boucle Principale ---
while not partie_terminee:
    afficher_grille(grille_jeu, serpent, nourriture)
    
    choix = input("Votre direction (z,q,s,d) ? ").lower()
    if choix == 'z': direction = "HAUT"
    elif choix == 'q': direction = "GAUCHE"
    elif choix == 's': direction = "BAS"
    elif choix == 'd': direction = "DROITE"

    tete_y, tete_x = serpent[0]
    if direction == "HAUT": nouvelle_tete = [tete_y - 1, tete_x]
    elif direction == "BAS": nouvelle_tete = [tete_y + 1, tete_x]
    elif direction == "GAUCHE": nouvelle_tete = [tete_y, tete_x - 1]
    elif direction == "DROITE": nouvelle_tete = [tete_y, tete_x + 1]

    # Collisions Murs
    if nouvelle_tete[0] < 0 or nouvelle_tete[0] >= HAUTEUR or nouvelle_tete[1] < 0 or nouvelle_tete[1] >= LARGEUR:
        print("Collision avec un mur !")
        partie_terminee = True
        continue
    
    # Collisions Serpent
    if nouvelle_tete in serpent:
        print("Vous vous êtes mordu la queue !")
        partie_terminee = True
        continue

    serpent.insert(0, nouvelle_tete)

    if serpent[0] == nourriture:
        nourriture = [random.randint(0, HAUTEUR-1), random.randint(0, LARGEUR-1)]
    else:
        serpent.pop()

print("Jeu terminé.")
