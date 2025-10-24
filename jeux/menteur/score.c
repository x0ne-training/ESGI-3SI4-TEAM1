#include <stdio.h>
#include "score.h"

static int joueur_vies;
static int ordi_vies;

void init_vies() {
    joueur_vies = 3;
    ordi_vies = 3;
}

void perdre_vie_joueur() {
    joueur_vies--;
    printf("Vies joueur restantes : %d\n", joueur_vies);
}

void perdre_vie_ordi() {
    ordi_vies--;
    printf("Vies ordinateur restantes : %d\n", ordi_vies);
}

int fin_jeu() {
    return joueur_vies <= 0 || ordi_vies <= 0;
}

int vies_joueur() { return joueur_vies; }
int vies_ordi() { return ordi_vies; }
