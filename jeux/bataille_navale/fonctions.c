#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "fonctions.h"


const BateauInfo BATEAUX[NB_BATEAUX] = {
        {5, "Porte-avions"},
        {4, "Croiseur"},
        {3, "Contre-torp"},
        {3, "Sous-marin"},
        {2, "Torpilleur"}
};

void init_plateau(Case p[TAILLE][TAILLE]) {
    for (int i=0;i<TAILLE;i++)
        for (int j=0;j<TAILLE;j++)
            p[i][j] = VIDE;
}

