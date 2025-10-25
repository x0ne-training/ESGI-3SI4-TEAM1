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

void displayBoard(Joueur joueurs[NB_JOUEURS]) {
    printf("\n--- Plateau ---\n");
    for(int i = 0; i < NB_JOUEURS; i++) {
        printf("%s: ", joueurs[i].nom);
        for(int j = 0; j < PIONS_PAR_JOUEUR; j++) {
            if(joueurs[i].pions[j].finished)
                printf("[F] ");
            else if(joueurs[i].pions[j].atHome)
                printf("[H] ");
            else
                printf("[%d] ", joueurs[i].pions[j].position);
        }
        printf("\n");
    }
}

int lancerDe() {
    return rand() % 6 + 1;
}

void movePion(Joueur *joueur, int pionIndex, int de) {
    Pion *pion = &joueur->pions[pionIndex];

    if(pion->finished) {
        printf("Ce pion est deja arrive.\n");
        return;
    }

    if(pion->atHome) {
        if(de == 6) {
            pion->position = 1;
            pion->atHome = 0;
            printf("%s sort un pion de la maison !\n", joueur->nom);
        } else {
            printf("%s ne peut pas sortir le pion (besoin de 6).\n", joueur->nom);
        }
        return;
    }

    pion->position += de;
    if(pion->position >= CASES_TOTAL) {
        pion->position = CASES_TOTAL;
        pion->finished = 1;
        printf("%s a amene un pion a la fin !\n", joueur->nom);
    } else {
        printf("%s deplace un pion de %d cases.\n", joueur->nom, de);
    }
}

int isGameOver(Joueur joueurs[NB_JOUEURS]) {
    for(int i = 0; i < NB_JOUEURS; i++) {
        for(int j = 0; j < PIONS_PAR_JOUEUR; j++) {
            if(!joueurs[i].pions[j].finished)
                return 0;
        }
    }
    return 1;
}
