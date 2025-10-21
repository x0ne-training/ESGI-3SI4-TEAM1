#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mastermind.h"

int code_secret[LONGUEUR_CODE];
int tentatives[NB_TENTATIVES_MAX][LONGUEUR_CODE];
int nb_tentatives = 0;
int victoires = 0;
int defaites = 0;

void genererCodeSecret() {
    int i;

    for (i = 0; i < LONGUEUR_CODE; i++) {
        code_secret[i] = (rand() % NB_COULEURS) + 1;
    }
}

void afficherReglesCouleurs() {
    printf("\nCouleurs disponibles :\n");
    printf("1 - %sRouge%s\n", ROUGE, RESET);
    printf("2 - %sVert%s\n", VERT, RESET);
    printf("3 - %sJaune%s\n", JAUNE, RESET);
    printf("4 - %sBleu%s\n", BLEU, RESET);
    printf("5 - %sMagenta%s\n", MAGENTA, RESET);
    printf("6 - %sCyan%s\n\n", CYAN, RESET);
}

void afficherCouleur(int couleur) {
    char* couleur_code;
    char* nom;

    if (couleur == 1) {
        couleur_code = ROUGE;
        nom = "R";
    } else if (couleur == 2) {
        couleur_code = VERT;
        nom = "V";
    } else if (couleur == 3) {
        couleur_code = JAUNE;
        nom = "J";
    } else if (couleur == 4) {
        couleur_code = BLEU;
        nom = "B";
    } else if (couleur == 5) {
        couleur_code = MAGENTA;
        nom = "M";
    } else {
        couleur_code = CYAN;
        nom = "C";
    }

    printf("%s%s%s", couleur_code, nom, RESET);
}

void afficherTentatives() {
    int i, j, bien_places, mal_places;

    printf("\n=== HISTORIQUE DES TENTATIVES ===\n");

    for (i = 0; i < nb_tentatives; i++) {
        printf("Tentative %d : ", i + 1);

        for (j = 0; j < LONGUEUR_CODE; j++) {
            afficherCouleur(tentatives[i][j]);
            printf(" ");
        }

        evaluerProposition(tentatives[i], &bien_places, &mal_places);

        printf("  -> %sBien places: %d%s, Mal places: %d\n",
               VERT, bien_places, RESET, mal_places);
    }

    printf("\n");
}

int proposerCode(int proposition[LONGUEUR_CODE]) {
    int i;

    printf("Entrez votre code (4 chiffres entre 1 et 6) :\n");

    for (i = 0; i < LONGUEUR_CODE; i++) {
        printf("Couleur %d : ", i + 1);
        scanf("%d", &proposition[i]);

        if (proposition[i] < 1 || proposition[i] > NB_COULEURS) {
            printf("Couleur invalide ! (1-6)\n");
            return 0;
        }
    }

    return 1;
}

void evaluerProposition(int proposition[LONGUEUR_CODE], int* bien_places, int* mal_places) {
    int i, j;
    int secret_utilise[LONGUEUR_CODE];
    int prop_utilise[LONGUEUR_CODE];

    *bien_places = 0;
    *mal_places = 0;

    for (i = 0; i < LONGUEUR_CODE; i++) {
        secret_utilise[i] = 0;
        prop_utilise[i] = 0;
    }

    for (i = 0; i < LONGUEUR_CODE; i++) {
        if (proposition[i] == code_secret[i]) {
            (*bien_places)++;
            secret_utilise[i] = 1;
            prop_utilise[i] = 1;
        }
    }

    for (i = 0; i < LONGUEUR_CODE; i++) {
        if (!prop_utilise[i]) {
            for (j = 0; j < LONGUEUR_CODE; j++) {
                if (!secret_utilise[j] && proposition[i] == code_secret[j]) {
                    (*mal_places)++;
                    secret_utilise[j] = 1;
                    break;
                }
            }
        }
    }
}

int verifierVictoire(int proposition[LONGUEUR_CODE]) {
    int i;

    for (i = 0; i < LONGUEUR_CODE; i++) {
        if (proposition[i] != code_secret[i]) {
            return 0;
        }
    }

    return 1;
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
    printf("%sVictoires : %d%s\n", VERT, victoires, RESET);
    printf("%sDefaites : %d%s\n", ROUGE, defaites, RESET);
    printf("============================\n");
}