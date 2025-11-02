#ifndef GAME_H
#define GAME_H

#include "player.h"

void initPlayers(Player players[], int numPlayers);
void printStatus(Player players[], int numPlayers);
void nightPhase(Player players[], int numPlayers);
void dayPhase(Player players[], int numPlayers);
int gameOver(Player players[], int numPlayers);
void declareWinner(Player players[], int numPlayers);

#endif
