#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"
#include "questions.h"

void printStats(Stats stats) {
    printf("\n--- Statistiques du Royaume ---\n");
    printf("Pouvoir : %d\n", stats.power);
    printf("Richesse : %d\n", stats.money);
    printf("Foi : %d\n", stats.faith);
    printf("Peuple : %d\n", stats.people);
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

int isGameOver(Stats stats) {
    return (stats.power <= 0 || stats.money <= 0 ||
            stats.faith <= 0 || stats.people <= 0 ||
            stats.power >= 100 || stats.money >= 100 ||
            stats.faith >= 100 || stats.people >= 100);
}

void playGame() {
    srand(time(NULL));
    Stats stats = {50, 50, 50, 50};
    int turn = 0;

    printf("Bienvenue, Votre Majesté ! Gouvernez avec sagesse...\n");

    while (!isGameOver(stats)) {
        Question q = getRandomQuestion();
        printf("\nTour %d : %s\n", ++turn, q.question);
        printf("1) %s\n2) %s\nVotre choix : ", q.optionA, q.optionB);

        int choice;
        scanf("%d", &choice);

        if (choice == 1) applyChoice(1, &stats, q.effectsA);
        else applyChoice(2, &stats, q.effectsB);

        printStats(stats);
    }

    printf("\nVotre règne est terminé après %d tours.\n", turn);
}
