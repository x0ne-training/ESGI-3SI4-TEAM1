#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "menteur-3000.h"

void intro() {
    system("cls");
    printf("🤥 Bienvenue dans le JEU DU MENTEUR 3000 🤥\n\n");
    printf("Je suis une IA ultra sophistiquée (selon moi).\n");
    printf("Je vais détecter si tu mens grâce à mes... 'algorithmes secrets'.\n\n");
}

void poser_question(const char *question, char *reponse, int taille) {
    printf("%s ", question);
    fgets(reponse, taille, stdin);
    reponse[strcspn(reponse, "\n")] = 0;
}

void analyse(const char *reponse) {
    srand((unsigned)time(NULL) + rand());
    int chance = rand() % 3; // 0, 1 ou 2
    if (strlen(reponse) == 0) {
        printf("Tu ne dis rien ? CLASSIQUE du menteur professionnel 😏\n");
    } else if (chance == 0) {
        printf("Je te crois... (mais je te surveille 👀)\n");
    } else if (chance == 1) {
        printf("Mouais... Ça sent le mensonge à plein nez ! 😤\n");
    } else {
        printf("HAHA tu crois me tromper ? C’est clairement un bobard 😂\n");
    }
}

