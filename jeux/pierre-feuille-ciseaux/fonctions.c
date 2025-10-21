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

