# main.py
# Projet pour créer le jeu Snake en mode texte.
import copy
import time

# --- Constantes ---
LARGEUR = 20
HAUTEUR = 10
SERPENT_SYMBOLE = "O"

# --- État du jeu ---
serpent = [[HAUTEUR // 2, LARGEUR // 4]]
direction = "DROITE" # "HAUT", "BAS", "GAUCHE", "DROITE"
partie_terminee = False

# --- Fonctions ---
def afficher_grille(grille, serpent_a_afficher):
    """Affiche la grille de jeu avec le serpent."""
    grille_affichee = copy.deepcopy(grille)
    for segment in serpent_a_afficher:
        y, x = segment
        grille_affichee[y][x] = SERPENT_SYMBOLE
        
    print("+" + "-" * LARGEUR + "+")
    for ligne in grille_affichee:
        print("|" + "".join(ligne) + "|")
    print("+" + "-" * LARGEUR + "+")

# --- Initialisation ---
grille_jeu = [[" " for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

# --- Boucle Principale ---
while not partie_terminee:
    afficher_grille(grille_jeu, serpent)
    time.sleep(0.5) # Petite pause pour voir le mouvement
    
    # 1. Calculer la nouvelle tête
    tete_y, tete_x = serpent[0]
    if direction == "DROITE":
        nouvelle_tete = [tete_y, tete_x + 1]
    # (on ajoutera les autres directions plus tard)

    # 2. Mettre à jour le serpent
    serpent.insert(0, nouvelle_tete) # Ajoute la nouvelle tête
    serpent.pop() # Retire l'ancienne queue
    
    # Condition de fin temporaire
    if serpent[0][1] >= LARGEUR -1:
        partie_terminee = True

print("Jeu terminé !")
