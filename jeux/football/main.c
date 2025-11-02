#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"
#include "questions.h"
#include "stats.h"

int main() {
    srand(time(NULL)); // Pour l'aléatoire

    Stats player = {100, 50, 0, 0};
    Stats opponent = {100, 50, 0, 0};

    printf("Bienvenue dans Mini FIFA CLI !\n");
    playMatch(&player, &opponent);

    return 0;
}
