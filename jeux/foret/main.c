#include <stdio.h>
#include "game.h"

int main(void) {
    printf("Bienvenue dans *La Forêt Maudite*\n");
    printf("Votre objectif : survivre le plus longtemps possible.\n");

    Player player;
    initializePlayer(&player);

    while (!isGameOver(&player)) {
        displayStats(&player);
        playTurn(&player);
    }

    endGame(&player);
    return 0;
}
