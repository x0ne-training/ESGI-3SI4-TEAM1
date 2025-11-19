#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "sims.h"

static int clamp(int v, int a, int b) {
    if (v < a) return a;
    if (v > b) return b;
    return v;
}

void init_sims(SimsState *s, const char *name) {
    strncpy(s->name, name, MAX_NAME - 1);
    s->name[MAX_NAME - 1] = '\0';
    s->hunger = 70;
    s->energy = 70;
    s->mood = 70;
    s->money = 100;
    s->day = 1;
    s->alive = 1;
}

void init_game(Game *g) {
    g->count = 0;
    g->current = -1;
}

