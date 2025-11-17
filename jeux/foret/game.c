#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

void initializePlayer(Player *p) {
    p->health = 100;
    p->energy = 100;
    p->food = 3;
    p->day = 1;
    srand(time(NULL));
}

void displayStats(Player *p) {
    printf("\n=== JOUR %d ===\n", p->day);
    printf("Santé : %d | Énergie : %d | Nourriture : %d\n", p->health, p->energy, p->food);
}

void playTurn(Player *p) {
    int choice;
    printf("\nQue voulez-vous faire ?\n");
    printf("1. Explorer la forêt\n");
    printf("2. Chasser pour trouver de la nourriture\n");
    printf("3. Se reposer\n");
    printf("Choix : ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Vous explorez la forêt...\n");
            int event = rand() % 3;
            if (event == 0) {
                printf("Vous êtes attaqué par un loup ! Vous perdez 20 points de santé.\n");
                p->health -= 20;
            } else if (event == 1) {
                printf("Vous trouvez des baies ! +1 nourriture.\n");
                p->food += 1;
            } else {
                printf("Rien d'intéressant, mais la forêt est belle.\n");
            }
            p->energy -= 15;
            break;

        case 2:
            if (rand() % 2) {
                printf("Vous avez chassé un lapin ! +2 nourriture.\n");
                p->food += 2;
            } else {
                printf("Vous n'avez rien trouvé.\n");
            }
            p->energy -= 20;
            break;

        case 3:
            printf("Vous vous reposez et regagnez de l'énergie.\n");
            p->energy += 30;
            if (p->energy > 100) p->energy = 100;
            p->health += 10;
            if (p->health > 100) p->health = 100;
            break;

        default:
            printf("Choix invalide.\n");
            return;
    }

    if (p->food > 0) {
        p->food--;
        printf("Vous mangez un peu de nourriture.\n");
    } else {
        printf("Vous avez faim et perdez de la santé.\n");
        p->health -= 10;
    }

    p->day++;
}

int isGameOver(Player *p) {
    return p->health <= 0 || p->energy <= 0;
}

void endGame(Player *p) {
    printf("\nVous n'avez pas survécu à la Forêt Maudite...\n");
    printf("Vous avez tenu %d jours.\n", p->day);
}
