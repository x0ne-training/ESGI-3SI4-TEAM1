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

# Placer les mines après le premier coup
placement_mines(terrain, rows, cols, mines, safe_pos=(r, c))
calcul_adj(terrain, rows, cols)

# Révéler la première case
reveler_case(terrain, affichage, r, c, rows, cols)
afficher_terrain_visible(affichage)

# === Boucle principale ===
partie = True
while partie:
    print("\n🎮 À toi de jouer !")
    r, c = choix_joueur(rows, cols)

    partie = reveler_case(terrain, affichage, r, c, rows, cols)
    afficher_terrain_visible(affichage)

    if not partie:
        print("💥 Tu as perdu... 💣")
        break

    if verifier_victoire(terrain, affichage):
        print("🏆 Félicitations, tu as gagné ! 🎉")
        break

    # (optionnel) mode debug
    print("\n=== Mode debug (pour test) ===")
    afficher_terrain_debug(terrain)
