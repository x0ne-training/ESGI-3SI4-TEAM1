#include "functions.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

static int clamp(int v, int a, int b) {
    if (v < a) return a;
    if (v > b) return b;
    return v;
}

void init_game(GameState *g) {
    if (!g) return;
    g->count = 0;
    g->gold = 50;   // monnaie de départ
    g->day = 1;
    srand((unsigned)time(NULL));
}

bool add_dragon(GameState *g, const char *name) {
    if (!g || !name) return false;
    if (g->count >= MAX_DRAGONS) return false;
    Dragon *d = &g->dragons[g->count++];
    strncpy(d->name, name, NAME_LEN-1);
    d->name[NAME_LEN-1] = '\0';
    d->level = 1;
    d->health = 100;
    d->hunger = 0;
    d->attack = 10;
    d->alive = true;
    return true;
}

void show_dragon(const Dragon *d) {
    if (!d) return;
    printf("Nom : %s | Niveau : %d | PV : %d | Faim : %d | Att : %d | %s\n",
           d->name, d->level, d->health, d->hunger, d->attack,
           d->alive ? "Vivant" : "Mort");
}

