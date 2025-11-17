# main.py
# Projet pour créer le jeu Snake en mode texte.
import copy

# --- Constantes ---
LARGEUR = 20
HAUTEUR = 10
SERPENT_SYMBOLE = "O"

# --- État du jeu ---
serpent = [[HAUTEUR // 2, LARGEUR // 4]]
direction = "DROITE" 
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
    
    # 1. Obtenir l'entrée du joueur
    choix = input("Votre direction (z,q,s,d) ? ").lower()
    if choix == 'z': direction = "HAUT"
    elif choix == 'q': direction = "GAUCHE"
    elif choix == 's': direction = "BAS"
    elif choix == 'd': direction = "DROITE"

    # 2. Calculer la nouvelle tête
    tete_y, tete_x = serpent[0]
    if direction == "HAUT": nouvelle_tete = [tete_y - 1, tete_x]
    elif direction == "BAS": nouvelle_tete = [tete_y + 1, tete_x]
    elif direction == "GAUCHE": nouvelle_tete = [tete_y, tete_x - 1]
    elif direction == "DROITE": nouvelle_tete = [tete_y, tete_x + 1]

    # 3. Mettre à jour le serpent
    serpent.insert(0, nouvelle_tete)
    serpent.pop()
    
    # Condition de fin temporaire
    if serpent[0][1] >= LARGEUR:
        partie_terminee = True

print("Jeu terminé !")
