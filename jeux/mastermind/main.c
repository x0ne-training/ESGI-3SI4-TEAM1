#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mastermind.h"

int main(void) {
    int proposition[LONGUEUR_CODE];
    int bien_places, mal_places;
    int victoire;
    int rejouer = REJOUER;
    int i;

    srand(time(NULL));

    printf("=== MASTERMIND ===\n\n");
    printf("Devinez le code secret de 4 couleurs !\n");
    printf("Vous avez %d tentatives.\n", NB_TENTATIVES_MAX);

    afficherReglesCouleurs();

    while (rejouer) {
        genererCodeSecret();
        nb_tentatives = 0;
        victoire = 0;

        while (nb_tentatives < NB_TENTATIVES_MAX && !victoire) {
            if (nb_tentatives > 0) {
                afficherTentatives();
            }

            printf("Tentative %d/%d\n", nb_tentatives + 1, NB_TENTATIVES_MAX);

            if (!proposerCode(proposition)) {
                continue;
            }

            for (i = 0; i < LONGUEUR_CODE; i++) {
                tentatives[nb_tentatives][i] = proposition[i];
            }

            nb_tentatives++;

            evaluerProposition(proposition, &bien_places, &mal_places);

            printf("\nVotre proposition : ");
            for (i = 0; i < LONGUEUR_CODE; i++) {
                afficherCouleur(proposition[i]);
                printf(" ");
            }
            printf("\n");

            printf("%sBien places : %d%s\n", VERT, bien_places, RESET);
            printf("Mal places : %d\n\n", mal_places);

            victoire = verifierVictoire(proposition);

            if (victoire) {
                printf("%s*** BRAVO ! Vous avez trouve le code secret ! ***%s\n", VERT, RESET);
                printf("Code secret : ");
                for (i = 0; i < LONGUEUR_CODE; i++) {
                    afficherCouleur(code_secret[i]);
                    printf(" ");
                }
                printf("\n");
                victoires++;
            } else if (nb_tentatives >= NB_TENTATIVES_MAX) {
                printf("%s*** PERDU ! ***%s\n", ROUGE, RESET);
                printf("Le code secret etait : ");
                for (i = 0; i < LONGUEUR_CODE; i++) {
                    afficherCouleur(code_secret[i]);
                    printf(" ");
                }
                printf("\n");
                defaites++;
            }
        }

        afficherScores();
        rejouer = demanderRejouer();
    }

    printf("\nMerci d'avoir joue !\n");

    return 0;
}