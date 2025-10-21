import sys

# Création du tableau de jeu
board = [' ' for _ in range(9)]

# Fonction pour afficher le tableau de jeu
def print_board():
    """Affiche la grille de morpion dans la console."""
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Fonction pour vérifier si un joueur a gagné
def check_win(player):
    """Vérifie toutes les conditions de victoire pour un joueur donné."""
    # Vérification des lignes
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player):
        return True
    # Vérification des colonnes
    elif (board[0] == player and board[3] == player and board[6] == player) or \
         (board[1] == player and board[4] == player and board[7] == player) or \
         (board[2] == player and board[5] == player and board[8] == player):
        return True
    # Vérification des diagonales
    elif (board[0] == player and board[4] == player and board[8] == player) or \
         (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Fonction pour vérifier si le tableau est plein (match nul)
def check_draw():
    """Vérifie si la partie est un match nul."""
    if ' ' not in board:
        return True
    else:
        return False

def lancer_partie():
    """
    Contient la boucle principale du jeu.
    Retourne un code indiquant le résultat de la partie.
    - 0: Match Nul
    - 1: Joueur X a gagné
    - 2: Joueur O a gagné
    """
    current_player = 'X'
    while True:
        print_board()

        # Tour du joueur actuel
        while True:
            try:
                move = int(input(f"Joueur {current_player}, entrez votre coup (1-9) : ")) - 1
                if 0 <= move <= 8:
                    if board[move] == ' ':
                        board[move] = current_player
                        break
                    else:
                        print("Cette case est déjà prise !")
                else:
                    print("Veuillez entrer un nombre entre 1 et 9.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        # Vérification de la victoire
        if check_win(current_player):
            print_board()
            print(f"Le joueur {current_player} a gagné !")
            if current_player == 'X':
                return 1
            else: # current_player == 'O'
                return 2

        # Vérification du match nul
        if check_draw():
            print_board()
            print("Match nul !")
            return 0

        # Changement de joueur
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


# --- POINT D'ENTRÉE PRINCIPAL ---
if __name__ == "__main__":
    print("--- Lancement du jeu de Morpion ---")
    
    # Lance la partie et récupère le résultat
    code_de_retour = lancer_partie()
    
    print(f"--- Fin de la partie. Le programme se termine avec le code {code_de_retour}. ---")
    
    # Termine le script en renvoyant le code de retour au système
    sys.exit(code_de_retour)
