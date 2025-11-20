import random

def main():
    print("Bienvenue au Blackjack !")

    while True:
        # Logique du jeu à venir ici
        rejouer = input("\nVoulez-vous rejouer ? (oui/non) ")
        if rejouer.lower() != 'oui':
            break

if __name__ == "__main__":
    main()
