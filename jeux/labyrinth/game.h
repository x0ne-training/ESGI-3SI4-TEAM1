#ifndef GAME_H
#define GAME_H

#include "player.h"
#include "maze.h"

void initializePlayer(Player *p);
void playTurn(Player *p, Maze *m);
int isGameOver(Player *p, Maze *m);
void endGame(Player *p, Maze *m);

#endif
