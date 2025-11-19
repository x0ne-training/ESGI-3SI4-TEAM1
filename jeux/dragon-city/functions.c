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
