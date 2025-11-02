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

