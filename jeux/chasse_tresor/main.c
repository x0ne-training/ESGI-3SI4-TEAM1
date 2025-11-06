#include <stdio.h>
#include "game.h"

int main() {
    Player player;
    Cell grid[GRID_SIZE][GRID_SIZE];

    initializeGame(&player, grid);

    while (!isGameOver(&player, grid)) {
        displayGrid(&player, grid);
        printf("\nDéplacez-vous : 1=Haut, 2=Bas, 3=Gauche, 4=Droite : ");
        int choice;
        scanf("%d", &choice);
        movePlayer(&player, grid, choice);
    }

    endGame(&player);
    return 0;
}
