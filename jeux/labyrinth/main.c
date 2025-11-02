#include <stdio.h>
#include <stdlib.h>
#include "game.h"

int main() {
    Player player;
    initializePlayer(&player);

    Maze maze;
    generateMaze(&maze, 5, 5); // 5x5 labyrinth

    printf("Bienvenue dans le Labyrinthe ! Trouvez la sortie.\n");

    while (!isGameOver(&player, &maze)) {
        displayMaze(&maze, &player);
        playTurn(&player, &maze);
    }

    endGame(&player, &maze);

    freeMaze(&maze);
    return 0;
}
