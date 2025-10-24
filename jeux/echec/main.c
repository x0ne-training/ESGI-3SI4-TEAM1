#include <stdio.h>
#include <stdlib.h>
#include "echecs.h"

int main() {
    Jeu jeu;
    char dep[3], arr[3];
    int x1, y1, x2, y2;

    initialiser_plateau(&jeu);

    printf("=== JEU D'ECHECS ===\n");
    printf("Format de saisie: e2 e4 (colonne+ligne espace colonne+ligne)\n");

    while (!partie_terminee(&jeu)) {
        afficher_plateau(&jeu);

        printf("\nVotre coup (ex: e2 e4) ou 'q' pour quitter: ");
        if (scanf("%s", dep) != 1) break;

        if (dep[0] == 'q') {
            printf("Partie abandonnée.\n");
            break;
        }

        if (scanf("%s", arr) != 1) break;

        // Conversion notation échecs en indices
        y1 = dep[0] - 'a';
        x1 = 8 - (dep[1] - '0');
        y2 = arr[0] - 'a';
        x2 = 8 - (arr[1] - '0');

        if (deplacer_piece(&jeu, x1, y1, x2, y2)) {
            changer_joueur(&jeu);
        } else {
            printf("Coup invalide! Réessayez.\n");
        }
    }

    if (partie_terminee(&jeu)) {
        afficher_plateau(&jeu);
        printf("\n=== PARTIE TERMINEE ===\n");
        printf("Les %s ont gagné!\n", jeu.joueur_courant == 2 ? "Blancs" : "Noirs");
    }

    return 0;
}