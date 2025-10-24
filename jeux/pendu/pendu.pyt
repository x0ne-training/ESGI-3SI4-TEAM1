import random
import unicodedata
from pathlib import Path

ASCII_PENDU = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]

def strip_accents(s: str) -> str:
    """Supprime les accents pour simplifier la comparaison."""
    nfkd = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))

def charger_mots() -> list[str]:
    """Charge les mots depuis le fichier 'mots_fr.txt'."""
    chemin = Path(__file__).parent / "mots_fr.txt"
    if not chemin.exists():
        print("❌ Erreur : le fichier 'mots_fr.txt' est introuvable !")
        print("Assure-toi qu'il se trouve dans le même dossier que pendu.py.")
        exit(1)
    with chemin.open("r", encoding="utf-8") as f:
        mots = [ligne.strip() for ligne in f if ligne.strip()]
    return mots





