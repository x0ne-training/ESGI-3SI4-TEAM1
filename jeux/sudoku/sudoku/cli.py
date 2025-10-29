from .board import Board
from .solver import solve_backtracking
from .generator import new_game

HELP = """
Commandes:
  n [easy|medium|hard] -> nouvelle grille (défaut: medium)
  p r c v              -> placer v en ligne r, colonne c (1-9), ex: p 3 7 5
  d r c                -> effacer la case (mettre 0)
  v                    -> vérifier cohérence (doublons)
  s                    -> résoudre automatiquement (backtracking)
  h                    -> afficher l'aide
  q                    -> quitter
"""

def _is_complete(board: Board) -> bool:
    return all(all(v != 0 for v in row) for row in board.grid) and board.is_consistent()

# ... (reprend la version du Commit 4, en ajoutant 'h' et le check après pose)

def _print_board(board: Board, fixed=set()):
    # (identique Commit 4)
    lines = []
    for r, row in enumerate(board.grid):
        if r % 3 == 0:
            lines.append("+-------+-------+-------+")
        line = []
        for c, v in enumerate(row):
            if c % 3 == 0:
                line.append("| ")
            if v == 0:
                sym = "."
            else:
                sym = str(v) + ("'" if (r, c) in fixed else "")
            line.append(sym)
            line.append(" ")
        line.append("|")
        lines.append("".join(line))
    lines.append("+-------+-------+-------+")
    col_idx = "    " + " ".join(str(i) for i in range(1, 10))
    print("\n".join(lines))
    print(col_idx)

def run_cli():
    print("=== Sudoku (Commit 5: CLI finitions) ===")
    print(HELP)
    board = new_game("medium")
    fixed = {(r, c) for r in range(9) for c in range(9) if board.get_cell(r, c) != 0}
    _print_board(board, fixed)

    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue
        parts = cmd.split()
        op = parts[0].lower()

        if op == "q":
            print("Bye.")
            break
        elif op == "h":
            print(HELP)
        elif op == "n":
            diff = parts[1].lower() if len(parts) > 1 else "medium"
            board = new_game(diff)
            fixed = {(r, c) for r in range(9) for c in range(9) if board.get_cell(r, c) != 0}
            _print_board(board, fixed)
        elif op == "v":
            print("OK, cohérent." if board.is_consistent() else "Conflits détectés.")
        elif op == "s":
            b = board.copy()
            if solve_backtracking(b):
                board = b
                _print_board(board, fixed)
                print("Solution trouvée.")
            else:
                print("Pas de solution trouvée.")
        elif op == "p":
            if len(parts) != 4:
                print("Usage: p r c v")
                continue
            try:
                r = int(parts[1]) - 1
                c = int(parts[2]) - 1
                v = int(parts[3])
            except ValueError:
                print("Paramètres invalides.")
                continue
            if (r, c) in fixed:
                print("Case initiale (fixe) non modifiable.")
                continue
            if not (0 <= r < 9 and 0 <= c < 9 and 1 <= v <= 9):
                print("Hors limites.")
                continue
            if not board.is_safe(r, c, v):
                print("Conflit avec ligne/colonne/boîte.")
                continue
            board.set_cell(r, c, v)
            _print_board(board, fixed)
            if _is_complete(board):
                print("Bravo ! Grille complétée sans conflit.")
        elif op == "d":
            if len(parts) != 3:
                print("Usage: d r c")
                continue
            try:
                r = int(parts[1]) - 1
                c = int(parts[2]) - 1
            except ValueError:
                print("Paramètres invalides.")
                continue
            if (r, c) in fixed:
                print("Case initiale (fixe) non modifiable.")
                continue
            if not (0 <= r < 9 and 0 <= c < 9):
                print("Hors limites.")
                continue
            board.set_cell(r, c, 0)
            _print_board(board, fixed)
        else:
            print("Commande inconnue. Tape 'h'.")
