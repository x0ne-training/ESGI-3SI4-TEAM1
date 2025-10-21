import random

# === PARTIE CREATION DU TERRAIN ===

def creation_terrain(rows: int, cols: int):
    """Crée une grille vide avec des cases prêtes à être remplies."""
    return [[{'mine': False, 'adj': 0} for _ in range(cols)] for _ in range(rows)]


def placement_mines(board, rows: int, cols: int, mines: int, safe_pos=None):
    """
    Place les mines aléatoirement sur le plateau.
    safe_pos = (r, c) => la première case choisie ne sera JAMAIS une mine.
    """
    if mines >= rows * cols:
        raise ValueError("Trop de mines pour la taille du terrain.")
    
    positions = [(r, c) for r in range(rows) for c in range(cols)]
    if safe_pos and safe_pos in positions:
        positions.remove(safe_pos)
    
    mines_placees = random.sample(positions, mines)
    for r, c in mines_placees:
        board[r][c]['mine'] = True


def calcul_adj(board, rows: int, cols: int):
    """Calcule le nombre de mines adjacentes pour chaque case."""
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]
    for r in range(rows):
        for c in range(cols):
            if board[r][c]['mine']:
                continue
            count = 0
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc]['mine']:
                    count += 1
            board[r][c]['adj'] = count


def creation_affichage(rows: int, cols: int):
    """Crée le tableau d'affichage du joueur (tout caché par des '/')."""
    return [['/' for _ in range(cols)] for _ in range(rows)]


# === PARTIE AFFICHAGE ===

def afficher_terrain_visible(affichage):
    """Affiche le tableau du joueur."""
    print("   " + " ".join(f"{i:2}" for i in range(len(affichage[0]))))
    for i, row in enumerate(affichage):
        print(f"{i:2} " + " ".join(row))
    print()


def afficher_terrain_debug(board):
    """Affiche le vrai terrain (debug/dev)."""
    for row in board:
        print(' '.join('M' if cell['mine'] else str(cell['adj']) for cell in row))
    print()


# === PARTIE JEU ===

def choix_joueur(rows, cols):
    """Demande au joueur de choisir une case (ligne, colonne) et vérifie que c'est valide."""
    while True:
        try:
            pos = input(f"Entre une position (ligne,colonne) entre 0-{rows-1} et 0-{cols-1} : ")
            r, c = map(int, pos.split(','))
            if 0 <= r < rows and 0 <= c < cols:
                return r, c
            else:
                print("⚠️ Position hors du terrain.")
        except ValueError:
            print("⚠️ Format invalide. Exemple : 3,5")


def reveler_case(terrain, affichage, r, c):
    """Révèle la case choisie par le joueur."""
    if terrain[r][c]['mine']:
        affichage[r][c] = '💥'
        print("💣 BOOM ! Tu as touché une mine !")
        return False
    else:
        affichage[r][c] = str(terrain[r][c]['adj'])
        return True