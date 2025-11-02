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

void apply_choice(int choice, Player *player, Player *adversaire, int *score_player, int *score_adv) {
    switch(choice) {
        case 1:
            if(action_success(player->tir)) {
                printf("But pour vous !\n");
                (*score_player)++;
            } else {
                printf("Tir manqué.\n");
            }
            break;
        case 2:
            printf(action_success(player->passe) ? "Passe réussie.\n" : "Passe échouée.\n");
            break;
        case 3:
            printf(action_success(player->dribble) ? "Dribble réussi.\n" : "Perte de balle.\n");
            break;
        case 4:
            printf("Défense...\n");
            if(action_success(adversaire->tir)) {
                printf("L'adversaire marque pendant votre défense !\n");
                (*score_adv)++;
            }
            break;
        default:
            printf("Choix invalide.\n");
    }

    // Tour aléatoire adversaire
    if(rand() % 2 == 0 && action_success(adversaire->tir)) {
        printf("L'adversaire tire... et marque !\n");
        (*score_adv)++;
    }
}
