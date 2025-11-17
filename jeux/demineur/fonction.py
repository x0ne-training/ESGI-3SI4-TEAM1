import random

# ============================================================
# ===============   CREATION DU TERRAIN   ====================
# ============================================================

def creation_terrain(rows: int, cols: int):
    """
    Crée une grille de jeu vide.
    Chaque case est représentée par un dictionnaire contenant :
        - mine: bool → True si c’est une mine.
        - adj: int → nombre de mines adjacentes.
        - revealed: bool → True si la case a déjà été révélée.
    """
    return [
        [{'mine': False, 'adj': 0, 'revealed': False} for _ in range(cols)]
        for _ in range(rows)
    ]


def placement_mines(board, rows: int, cols: int, mines: int, safe_pos=None):
    """
    Place les mines aléatoirement sur le terrain.
    
    - safe_pos (tuple): position sûre (ligne, colonne) où aucune mine
      ne sera placée (ainsi que les cases adjacentes).
    - Vérifie qu’on ne place pas plus de mines que de cases.
    """
    if mines >= rows * cols:
        raise ValueError("Trop de mines pour la taille du terrain.")
    
    # Liste de toutes les positions possibles
    positions = [(r, c) for r in range(rows) for c in range(cols)]
    
    # On retire la position sûre et ses cases voisines immédiates
    if safe_pos:
        sx, sy = safe_pos
        positions = [(r, c) for r, c in positions if abs(r - sx) > 1 or abs(c - sy) > 1]
    
    # Sélection aléatoire de certaines positions pour placer les mines
    mines_placees = random.sample(positions, mines)
    for r, c in mines_placees:
        board[r][c]['mine'] = True


def calcul_adj(board, rows: int, cols: int):
    """
    Calcule le nombre de mines adjacentes pour chaque case du terrain.
    - Si la case contient une mine, adj = -1 (indicateur interne).
    """
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c]['mine']:
                board[r][c]['adj'] = -1
                continue

            count = 0
            # On regarde toutes les cases autour
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc]['mine']:
                    count += 1
            board[r][c]['adj'] = count


def creation_affichage(rows: int, cols: int):
    """
    Crée la grille visible du joueur.
    Par défaut, toutes les cases sont masquées ('/').
    """
    return [['/' for _ in range(cols)] for _ in range(rows)]


# ============================================================
# ===============         AFFICHAGE        ===================
# ============================================================

def afficher_terrain_visible(affichage):
    """
    Affiche le plateau visible par le joueur.
    Les indices de lignes et colonnes sont affichés pour faciliter la saisie.
    """
    print("   " + " ".join(f"{i:2}" for i in range(len(affichage[0]))))
    for i, row in enumerate(affichage):
        print(f"{i:2} " + " ".join(row))
    print()


def afficher_terrain_debug(board):
    """
    Affiche le plateau réel (avec les mines et les chiffres).
    Utile pour le mode développeur ou pour tester le jeu.
    """
    for row in board:
        print(' '.join('M' if cell['mine'] else str(cell['adj']) for cell in row))
    print()


# ============================================================
# ===============        LOGIQUE DU JEU     ==================
# ============================================================

def choix_joueur(rows, cols):
    """
    Demande au joueur de choisir une case sous la forme 'ligne,colonne'.
    Vérifie que la saisie est correcte et que la position est dans la grille.
    """
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
    Révèle une case choisie par le joueur :
      - Si c’est une mine → le joueur perd.
      - Si c’est une case vide (adj=0) → on révèle automatiquement
        toutes les zones vides adjacentes (algorithme BFS).
      - Sinon → on révèle simplement la case choisie.
    """
    if terrain[r][c]['mine']:
        affichage[r][c] = '💥'
        print("💣 BOOM ! Tu as touché une mine !")
        return False
    
    # Si la case est déjà révélée, on ignore
    if terrain[r][c]['revealed']:
        return True

    # Liste des cases à révéler (utilisation d’une pile)
    to_reveal = [(r, c)]
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1),  (1,0), (1,1)]

    while to_reveal:
        x, y = to_reveal.pop()
        cell = terrain[x][y]

        # Ignore si déjà révélée
        if cell['revealed']:
            continue

        # Révèle la case
        cell['revealed'] = True
        affichage[x][y] = str(cell['adj'])

        # Si la case vaut 0, on ajoute les voisins à révéler
        if cell['adj'] == 0:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    neighbor = terrain[nx][ny]
                    if not neighbor['revealed'] and not neighbor['mine']:
                        to_reveal.append((nx, ny))
    return True


def verifier_victoire(terrain, affichage):
    """
    Vérifie si le joueur a gagné :
      → toutes les cases sans mine ont été révélées.
    Retourne True si la partie est gagnée, False sinon.
    """
    for r in range(len(terrain)):
        for c in range(len(terrain[0])):
            if not terrain[r][c]['mine'] and affichage[r][c] == '/':
                return False
    return True
