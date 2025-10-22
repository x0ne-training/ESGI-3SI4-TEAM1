from fonction import *

rows = int(input("Saisir la hauteur de la grille : "))
cols = int(input("Saisir la longueur de la grille : "))
mines = int(input("Saisir le nombre de bombes : "))

# --- Création du terrain et de l'affichage ---
affichage = creation_affichage(rows, cols)
terrain = creation_terrain(rows, cols)

afficher_terrain_visible(affichage)

print("🎮 Premier coup (tu ne peux pas tomber sur une mine)")
r, c = choix_joueur(rows, cols)

# Placer les mines APRÈS le premier coup pour éviter de mourir direct
placement_mines(terrain, rows, cols, mines, safe_pos=(r, c))
calcul_adj(terrain, rows, cols)

# Révéler la première case (et les zones de 0)
reveler_case(terrain, affichage, r, c, rows, cols)
afficher_terrain_visible(affichage)

# === Boucle principale ===
partie = True
while partie:
    print("\n🎮 À toi de jouer !")
    r, c = choix_joueur(rows, cols)
    partie = reveler_case(terrain, affichage, r, c, rows, cols)
    afficher_terrain_visible(affichage)

    # (optionnel) mode debug pour dev
    print("\n=== Mode debug (pour test) ===")
    afficher_terrain_debug(terrain)

print("💣 Fin de la partie 💣")
