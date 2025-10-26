#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "qi-patate.h"

void intro() {
    system("cls");
    printf("Bienvenue dans le JEU DU QI DE PATATE\n\n");
    printf("Reponds aux questions et je calculerai ton QI de patate.\n\n");
}

void poser_question(const char *question, char *reponse, int taille) {
    printf("%s ", question);
    fgets(reponse, taille, stdin);
    reponse[strcspn(reponse, "\n")] = 0;
}

void analyse(const char *reponse) {
    srand((unsigned)time(NULL) + rand());
    int r = rand() % 3;
    if (strlen(reponse) == 0) {
        printf("Tu n'as rien repondu, patate silencieuse.\n\n");
    } else if (r == 0) {
        printf("Interressant choix.\n\n");
    } else if (r == 1) {
        printf("Hum, patate douteuse...\n\n");
    } else {
        printf("Ceci va influencer ton QI de patate.\n\n");
    }
}

void verdict_final() {
    srand((unsigned)time(NULL));
    int qi = rand() % 101; // 0 a 100
    printf("Ton QI de patate est de %d.\n", qi);
    if (qi < 20) {
        printf("Incroyable ! Meme une patate de jardin est plus intelligente.\n");
    } else if (qi < 50) {
        printf("Tu es une patate moyenne, rien de special.\n");
    } else if (qi < 80) {
        printf("Bravo ! Patate bien avancee.\n");
    } else {
        printf("Exceptionnel ! Patate de genie.\n");
    }
    printf("\nMerci d'avoir joue au QI de patate !\n");
}
