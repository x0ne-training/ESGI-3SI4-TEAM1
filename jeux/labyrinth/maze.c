#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "maze.h"
#include "player.h"

void generateMaze(Maze *m, int rows, int cols) {
    m->rows = rows;
    m->cols = cols;
    m->grid = malloc(sizeof(char*) * rows);
    for (int i = 0; i < rows; i++) {
        m->grid[i] = malloc(sizeof(char) * cols);
        for (int j = 0; j < cols; j++) {
            if (rand() % 4 == 0) m->grid[i][j] = '#';
            else m->grid[i][j] = '.';
        }
    }
    m->exitX = rows - 1;
    m->exitY = cols - 1;
    m->grid[m->exitX][m->exitY] = 'E';
}

void displayMaze(Maze *m, void *p) {
    Player *player = (Player*)p;
    for (int i = 0; i < m->rows; i++) {
        for (int j = 0; j < m->cols; j++) {
            if (i == player->x && j == player->y) printf("P ");
            else printf("%c ", m->grid[i][j]);
        }
        printf("\n");
    }
}
