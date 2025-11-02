#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

int main() {
    srand(time(NULL));
    Player player = {70, 80, 60, 100};
    Player adversaire = {65, 75, 55, 100};

    int score_player = 0, score_adv = 0;
    int minute;

    printf("Bienvenue dans CLI-FIFA 25 !\n");

    for(minute = 1; minute <= 5; minute++) {  // match court pour test
        printf("\n--- Minute %d ---\n", minute);
        print_stats(player);

        int choice = get_player_choice();
        apply_choice(choice, &player, &adversaire, &score_player, &score_adv);
    }

    printf("\nMatch terminé ! Score final : Vous %d - Adversaire %d\n", score_player, score_adv);
    return 0;
}
