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

int movePlayer(Player *p, Cell grid[GRID_SIZE][GRID_SIZE], int choice) {
    int newX = p->x;
    int newY = p->y;

    switch (choice) {
        case 1: newX--; break; // haut
        case 2: newX++; break; // bas
        case 3: newY--; break; // gauche
        case 4: newY++; break; // droite
        default: printf("Choix invalide.\n"); return 0;
    }

    if (newX < 0 || newX >= GRID_SIZE || newY < 0 || newY >= GRID_SIZE) {
        printf("Vous ne pouvez pas sortir de la grille !\n");
        return 0;
    }

    p->x = newX;
    p->y = newY;

    if (grid[p->x][p->y] == TREASURE) {
        printf("Vous avez trouvé un trésor ! +10 points\n");
        p->score += 10;
        grid[p->x][p->y] = EMPTY;
    } else if (grid[p->x][p->y] == TRAP) {
        printf("Vous êtes tombé dans un piège ! -20 vie\n");
        p->life -= 20;
        grid[p->x][p->y] = EMPTY;
    } else {
        printf("Rien ici...\n");
    }
    return 1;
}

int isGameOver(Player *p, Cell grid[GRID_SIZE][GRID_SIZE]) {
    if (p->life <= 0) return 1;

    // vérifier si tous les trésors ont été collectés
    for (int i = 0; i < GRID_SIZE; i++)
        for (int j = 0; j < GRID_SIZE; j++)
            if (grid[i][j] == TREASURE) return 0;

    return 1;
}


