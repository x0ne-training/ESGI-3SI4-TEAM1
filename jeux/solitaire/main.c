#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "solitaire.h"

int main(void) {
    int choix;
    int l1, c1, l2, c2;
    int victoire;
    int rejouer = REJOUER;

    srand(time(NULL));

    printf("=== SOLITAIRE PYRAMIDE ===\n\n");
    printf("Regles : Retirez des paires de cartes qui font 13\n");
    printf("As=1, Valet=11, Dame=12, Roi=13\n");
    printf("Les Rois se retirent seuls\n\n");

    while (rejouer) {
        initialiserJeu();
        victoire = PAS_VICTOIRE;

        while (!victoire) {
            afficherPyramide();

            printf("1 - Retirer une paire\n");
            printf("2 - Retirer un Roi\n");
            printf("3 - Abandonner\n");
            printf("\nVotre choix : ");
            scanf("%d", &choix);

            if (choix == 1) {
                printf("\nPremiere carte - Ligne (1-7) : ");
                scanf("%d", &l1);
                printf("Premiere carte - Colonne (1-%d) : ", l1);
                scanf("%d", &c1);

                printf("Deuxieme carte - Ligne (1-7) : ");
                scanf("%d", &l2);
                printf("Deuxieme carte - Colonne (1-%d) : ", l2);
                scanf("%d", &c2);

                l1--;
                c1--;
                l2--;
                c2--;

                if (l1 < 0 || l1 > 6 || c1 < 0 || c1 > l1 ||
                    l2 < 0 || l2 > 6 || c2 < 0 || c2 > l2) {
                    printf("Positions invalides !\n");
                    continue;
                }

                retirerPaire(l1, c1, l2, c2);

            } else if (choix == 2) {
                printf("\nRoi - Ligne (1-7) : ");
                scanf("%d", &l1);
                printf("Roi - Colonne (1-%d) : ", l1);
                scanf("%d", &c1);

                l1--;
                c1--;

                if (l1 < 0 || l1 > 6 || c1 < 0 || c1 > l1) {
                    printf("Position invalide !\n");
                    continue;
                }

                retirerRoi(l1, c1);

            } else if (choix == 3) {
                printf("\nVous abandonnez...\n");
                defaites++;
                break;
            } else {
                printf("Choix invalide !\n");
                continue;
            }

            victoire = verifierVictoire();

            if (victoire) {
                afficherPyramide();
                printf("\n*** BRAVO ! Vous avez gagne ! ***\n");
                victoires++;
            }
        }

        afficherScores();
        rejouer = demanderRejouer();
    }

    printf("\nMerci d'avoir joue !\n");

    return 0;
}