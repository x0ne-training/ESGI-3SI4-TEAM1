#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "pfc.h"

int victoires_joueur = 0;
int victoires_ordi = 0;
int egalites = 0;

int choixOrdinateur() {
    int choix;
    choix = (rand() % 3) + 1;
    return choix;
}

int determinerGagnant(int choix_joueur, int choix_ordi) {
    int resultat;

    if (choix_joueur == choix_ordi) {
        resultat = EGALITE;
        return resultat;
    }

    if ((choix_joueur == PIERRE && choix_ordi == CISEAUX) ||
        (choix_joueur == FEUILLE && choix_ordi == PIERRE) ||
        (choix_joueur == CISEAUX && choix_ordi == FEUILLE)) {
        resultat = JOUEUR_GAGNE;
        return resultat;
    }

    resultat = ORDI_GAGNE;
    return resultat;
}

void afficherChoix(int choix, char* nom) {
    printf("%s a choisi : ", nom);

    if (choix == PIERRE) {
        printf("%sPierre%s", BLEU, RESET);
    } else if (choix == FEUILLE) {
        printf("%sFeuille%s", VERT, RESET);
    } else if (choix == CISEAUX) {
        printf("%sCiseaux%s", ROUGE, RESET);
    }

    printf("\n");
}

void afficherResultat(int resultat) {
    printf("\n");

    if (resultat == JOUEUR_GAGNE) {
        printf("%sVous avez gagne !%s\n", VERT, RESET);
        victoires_joueur++;
    } else if (resultat == ORDI_GAGNE) {
        printf("%sL'ordinateur a gagne !%s\n", ROUGE, RESET);
        victoires_ordi++;
    } else {
        printf("%sEgalite !%s\n", BLEU, RESET);
        egalites++;
    }
}

void afficherScores() {
    printf("\n========== SCORES ==========\n");
    printf("%sVous : %d victoires%s\n", VERT, victoires_joueur, RESET);
    printf("%sOrdinateur : %d victoires%s\n", ROUGE, victoires_ordi, RESET);
    printf("Egalites : %d\n", egalites);
    printf("============================\n");
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