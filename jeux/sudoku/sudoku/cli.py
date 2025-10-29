from .board import Board

PUZZLE = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],

    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],

    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9],
]

HELP = """
Commandes:
  p r c v   -> placer v en ligne r, colonne c (1-9), ex: p 3 7 5
  d r c     -> effacer la case (mettre 0)
  v         -> vérifier cohérence (doublons)
  q         -> quitter
"""

def _print_board(board: Board):
    lines = []
    for r, row in enumerate(board.grid):
        if r % 3 == 0:
            lines.append("+-------+-------+-------+")
        line = []
        for c, v in enumerate(row):
            if c % 3 == 0:
                line.append("| ")
            line.append("." if v == 0 else str(v))
            line.append(" ")
        line.append("|")
        lines.append("".join(line))
    lines.append("+-------+-------+-------+")
    col_idx = "    " + " ".join(str(i) for i in range(1, 10))
    print("\n".join(lines))
    print(col_idx)

