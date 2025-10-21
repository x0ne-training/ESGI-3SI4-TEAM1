from fonction import *

# longueur_grille = int(input("Saisir la hauteur de la grille"))
# longueur_grille = int(input("Saisir la longueur de la grille"))
# nb_bombe = int(input("Saisir le nombre de bombe"))

# print (longueur_grille, longueur_grille, nb_bombe)

# --- Exemple d’utilisation ---
if __name__ == "__main__":
    rows, cols, mines = 3, 4, 2
    affichage = creation_affichage(rows, cols)
    terrain = creation_terrain(rows, cols)

    afficher_terrain_visible(affichage)

    print("🎮 Premier coup (tu ne peux pas tomber sur une mine)")
    r, c = choix_joueur(rows, cols)

    # Placer les mines après le premier choix pour garantir sécurité
    placement_mines(terrain, rows, cols, mines, safe_pos=(r, c))
    calcul_adj(terrain, rows, cols)

    # Révéler la première case
    reveler_case(terrain, affichage, r, c)
    afficher_terrain_visible(affichage)

    print("=== Mode debug (pour test) ===")
    afficher_terrain_debug(terrain)