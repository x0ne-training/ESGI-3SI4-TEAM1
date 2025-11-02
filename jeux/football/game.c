#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

void applyChoice(int choice, Stats *stats) {
    // Actions possibles :
    // 1 = Attaque, 2 = Défense, 3 = Dribble
    switch (choice) {
        case 1: // Attaque
            stats->energy -= 5;
            stats->goals += rand() % 2; // 0 ou 1 but
            stats->morale += 2;
            break;
        case 2: // Défense
            stats->energy -= 3;
            stats->fouls += rand() % 2;
            stats->morale += 1;
            break;
        case 3: // Dribble
            stats->energy -= 4;
            if(rand() % 2) stats->goals += 1;
            stats->morale += 1;
            break;
        default:
            printf("Action invalide!\n");
    }
}

void playMatch(Stats *player, Stats *opponent) {
    int rounds = 5;
    for (int i = 0; i < rounds; i++) {
        printf("\n--- Tour %d ---\n", i + 1);
        int choice;
        printf("Choisissez votre action (1=Attaque, 2=Défense, 3=Dribble): ");
        scanf("%d", &choice);
        applyChoice(choice, player);

        // Action aléatoire de l'adversaire
        int op_choice = rand() % 3 + 1;
        applyChoice(op_choice, opponent);

        printf("Votre stats:\n");
        displayStats(player);
        printf("Adversaire stats:\n");
        displayStats(opponent);
    }

    printf("\n=== Résultat du match ===\n");
    if (player->goals > opponent->goals) printf("Vous avez gagné !\n");
    else if (player->goals < opponent->goals) printf("Vous avez perdu !\n");
    else printf("Match nul !\n");
}

void displayStats(Stats *stats) {
    printf("Énergie: %d | Morale: %d | Buts: %d | Fautes: %d\n",
        stats->energy, stats->morale, stats->goals, stats->fouls);
}
