#ifndef GAME_H
#define GAME_H

#include "player.h"

void initializePlayer(Player *p);
void playTurn(Player *p);
void displayStats(Player *p);
int isGameOver(Player *p);
void endGame(Player *p);

#endif
