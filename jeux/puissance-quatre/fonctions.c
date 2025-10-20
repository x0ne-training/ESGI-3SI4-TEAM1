#include <stdio.h>
#include "puissance4.h"

char grille[LIGNES][COLONNES];
int victoires_rouge = 0;
int victoires_jaune = 0;
int matchs_nuls = 0;

void initialiserGrille() {
    for (int i = 0; i < LIGNES; i++) {
        for (int j = 0; j < COLONNES; j++) {
            grille[i][j] = ' ';
        }
    }
}

void afficherGrille() {
    printf("\n");
    printf("  1   2   3   4   5   6   7\n");

    for (int i = 0; i < LIGNES; i++) {
        printf("| ");
        for (int j = 0; j < COLONNES; j++) {
            if (grille[i][j] == 'R') {
                printf("%sR%s", ROUGE, RESET);
            } else if (grille[i][j] == 'J') {
                printf("%sJ%s", JAUNE, RESET);
            } else {
                printf(" ");
            }
            printf(" | ");
        }
        printf("\n");
    }

    printf("+---+---+---+---+---+---+---+\n");
}

int verifierVictoire() {
    // Vérifier lignes horizontales
    for (int i = 0; i < LIGNES; i++) {
        for (int j = 0; j < COLONNES - 3; j++) {
            if (grille[i][j] != ' ' &&
                grille[i][j] == grille[i][j+1] &&
                grille[i][j] == grille[i][j+2] &&
                grille[i][j] == grille[i][j+3]) {
                return VICTOIRE;
            }
        }
    }

    // Vérifier colonnes verticales
    for (int i = 0; i < LIGNES - 3; i++) {
        for (int j = 0; j < COLONNES; j++) {
            if (grille[i][j] != ' ' &&
                grille[i][j] == grille[i+1][j] &&
                grille[i][j] == grille[i+2][j] &&
                grille[i][j] == grille[i+3][j]) {
                return VICTOIRE;
            }
        }
    }

    // Vérifier diagonales descendantes (↘)
    for (int i = 0; i < LIGNES - 3; i++) {
        for (int j = 0; j < COLONNES - 3; j++) {
            if (grille[i][j] != ' ' &&
                grille[i][j] == grille[i+1][j+1] &&
                grille[i][j] == grille[i+2][j+2] &&
                grille[i][j] == grille[i+3][j+3]) {
                return VICTOIRE;
            }
        }
    }

    // Vérifier diagonales montantes (↗)
    for (int i = 3; i < LIGNES; i++) {
        for (int j = 0; j < COLONNES - 3; j++) {
            if (grille[i][j] != ' ' &&
                grille[i][j] == grille[i-1][j+1] &&
                grille[i][j] == grille[i-2][j+2] &&
                grille[i][j] == grille[i-3][j+3]) {
                return VICTOIRE;
            }
        }
    }

    return PAS_VICTOIRE;
}

int grillePleine() {
    for (int j = 0; j < COLONNES; j++) {
        if (grille[0][j] == ' ') {
            return GRILLE_NON_PLEINE;
        }
    }
    return GRILLE_PLEINE;
}

int colonneValide(int colonne) {
    if (colonne < 0 || colonne >= COLONNES) {
        return COLONNE_INVALIDE;
    }

    if (grille[0][colonne] != ' ') {
        return COLONNE_INVALIDE;
    }

    return COLONNE_VALIDE;
}

int placerJeton(int colonne, char joueur) {
    for (int i = LIGNES - 1; i >= 0; i--) {
        if (grille[i][colonne] == ' ') {
            grille[i][colonne] = joueur;
            return COLONNE_VALIDE;
        }
    }
    return COLONNE_INVALIDE;
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
    printf("%sJoueur Rouge : %d victoires%s\n", ROUGE, victoires_rouge, RESET);
    printf("%sJoueur Jaune : %d victoires%s\n", JAUNE, victoires_jaune, RESET);
    printf("Matchs nuls : %d\n", matchs_nuls);
    printf("============================\n");
}