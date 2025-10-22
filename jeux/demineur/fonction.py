import random

def creation_terrain(rows: int, cols: int):
    """Crée une grille vide avec des cases prêtes à être remplies."""
    return [[{'mine': False, 'adj': 0, 'revealed': False} for _ in range(cols)] for _ in range(rows)]


def placement_mines(board, rows: int, cols: int, mines: int, safe_pos=None):
    """
    Place les mines aléatoirement sur le plateau.
    safe_pos = (r, c) => la première case choisie ne sera JAMAIS une mine.
    """
    if mines >= rows * cols:
        raise ValueError("Trop de mines pour la taille du terrain.")
    
    positions = [(r, c) for r in range(rows) for c in range(cols)]
    if safe_pos:
        # on retire la position sûre + ses voisins immédiats
        sx, sy = safe_pos
        positions = [(r, c) for r, c in positions if abs(r - sx) > 1 or abs(c - sy) > 1]
    
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
                board[r][c]['adj'] = -1
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


def reveler_case(terrain, affichage, r, c, rows, cols):
    """
    Révèle la case choisie.
    Si c'est un 0, révèle aussi toutes les zones de 0 connectées.
    """
    if terrain[r][c]['mine']:
        affichage[r][c] = '💥'
        print("💣 BOOM ! Tu as touché une mine !")
        return False
    
    # Si la case est déjà révélée, on ne refait rien
    if terrain[r][c]['revealed']:
        return True

    # Révélation récursive (BFS)
    to_reveal = [(r, c)]
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]

    while to_reveal:
        x, y = to_reveal.pop()
        cell = terrain[x][y]
        if cell['revealed']:
            continue
        cell['revealed'] = True
        affichage[x][y] = str(cell['adj'])

        if cell['adj'] == 0:
            # si c'est un 0, on révèle les voisins
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    neighbor = terrain[nx][ny]
                    if not neighbor['revealed'] and not neighbor['mine']:
                        to_reveal.append((nx, ny))
    return True

