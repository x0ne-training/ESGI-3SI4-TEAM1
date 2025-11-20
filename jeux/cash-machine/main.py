import random

SYMBOLS = {
    'Cerise': 2,
    'Orange': 3,
    'Citron': 4,
    'Bar': 5,
    'Sept': 10
}

def spin_reels():
    """
    Effectue un tirage des trois rouleaux de la machine a sous.

    Retourne:
        list: Une liste de trois symboles representant le resultat du tirage.
    """
    return [random.choice(list(SYMBOLS.keys())) for _ in range(3)]

def calculate_winnings(reels, bet):
    """
    Calcule les gains en fonction du resultat du tirage et de la mise.

    Args:
        reels (list): Le resultat du tirage des rouleaux.
        bet (int): Le montant de la mise.

    Retourne:
        int: Le montant des gains.
    """
    if reels[0] == reels[1] == reels[2]:
        symbol = reels[0]
        return bet * SYMBOLS[symbol]
    return 0

def main():
    """
    Fonction principale du jeu de machine a sous.
    """
    balance = 100
    print("Bienvenue a la machine a sous !")
    print(f"Votre solde est de {balance}.")

    while balance > 0:
        bet = int(input("Combien voulez-vous miser ? (ou 0 pour quitter) "))

        if bet == 0:
            break

        if bet > balance:
            print("Vous n'avez pas assez d'argent !")
            continue

        balance -= bet
        result = spin_reels()
        print("Les rouleaux s'arretent sur :", " | ".join(result))

        winnings = calculate_winnings(result, bet)
        if winnings > 0:
            print(f"Felicitations ! Vous avez gagne {winnings} !")
            balance += winnings
        else:
            print("Dommage, vous avez perdu.")

        print(f"Votre nouveau solde est de {balance}.")

    print("Merci d'avoir joue !")

if __name__ == "__main__":
    main()
