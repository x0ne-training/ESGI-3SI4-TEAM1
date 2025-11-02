#include <stdio.h>
#include "game.h"

void initializePlayer(Player *p) {
    p->x = 0;
    p->y = 0;
    p->health = 100;
}

void playTurn(Player *p, Maze *m) {
    char choice;
    printf("\nDéplacez-vous (Z=haut, S=bas, Q=gauche, D=droite) : ");
    scanf(" %c", &choice);

    