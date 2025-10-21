#include <stdio.h
#include <stdlib.h>
#include <time.h>
#include "pfc.h"

int victoires_joueur = 0;
int victoires_ordi = 0;
int egalites = 0;

int choixOrdinateur(){
    int choix;
    choix = (rand() % 3) + 1;
    return choix;
}


int determinerGagnant(int choix_joueur, int choix_ordi) {
    int resultat;

    if (choix_joueur == choix_ordi) {
        resultat = EGALITE;
        return resultat;
    }

    if ((choix_joueur == PIERRE && choix_ordi == CISEAUX) ||
        (choix_joueur == FEUILLE && choix_ordi == PIERRE) ||
        (choix_joueur == CISEAUX && choix_ordi == FEUILLE)) {
        resultat = JOUEUR_GAGNE;
        return resultat;
    }

    resultat = ORDI_GAGNE;
    return resultat;
}
