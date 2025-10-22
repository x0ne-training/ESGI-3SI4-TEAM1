#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "des.h"

int lancer_de(void) {
    return (rand() % 6) + 1;
}

void jouer_manche(void) {
    int joueur = lancer_de();
    int ordi = lancer_de();

    printf("Vous : %d\n", joueur);
    printf("Ordinateur : %d\n", ordi);

    if (joueur > ordi)
        printf("Vous gagnez.\n");
    else if (ordi > joueur)
        printf("Ordinateur gagne.\n");
    else
        printf("Egalite.\n");
}
