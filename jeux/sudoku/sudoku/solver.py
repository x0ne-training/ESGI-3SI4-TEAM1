from __future__ import annotations
from typing import Optional, Tuple
from .board import Board

def _find_empty(board: Board) -> Optional[Tuple[int, int]]:
    for r in range(9):
        for c in range(9):
            if board.get_cell(r, c) == 0:
                return r, c
    return None

def solve_backtracking(board: Board) -> bool:
    empty = _find_empty(board)
    if not empty:
        return True
    r, c = empty
    for val in range(1, 10):
        if board.is_safe(r, c, val):
            board.set_cell(r, c, val)
            if solve_backtracking(board):
                return True
            board.set_cell(r, c, 0)
    return False