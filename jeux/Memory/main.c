#include <stdio.h>
#include "memory.h"

int main() {
    Card board[SIZE][SIZE];
    initBoard(board);
    printf("Bienvenue dans le jeu de Memoire !\n");
    playGame(board);
    return 0;
}
