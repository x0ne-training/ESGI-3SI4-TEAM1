import random

def creer_deck():
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    deck = []
    for couleur in couleurs:
        for valeur in valeurs:
            deck.append(f"{valeur} de {couleur}")
    return deck

def main():
    print("Bienvenue au Blackjack !")

    while True:
        deck = creer_deck()
        print(deck) # Pour le test

        rejouer = input("\nVoulez-vous rejouer ? (oui/non) ")
        if rejouer.lower() != 'oui':
            break

if __name__ == "__main__":
    main()
