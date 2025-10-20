#include <stdio.h>
#include "puissance4.h"

int main(void) {
    int colonne;
    char joueur;
    int victoire;
    int rejouer = REJOUER;

    printf("=== JEU DE PUISSANCE 4 ===\n\n");

    while (rejouer) {
        joueur = 'R';
        victoire = PAS_VICTOIRE;
        initialiserGrille();

        while (!victoire && !grillePleine()) {
            afficherGrille();

            printf("\nJoueur %s%c%s, choisissez une colonne (1-7) : ",
                   joueur == 'R' ? ROUGE : JAUNE,
                   joueur == 'R' ? 'R' : 'J',
                   RESET);
            scanf("%d", &colonne);

            colonne--;

            if (!colonneValide(colonne)) {
                printf("Colonne invalide ou pleine !\n");
                continue;
            }

            placerJeton(colonne, joueur);

            victoire = verifierVictoire();

            if (victoire) {
                afficherGrille();
                if (joueur == 'R') {
                    printf("\n%sJoueur Rouge a gagne !%s\n", ROUGE, RESET);
                    victoires_rouge++;
                } else {
                    printf("\n%sJoueur Jaune a gagne !%s\n", JAUNE, RESET);
                    victoires_jaune++;
                }
            } else if (grillePleine()) {
                afficherGrille();
                printf("\nMatch nul !\n");
                matchs_nuls++;
            } else {
                joueur = (joueur == 'R') ? 'J' : 'R';
            }
        }

        afficherScores();
        rejouer = demanderRejouer();
    }

    printf("\nMerci d'avoir joue !\n");

    return 0;
}