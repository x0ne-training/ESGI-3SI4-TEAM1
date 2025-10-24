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

def afficher_etat(mot_affiche: str, lettres_ratees: set[str], vies_restantes: int):
    """Affiche le pendu ASCII et l'état actuel du mot."""
    vies_perdues = (len(ASCII_PENDU) - 1) - vies_restantes
    vies_perdues = max(0, min(vies_perdues, len(ASCII_PENDU) - 1))
    print(ASCII_PENDU[vies_perdues])
    print(f"Mot : {mot_affiche}")
    if lettres_ratees:
        print("Lettres fausses :", " ".join(sorted(lettres_ratees)))
    print(f"Vies restantes : {vies_restantes}")
    print("-" * 40)

    





