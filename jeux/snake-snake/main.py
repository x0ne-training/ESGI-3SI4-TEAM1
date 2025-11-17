# main.py
# Projet pour créer le jeu Snake en mode texte.

# --- Constantes ---
LARGEUR = 20
HAUTEUR = 10

# --- Fonctions ---
def afficher_grille(grille):
    """Affiche la grille de jeu avec des bordures."""
    print("+" + "-" * LARGEUR + "+")
    for ligne in grille:
        print("|" + "".join(ligne) + "|")
    print("+" + "-" * LARGEUR + "+")

# --- Initialisation ---
# On crée une grille vide, remplie d'espaces.
grille_jeu = [[" " for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

# --- Boucle principale (temporaire) ---
print("Lancement du jeu Snake...")
afficher_grille(grille_jeu)
