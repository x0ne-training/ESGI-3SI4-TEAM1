#ifndef LABYRINTHE_H
#define LABYRINTHE_H

#define SIZE 10

typedef struct {
    int x;
    int y;
} Position;

void initLabyrinthe(char lab[SIZE][SIZE], Position *player, Position *exitPos);
void afficherLabyrinthe(char lab[SIZE][SIZE], Position player);
int deplacer(char lab[SIZE][SIZE], Position *player, char direction);
int estSortie(Position player, Position exitPos);

#endif