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

void AfficherGrille(){
    printf("\n");
    printf("  1   2   3\n");
    for (int i = 0; i < 3; i++){
        printf("%d ", i + 1);
        for (int j = 0; j < 3; j++){
            if grille[i][j] == 'X') {
                printf("%sX%s", ROUGE, RESET);
            } else if (grille[i][j] == 'O') {
                printf("%sO%s", BLEU, RESET);
            } else {
                printf(" ");
            }
            if (j < 2) printf(" | ");
        }
        printf("\n");
        if (i < 2) printf("  --+---+--\n");
    }
}