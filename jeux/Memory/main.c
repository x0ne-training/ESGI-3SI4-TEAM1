#include <stdio.h>
#include "memory.h"

int main() {
    Card board[SIZE][SIZE];

    printf("Bienvenue dans le jeu de memoire !\n");
    printf("Trouvez toutes les paires de cartes identiques.\n\n");

    initBoard(board);
    playGame(board);

    return 0;
}

