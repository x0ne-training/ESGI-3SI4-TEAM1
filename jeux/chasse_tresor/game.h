#ifndef GAME_H
#define GAME_H

#define GRID_SIZE 5
#define TREASURES 3
#define TRAPS 3

typedef struct {
    int x, y;
    int life;
    int score;
} Player;

typedef enum {
    EMPTY,
    TREASURE,
    TRAP
} Cell;

void initializeGame(Player *p, Cell grid[GRID_SIZE][GRID_SIZE]);
void displayGrid(Player *p, Cell grid[GRID_SIZE][GRID_SIZE]);
int movePlayer(Player *p, Cell grid[GRID_SIZE][GRID_SIZE], int choice);
int isGameOver(Player *p, Cell grid[GRID_SIZE][GRID_SIZE]);
void endGame(Player *p);

#endif
