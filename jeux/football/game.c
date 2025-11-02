#include <stdio.h>
#include <stdlib.h>
#include "game.h"

int action_success(int skill) {
    return rand() % 100 < skill;
}

void print_stats(Player p) {
    printf("Stats - Tir:%d Passe:%d Dribble:%d Endurance:%d\n", p.tir, p.passe, p.dribble, p.endurance);
}

int get_player_choice() {
    int choice;
    printf("Que voulez-vous faire ?\n1. Tir\n2. Passe\n3. Dribble\n4. Défense\n> ");
    scanf("%d", &choice);
    return choice;
}
