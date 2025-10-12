#include <stdio.h>
#include "morpion.h"

char grille[3][3];
int victoires_x = 0;
int victoires_o = 0;
int matchs_nuls = 0;

void initialiserGrille() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            grille[i][j] = ' ';
        }
    }
}

void afficherGrille() {
    printf("\n");
    printf("  1   2   3\n");
    for (int i = 0; i < 3; i++) {
        printf("%d ", i + 1);
        for (int j = 0; j < 3; j++) {
            if (grille[i][j] == 'X') {
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

int verifierVictoire() {
    // Vérifie les lignes
    for (int i = 0; i < 3; i++) {
        if (grille[i][0] != ' ' && grille[i][0] == grille[i][1] && grille[i][1] == grille[i][2]) {
            return VICTOIRE;
        }
    }

    // Vérifie les colonnes
    for (int j = 0; j < 3; j++) {
        if (grille[0][j] != ' ' && grille[0][j] == grille[1][j] && grille[1][j] == grille[2][j]) {
            return VICTOIRE;
        }
    }

    // Vérifie diagonale descendante
    if (grille[0][0] != ' ' && grille[0][0] == grille[1][1] && grille[1][1] == grille[2][2]) {
        return VICTOIRE;
    }

    // Vérifie diagonale montante
    if (grille[0][2] != ' ' && grille[0][2] == grille[1][1] && grille[1][1] == grille[2][0]) {
        return VICTOIRE;
    }

    return PAS_VICTOIRE;
}

int grillePleine() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (grille[i][j] == ' ') {
                return GRILLE_NON_PLEINE;
            }
        }
    }

    return GRILLE_PLEINE;
}

int demanderRejouer() {
    char reponse;
    int rejouer = NE_PAS_REJOUER;

    printf("\nVoulez-vous rejouer ? (o/n) : ");
    scanf(" %c", &reponse);

    if (reponse == 'o' || reponse == 'O') {
        rejouer = REJOUER;
    }

    return rejouer;
}

void afficherScores() {
    printf("\n========== SCORES ==========\n");
    printf("%sJoueur X : %d victoires%s\n", ROUGE, victoires_x, RESET);
    printf("%sJoueur O : %d victoires%s\n", BLEU, victoires_o, RESET);
    printf("Matchs nuls : %d\n", matchs_nuls);
    printf("============================\n");
}