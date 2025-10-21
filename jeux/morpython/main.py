# Création du tableau de jeu
board = [' ' for _ in range(9)]

# Fonction pour afficher le tableau de jeu
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Fonction pour vérifier si un joueur a gagné
def check_win(player):
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
    if ' ' not in board:
        return True
    else:
        return False

# Boucle principale du jeu
while True:
    print_board()

    # Tour du joueur X
    while True:
        try:
            move = int(input("Joueur X, entrez votre coup (1-9) : ")) - 1
            if move >= 0 and move <= 8:
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("Cette case est déjà prise !")
            else:
                print("Veuillez entrer un nombre entre 1 et 9.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Vérification de la victoire du joueur X
    if check_win('X'):
        print_board()
        print("Le joueur X a gagné !")
        break

    # Vérification du match nul
    if check_draw():
        print_board()
        print("Match nul !")
        break

    print_board()

    # Tour du joueur O
    while True:
        try:
            move = int(input("Joueur O, entrez votre coup (1-9) : ")) - 1
            if move >= 0 and move <= 8:
                if board[move] == ' ':
                    board[move] = 'O'
                    break
                else:
                    print("Cette case est déjà prise !")
            else:
                print("Veuillez entrer un nombre entre 1 et 9.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


    # Vérification de la victoire du joueur O
    if check_win('O'):
        print_board()
        print("Le joueur O a gagné !")
        break

    # Vérification du match nul
    if check_draw():
        print_board()
        print("Match nul !")
        break
