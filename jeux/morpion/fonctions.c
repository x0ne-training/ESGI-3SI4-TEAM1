#include <stdio.h>
#include "morpion.h"

char grille[3][3];

void initialiserGrille() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            grille[i][j] = ' ';
        }
    }
}