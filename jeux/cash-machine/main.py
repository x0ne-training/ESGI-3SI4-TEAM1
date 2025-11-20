import random
import time

SYMBOLS = {
    'Cerise': {'icon': '🍒', 'value': 2},
    'Orange': {'icon': '🍊', 'value': 3},
    'Citron': {'icon': '🍋', 'value': 4},
    'Bar':    {'icon': '🍫', 'value': 5},
    'Sept':   {'icon': '７', 'value': 10}
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
        return bet * SYMBOLS[symbol]['value']
    return 0

def print_reels(reels):
    """
    Affiche les rouleaux avec une animation simple.
    """
    icons = [SYMBOLS[symbol]['icon'] for symbol in reels]
    print(" | ".join(icons), end='\r')
    time.sleep(1)
    print(" | ".join(icons))


def main():
    """
    Fonction principale du jeu de machine a sous.
    """
    balance = 100
    print("=" * 30)
    print("  BIENVENUE A LA MACHINE A SOUS  ")
    print("=" * 30)
    print(f"Votre solde de depart est de {balance} credits.")

    while balance > 0:
        print("-" * 30)
        try:
            bet = int(input(f"Solde: {balance} | Combien voulez-vous miser ? (0 pour quitter) "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue


        if bet == 0:
            break

        if not 0 < bet <= balance:
            print("Mise invalide. Veuillez miser un montant entre 1 et votre solde.")
            continue

        balance -= bet
        print("Tirage en cours...")
        result = spin_reels()
        print_reels(result)

        winnings = calculate_winnings(result, bet)
        if winnings > 0:
            print(f"🎉 Felicitations ! Vous avez gagne {winnings} credits ! 🎉")
            balance += winnings
        else:
            print("😕 Dommage, vous avez perdu. 😕")

        print(f"Votre nouveau solde est de {balance} credits.")

    print("=" * 30)
    print("Merci d'avoir joue ! A bientot !")
    print("=" * 30)


if __name__ == "__main__":
    main()
