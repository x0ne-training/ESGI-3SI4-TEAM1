# main.py
# Projet pour créer le jeu Snake en mode texte.
import copy

# --- Constantes ---
LARGEUR = 20
HAUTEUR = 10
SERPENT_SYMBOLE = "O"

# --- État du jeu ---
serpent = [[HAUTEUR // 2, LARGEUR // 2]] # Une liste de coordonnées [y, x]

# --- Fonctions ---
def afficher_grille(grille, serpent_a_afficher):
    """Affiche la grille de jeu avec le serpent."""
    # On copie la grille pour ne pas modifier l'originale
    grille_affichee = copy.deepcopy(grille)
    
    # Place le serpent sur la grille à afficher
    for segment in serpent_a_afficher:
        y, x = segment
        grille_affichee[y][x] = SERPENT_SYMBOLE
        
    print("+" + "-" * LARGEUR + "+")
    for ligne in grille_affichee:
        print("|" + "".join(ligne) + "|")
    print("+" + "-" * LARGEUR + "+")

# --- Initialisation ---
grille_jeu = [[" " for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

# --- Boucle principale (temporaire) ---
print("Lancement du jeu Snake...")
afficher_grille(grille_jeu, serpent)
