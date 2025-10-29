from __future__ import annotations
from typing import Optional, Tuple
from .board import Board

def _find_empty(board: Board) -> Optional[Tuple[int, int]]:
    for r in range(9):
        for c in range(9):
            if board.get_cell(r, c) == 0:
                return r, c
    return None