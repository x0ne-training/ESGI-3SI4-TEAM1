#include <stdio.h>
#include "morpion.h"

int main(void) {
    int ligne, colonne;
    char joueur;
    int victoire;
    int rejouer = REJOUER;

    printf("=== JEU DE MORPION ===\n\n");

    while (rejouer) {
        joueur = 'X';
        victoire = PAS_VICTOIRE;
        initialiserGrille();

        while (!victoire && !grillePleine()) {
            afficherGrille();

            printf("\nJoueur %c, entrez ligne (1-3) : ", joueur);
            scanf("%d", &ligne);
            printf("Entrez colonne (1-3) : ");
            scanf("%d", &colonne);

            ligne--;
            colonne--;

            if (ligne < 0 || ligne > 2 || colonne < 0 || colonne > 2) {
                printf("Position invalide !\n");
                continue;
            }

            if (grille[ligne][colonne] != ' ') {
                printf("Case occupee !\n");
                continue;
            }

            grille[ligne][colonne] = joueur;

            victoire = verifierVictoire();

            if (victoire) {
                afficherGrille();
                if (joueur == 'X') {
                    printf("\n%sJoueur X a gagne !%s\n", ROUGE, RESET);
                    victoires_x++;
                } else {
                    printf("\n%sJoueur O a gagne !%s\n", BLEU, RESET);
                    victoires_o++;
                }
            } else if (grillePleine()) {
                afficherGrille();
                printf("\nMatch nul !\n");
                matchs_nuls++;
            } else {
                joueur = (joueur == 'X') ? 'O' : 'X';
            }
        }

        afficherScores();
        rejouer = demanderRejouer();
    }

    printf("\nMerci d'avoir joue !\n");

    return 0;
}