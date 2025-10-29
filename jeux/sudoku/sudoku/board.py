from __future__ import annotations
from typing import List, Tuple, Set

Grid = List[List[int]]

class Board:
    """
    Grille Sudoku 9x9.
    - 0 = case vide
    """

    def __init__(self, grid: Grid):
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise ValueError("La grille doit être 9x9.")
        self.grid: Grid = [row[:] for row in grid]

    
