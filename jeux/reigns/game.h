#ifndef GAME_H
#define GAME_H

#define MAX_NAME 50

typedef struct {
    int power;
    int money;
    int faith;
    int people;
} Stats;

void playGame();
void applyChoice(int choice, Stats *stats, int effects[4]);
int isGameOver(Stats stats);
void printStats(Stats stats);

#endif
