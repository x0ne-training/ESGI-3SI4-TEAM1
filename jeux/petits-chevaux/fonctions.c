#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "petitschevaux.h"

void initGame(Joueur joueurs[NB_JOUEURS]) {
    for(int i = 0; i < NB_JOUEURS; i++) {
        printf("Entrez le nom du joueur %d : ", i+1);
        scanf("%19s", joueurs[i].nom);
        for(int j = 0; j < PIONS_PAR_JOUEUR; j++) {
            joueurs[i].pions[j].position = 0;
            joueurs[i].pions[j].atHome = 1;
            joueurs[i].pions[j].finished = 0;
        }
    }
    srand((unsigned int)time(NULL));
}

