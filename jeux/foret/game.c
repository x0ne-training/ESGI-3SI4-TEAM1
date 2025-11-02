#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

void initializePlayer(Player *p) {
    p->health = 100;
    p->energy = 100;
    p->food = 3;
    p->day = 1;
    srand(time(NULL));
}

void displayStats(Player *p) {
    printf("\n=== JOUR %d ===\n", p->day);
    printf("Santé : %d | Énergie : %d | Nourriture : %d\n", p->health, p->energy, p->food);
}

