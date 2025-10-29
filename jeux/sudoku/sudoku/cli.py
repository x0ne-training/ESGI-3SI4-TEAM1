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

