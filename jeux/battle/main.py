import random

def creer_paquet():
    """Crée un paquet de 52 cartes."""
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trefle']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    paquet = []
    for couleur in couleurs:
        for valeur in valeurs:
            paquet.append(f"{valeur} de {couleur}")
    return paquet

def main():
    """Fonction principale du jeu."""
    paquet = creer_paquet()
    print("Paquet de cartes créé :")
    for carte in paquet:
        print(carte)

if __name__ == "__main__":
    main()
