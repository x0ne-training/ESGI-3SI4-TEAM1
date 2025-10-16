#ifndef FONCTIONS_H
#define FONCTIONS_H

#include <stdbool.h>

#define TAILLE 10
#define NB_BATEAUX 5

typedef enum {
    VIDE = 0,
    BATEAU,
    TOUCHÉ,
    MANQUÉ,
    COULÉ
} Case;

typedef struct {
    int x, y;
} Point;


#endif
x
};