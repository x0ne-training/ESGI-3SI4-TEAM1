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

    int newX = p->x;
    int newY = p->y;

    switch (choice) {
        case 'Z': case 'z': newX--; break;
        case 'S': case 's': newX++; break;
        case 'Q': case 'q': newY--; break;
        case 'D': case 'd': newY++; break;
        default: printf("Choix invalide !\n"); return;
    }

    
