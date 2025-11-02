#include <stdio.h>
#include <stdlib.h>
#include "game.h"

int action_success(int skill) {
    return rand() % 100 < skill;
}

void print_stats(Player p) {
    printf("Stats - Tir:%d Passe:%d Dribble:%d Endurance:%d\n", p.tir, p.passe, p.dribble, p.endurance);
}
