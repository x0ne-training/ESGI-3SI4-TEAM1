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

    def copy(self) -> "Board":
        return Board([row[:] for row in self.grid])

    def is_valid_coord(self, r: int, c: int) -> bool:
        return 0 <= r < 9 and 0 <= c < 9
    
    def get_cell(self, r: int, c: int) -> int:
        if not self.is_valid_coord(r, c):
            raise ValueError("Coordonnées invalides.")
        return self.grid[r][c]
    
    def set_cell(self, r: int, c: int, val: int) -> None:
        if not self.is_valid_coord(r, c):
            raise ValueError("Coordonnées invalides.")
        if not (0 <= val <= 9):
            raise ValueError("Valeur doit être entre 0 et 9.")
        self.grid[r][c] = val

    def row_vals(self, r: int) -> Set[int]:
        return set(self.grid[r])
    
    def col_vals(self, c: int) -> Set[int]:
        return {self.grid[r][c] for r in range(9)}
