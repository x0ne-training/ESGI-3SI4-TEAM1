from fonction import *

rows = int(input("Saisir la hauteur de la grille"))
cols = int(input("Saisir la longueur de la grille"))
mines = int(input("Saisir le nombre de bombe"))

# print (longueur_grille, longueur_grille, nb_bombe)

# --- Exemple d’utilisation ---

# rows, cols, mines = 3, 4, 2
affichage = creation_affichage(rows, cols)
terrain = creation_terrain(rows, cols)

afficher_terrain_visible(affichage)

print("🎮 Premier coup (tu ne peux pas tomber sur une mine)")
r, c = choix_joueur(rows, cols)
# Révéler la première case
reveler_case(terrain, affichage, r, c)
afficher_terrain_visible(affichage)

# Placer les mines après le premier choix pour garantir sécurité
placement_mines(terrain, rows, cols, mines, safe_pos=(r, c))
calcul_adj(terrain, rows, cols)

partie = True 
while partie == True :

    print("🎮 rentrez une position (ligne, colonne)")
    r, c = choix_joueur(rows, cols)
    # Révéler la case
    partie = reveler_case(terrain, affichage, r, c)
    afficher_terrain_visible(affichage)


    

    print("=== Mode debug (pour test) ===")
    afficher_terrain_debug(terrain)