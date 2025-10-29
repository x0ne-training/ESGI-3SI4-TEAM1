from __future__ import annotations
import random
from typing import List, Tuple
from .board import Board
from .solver import solve_backtracking

def _seed_full_board() -> Board:
    """Crée une solution complète valide via un motif latin mélangé."""
    base = 3
    side = base * base

    def pattern(r, c): 
        return (base * (r % base) + r // base + c) % side

    r_base = list(range(base))
    rows = [g * base + r for g in random.sample(r_base, len(r_base)) for r in random.sample(r_base, len(r_base))]
    cols = [g * base + c for g in random.sample(r_base, len(r_base)) for c in random.sample(r_base, len(r_base))]
    nums = random.sample(range(1, side + 1), side)

    grid = [[nums[pattern(r, c)] for c in cols] for r in rows]
    b = Board(grid)
    # sanity: doit être déjà une grille complète correcte
    assert solve_backtracking(b.copy())
    return b

def _positions() -> List[Tuple[int, int]]:
    pos = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(pos)
    return pos

def generate_puzzle(hints: int = 30) -> Board:
    """Génère une grille jouable avec ~`hints` cases visibles (entre 17 et 81)."""
    hints = max(17, min(81, hints))
    full = _seed_full_board()
    puzzle = full.copy()

    to_remove = 81 - hints
    removed = 0
    for (r, c) in _positions():
        if removed >= to_remove:
            break
        puzzle.set_cell(r, c, 0)
        # NB: on ne vérifie pas l'unicité ici pour rester rapide/simple.
        removed += 1
    return puzzle

