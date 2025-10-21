#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "pfc.h"

int main(void) {
    int choix_joueur;
    int choix_ordi;
    int resultat;
    int rejouer = REJOUER;

    srand(time(NULL));

    printf("=== PIERRE-FEUILLE-CISEAUX ===\n\n");

    while (rejouer) {
        printf("\nChoisissez :\n");
        printf("%s1 - Pierre%s\n", BLEU, RESET);
        printf("%s2 - Feuille%s\n", VERT, RESET);
        printf("%s3 - Ciseaux%s\n", ROUGE, RESET);
        printf("\nVotre choix : ");
        scanf("%d", &choix_joueur);

        if (choix_joueur < 1 || choix_joueur > 3) {
            printf("Choix invalide ! Veuillez choisir 1, 2 ou 3.\n");
            continue;
        }

        choix_ordi = choixOrdinateur();

        printf("\n");
        afficherChoix(choix_joueur, "Vous");
        afficherChoix(choix_ordi, "Ordinateur");

        resultat = determinerGagnant(choix_joueur, choix_ordi);
        afficherResultat(resultat);

        afficherScores();
        rejouer = demanderRejouer();
    }

    printf("\nMerci d'avoir joue !\n");

    return 0;
}