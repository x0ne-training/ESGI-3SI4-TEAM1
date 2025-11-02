#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "utils.h"

int lire_entier() {
    int x;
    while(scanf("%d", &x) != 1) {
        while(getchar() != '\n');
        printf("Veuillez entrer un nombre valide : ");
    }
    return x;
}

int hasard(int min, int max) {
    static int init = 0;
    if(!init) {
        srand(time(NULL));
        init = 1;
    }
    return rand() % (max - min + 1) + min;
}

char* nom_carte(int valeur) {
    switch(valeur) {
        case 1: return "As";
        case 11: return "Valet";
        case 12: return "Dame";
        case 13: return "Roi";
        default: ;
    }
    static char buf[3];
    sprintf(buf, "%d", valeur);
    return buf;
}
