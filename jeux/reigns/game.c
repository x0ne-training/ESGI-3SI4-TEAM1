#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"
#include "questions.h"

void printStats(Stats stats) {
    printf("\n--- Statistiques du Royaume ---\n");
    printf("👑 Pouvoir : %d\n", stats.power);
    printf("💰 Richesse : %d\n", stats.money);
    printf("😇 Foi : %d\n", stats.faith);
    printf("🧑‍🌾 Peuple : %d\n", stats.people);
    printf("-------------------------------\n");
}

void applyChoice(int choice, Stats *stats, int effects[4]) {
    stats->power  += effects[0];
    stats->money  += effects[1];
    stats->faith  += effects[2];
    stats->people += effects[3];

    if (stats->power < 0) stats->power = 0;
    if (stats->money < 0) stats->money = 0;
    if (stats->faith < 0) stats->faith = 0;
    if (stats->people < 0) stats->people = 0;
}

