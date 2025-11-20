import random

def spin_reels():
    """
    Effectue un tirage des trois rouleaux de la machine a sous.

    Retourne:
        list: Une liste de trois symboles representant le resultat du tirage.
    """
    symbols = ['Cerise', 'Orange', 'Citron', 'Bar', 'Sept']
    return [random.choice(symbols) for _ in range(3)]

def main():
    """
    Fonction principale du jeu de machine a sous.
    """
    print("Bienvenue a la machine a sous !")
    input("Appuyez sur Entree pour jouer...")

    result = spin_reels()
    print("Les rouleaux s'arretent sur :", " | ".join(result))

if __name__ == "__main__":
    main()
