import random

def creer_deck():
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    deck = []
    for couleur in couleurs:
        for valeur in valeurs:
            deck.append(f"{valeur} de {couleur}")
    return deck

def melanger_deck(deck):
    random.shuffle(deck)

def tirer_carte(deck):
    return deck.pop()

def main():
    print("Bienvenue au Blackjack !")

    while True:
        deck = creer_deck()
        melanger_deck(deck)

        joueur_main = [tirer_carte(deck), tirer_carte(deck)]
        croupier_main = [tirer_carte(deck), tirer_carte(deck)]

        print(f"Votre main : {joueur_main}")
        print(f"Main du croupier : [{croupier_main[0]}, 'Carte cachée']")

        rejouer = input("\nVoulez-vous rejouer ? (oui/non) ")
        if rejouer.lower() != 'oui':
            break

if __name__ == "__main__":
    main()
