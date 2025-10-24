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

def generer_mot(mots: list[str]) -> tuple[str, str]:
    """Choisit un mot au hasard."""
    mot = random.choice(mots).lower()
    mot_normalise = strip_accents(mot)
    return mot, mot_normalise

def construire_masque(mot_original: str, lettres_trouvees_norm: set[str]) -> str:
    """Construit l'affichage du mot avec les lettres découvertes."""
    res = []
    for ch in mot_original:
        if ch.isalpha():
            if strip_accents(ch) in lettres_trouvees_norm:
                res.append(ch)
            else:
                res.append("_")
        else:
            res.append(ch)
    return " ".join(res)

def demander_coup(lettres_deja: set[str]) -> str:
    """Demande au joueur une lettre ou un mot complet."""
    while True:
        entree = input("Propose une lettre ou un mot entier : ").strip().lower()
        if not entree:
            print("Entrée vide. Réessaie.")
            continue
        entree_norm = strip_accents(entree)
        if len(entree_norm) == 1 and entree_norm.isalpha():
            if entree_norm in lettres_deja:
                print("Tu as déjà essayé cette lettre. Réessaie.")
                continue
            return entree
        elif len(entree_norm) >= 2 and entree_norm.replace(" ", "").isalpha():
            return entree
        else:
            print("Entrée invalide. Réessaie.")

def jouer_une_partie(vies_max: int = 6):
    mots = charger_mots()
    mot_original, mot_norm = generer_mot(mots)

    lettres_trouvees_norm: set[str] = set()
    lettres_ratees_norm: set[str] = set()
    vies = vies_max

    while True:
        mot_affiche = construire_masque(mot_original, lettres_trouvees_norm)
        afficher_etat(mot_affiche, lettres_ratees_norm, vies)

        if "_" not in mot_affiche:
            print(f"🎉 Bravo ! Tu as trouvé : {mot_original}")
            break

        if vies <= 0:
            print(f"💀 Pendu... Le mot était : {mot_original}")
            break

        coup = demander_coup(lettres_trouvees_norm | lettres_ratees_norm)
        coup_norm = strip_accents(coup)

        # Proposition de mot entier
        if len(coup_norm) > 1:
            if coup_norm == mot_norm:
                print(f"✅ Exact ! Le mot était bien : {mot_original}")
                break
            else:
                print("❌ Mauvaise proposition de mot.")
                vies -= 1
                continue

        # Proposition d'une lettre
        if coup_norm in mot_norm:
            lettres_trouvees_norm.add(coup_norm)
            print("✔️ Bonne lettre !")
        else:
            lettres_ratees_norm.add(coup_norm)
            vies -= 1
            print("❌ Mauvaise lettre.")

def menu():
    print("=" * 40)
    print("     🎮  PENDU (console, FR)  🎮")
    print("=" * 40)
    while True:
        print("\n1) Jouer")
        print("2) Quitter")
        choix = input("Choix : ").strip()
        if choix == "1":
            jouer_une_partie()
        elif choix == "2":
            print("À bientôt 👋")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()
