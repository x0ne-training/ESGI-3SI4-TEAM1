#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

int main() {
    srand(time(NULL));
    int numPlayers;
    printf("Nombre de joueurs: ");
    scanf("%d", &numPlayers);
    Player players[numPlayers];

    initPlayers(players, numPlayers);

    while(!gameOver(players, numPlayers)) {
        nightPhase(players, numPlayers);
        dayPhase(players, numPlayers);
        printStatus(players, numPlayers);
    }

    declareWinner(players, numPlayers);

    return 0;
}
