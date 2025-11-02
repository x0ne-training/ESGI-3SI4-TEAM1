#ifndef GAME_H
#define GAME_H

#include "stats.h"

void applyChoice(int choice, Stats *stats);
void playMatch(Stats *player, Stats *opponent);
void displayStats(Stats *stats);

#endif // GAME_H
