from __future__ import annotations
import random
from typing import List, Tuple
from .board import Board
from .solver import solve_backtracking

def _seed_full_board() -> Board:
    """Crée une solution complète valide via un motif latin mélangé."""
    base = 3
    side = base * base