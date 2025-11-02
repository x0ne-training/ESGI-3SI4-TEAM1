#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

void initializeGame(Player *p, Cell grid[GRID_SIZE][GRID_SIZE]) {
    p->x = 0;
    p->y = 0;
    p->life = 100;
    p->score = 0;

    srand(time(NULL));

    // Initialiser la grille à vide
    for (int i = 0; i < GRID_SIZE; i++)
        for (int j = 0; j < GRID_SIZE; j++)
            grid[i][j] = EMPTY;

    // Placer les trésors
    for (int i = 0; i < TREASURES; i++) {
        int tx, ty;
        do {
            tx = rand() % GRID_SIZE;
            ty = rand() % GRID_SIZE;
        } while (grid[tx][ty] != EMPTY || (tx==0 && ty==0));
        grid[tx][ty] = TREASURE;
    }

    // Placer les pièges
    for (int i = 0; i < TRAPS; i++) {
        int tx, ty;
        do {
            tx = rand() % GRID_SIZE;
            ty = rand() % GRID_SIZE;
        } while (grid[tx][ty] != EMPTY || (tx==0 && ty==0));
        grid[tx][ty] = TRAP;
    }
}

void displayGrid(Player *p, Cell grid[GRID_SIZE][GRID_SIZE]) {
    printf("\nGrille :\n");
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            if (i == p->x && j == p->y) printf(" P ");
            else printf(" ? ");
        }
        printf("\n");
    }
    printf("Vie : %d | Score : %d\n", p->life, p->score);
}

