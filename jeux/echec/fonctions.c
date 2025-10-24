#include <stdio.h>
#include <stdlib.h>
#include "echecs.h"

void initialiser_plateau(Jeu *jeu) {
    for (int i = 0; i < TAILLE; i++) {
        for (int j = 0; j < TAILLE; j++) {
            jeu->plateau[i][j] = VIDE;
        }
    }

    jeu->plateau[0][0] = TOUR_N;
    jeu->plateau[0][1] = CAVALIER_N;
    jeu->plateau[0][2] = FOU_N;
    jeu->plateau[0][3] = DAME_N;
    jeu->plateau[0][4] = ROI_N;
    jeu->plateau[0][5] = FOU_N;
    jeu->plateau[0][6] = CAVALIER_N;
    jeu->plateau[0][7] = TOUR_N;
    for (int j = 0; j < TAILLE; j++) {
        jeu->plateau[1][j] = PION_N;
    }

    for (int j = 0; j < TAILLE; j++) {
        jeu->plateau[6][j] = PION_B;
    }
    jeu->plateau[7][0] = TOUR_B;
    jeu->plateau[7][1] = CAVALIER_B;
    jeu->plateau[7][2] = FOU_B;
    jeu->plateau[7][3] = DAME_B;
    jeu->plateau[7][4] = ROI_B;
    jeu->plateau[7][5] = FOU_B;
    jeu->plateau[7][6] = CAVALIER_B;
    jeu->plateau[7][7] = TOUR_B;

    jeu->joueur_courant = 1;
    jeu->partie_finie = 0;
}

void afficher_plateau(Jeu *jeu) {
    printf("\n  a b c d e f g h\n");
    for (int i = 0; i < TAILLE; i++) {
        printf("%d ", 8 - i);
        for (int j = 0; j < TAILLE; j++) {
            char symbole;
            switch (jeu->plateau[i][j]) {
                case VIDE: symbole = '.'; break;
                case PION_B: symbole = 'P'; break;
                case TOUR_B: symbole = 'T'; break;
                case CAVALIER_B: symbole = 'C'; break;
                case FOU_B: symbole = 'F'; break;
                case DAME_B: symbole = 'D'; break;
                case ROI_B: symbole = 'R'; break;
                case PION_N: symbole = 'p'; break;
                case TOUR_N: symbole = 't'; break;
                case CAVALIER_N: symbole = 'c'; break;
                case FOU_N: symbole = 'f'; break;
                case DAME_N: symbole = 'd'; break;
                case ROI_N: symbole = 'r'; break;
                default: symbole = '?'; break;
            }
            printf("%c ", symbole);
        }
        printf("%d\n", 8 - i);
    }
    printf("  a b c d e f g h\n");
    printf("\nJoueur %s\n", jeu->joueur_courant == 1 ? "Blancs (majuscules)" : "Noirs (minuscules)");
}

int est_piece_du_joueur(int piece, int joueur) {
    if (joueur == 1) {
        return piece >= PION_B && piece <= ROI_B;
    }
    return piece >= PION_N && piece <= ROI_N;
}

int est_mouvement_valide(Jeu *jeu, int x1, int y1, int x2, int y2) {
    if (x1 < 0 || x1 >= TAILLE || y1 < 0 || y1 >= TAILLE ||
        x2 < 0 || x2 >= TAILLE || y2 < 0 || y2 >= TAILLE) {
        return 0;
    }

    int piece = jeu->plateau[x1][y1];
    int cible = jeu->plateau[x2][y2];

    if (piece == VIDE) return 0;
    if (!est_piece_du_joueur(piece, jeu->joueur_courant)) return 0;
    if (cible != VIDE && est_piece_du_joueur(cible, jeu->joueur_courant)) return 0;

    if (piece == PION_B || piece == PION_N) {
        int direction = (piece == PION_B) ? -1 : 1;
        if (y1 == y2 && x2 == x1 + direction && cible == VIDE) return 1;
        if (abs(y2 - y1) == 1 && x2 == x1 + direction && cible != VIDE) return 1;
    }

    if (piece == TOUR_B || piece == TOUR_N) {
        if (x1 == x2 || y1 == y2) return 1;
    }

    if (piece == CAVALIER_B || piece == CAVALIER_N) {
        int dx = abs(x2 - x1);
        int dy = abs(y2 - y1);
        if ((dx == 2 && dy == 1) || (dx == 1 && dy == 2)) return 1;
    }

    if (piece == FOU_B || piece == FOU_N) {
        if (abs(x2 - x1) == abs(y2 - y1)) return 1;
    }

    if (piece == DAME_B || piece == DAME_N) {
        if (x1 == x2 || y1 == y2 || abs(x2 - x1) == abs(y2 - y1)) return 1;
    }

    if (piece == ROI_B || piece == ROI_N) {
        if (abs(x2 - x1) <= 1 && abs(y2 - y1) <= 1) return 1;
    }

    return 0;
}

int deplacer_piece(Jeu *jeu, int x1, int y1, int x2, int y2) {
    if (!est_mouvement_valide(jeu, x1, y1, x2, y2)) {
        return 0;
    }

    int piece_capturee = jeu->plateau[x2][y2];
    if (piece_capturee == ROI_B || piece_capturee == ROI_N) {
        jeu->partie_finie = 1;
    }

    jeu->plateau[x2][y2] = jeu->plateau[x1][y1];
    jeu->plateau[x1][y1] = VIDE;

    return 1;
}

void changer_joueur(Jeu *jeu) {
    jeu->joueur_courant = (jeu->joueur_courant == 1) ? 2 : 1;
}

int partie_terminee(Jeu *jeu) {
    return jeu->partie_finie;
}