#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "game.h"

void display_card(const char *value, const char *suit) {
    printf("┌─────────┐\n");
    printf("│%-2s       │\n", value);
    printf("│         │\n");
    printf("│    %s    │\n", suit);
    printf("│         │\n");
    printf("│       %-2s│\n", value);
    printf("└─────────┘\n");
}

int random_choice(int n) {
    return rand() % n;
}

void play_game() {
    srand(time(NULL));

    int playerLives = 3;
    int computerLives = 3;
    int round = 1;

    printf("=== Jeu du Menteur ===\n");
    printf("Chaque joueur commence avec 3 vies.\n");

    while (playerLives > 0 && computerLives > 0) {
        printf("\n--- Tour %d ---\n", round);

        // Le joueur annonce sa carte
        char announcedValue[10];
        printf("Annoncez la valeur de votre carte (ex: As, Roi, 7, etc.) : ");
        scanf("%9s", announcedValue);

        printf("Vous posez une carte annoncée comme un %s !\n", announcedValue);
        printf("Votre carte :\n");
        display_card(announcedValue, "♠");

        // Décision aléatoire de l’ordinateur (1/3 de chance de dire menteur)
        int computerSaysLiar = random_choice(3) == 0;

        if (computerSaysLiar) {
            printf("\n🤖 L'ordinateur dit : \"Menteur !\"\n");

            int youWereLying = random_choice(2); // 50 % de chance de mentir
            if (youWereLying) {
                printf("💀 Vous mentiez ! Vous perdez 1 vie.\n");
                playerLives--;
            } else {
                printf("😎 Vous disiez la vérité ! L'ordinateur perd 1 vie.\n");
                computerLives--;
            }
        } else {
            printf("\n🤖 L'ordinateur vous croit.\n");
        }

        printf("Vies restantes — Vous : %d | Ordinateur : %d\n", playerLives, computerLives);
        round++;
    }

    if (playerLives <= 0)
        printf("\n💀 Vous avez perdu le jeu !\n");
    else
        printf("\n🏆 Vous avez gagné contre l'ordinateur !\n");
}
