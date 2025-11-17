# main.py
# Projet pour créer le jeu Snake en mode texte.
import copy

# --- Constantes ---
LARGEUR = 20
HAUTEUR = 10
SERPENT_SYMBOLE = "O"

# --- État du jeu ---
serpent = [[HAUTEUR // 2, LARGEUR // 2]]
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
    # Pour l'instant, on arrête la boucle manuellement
    partie_terminee = True 

print("Jeu terminé !")
