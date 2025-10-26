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
