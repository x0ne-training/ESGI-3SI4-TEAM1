#include <stdio.h>
#include <string.h>
#include "undercover.h"

int main() {
    int nbJoueurs, hasMrWhite;
    char motCitoyen[MAX_MOT], motUndercover[MAX_MOT];

    printf("Nombre de joueurs (min 4, max 20) : ");
    scanf("%d", &nbJoueurs);
    if(nbJoueurs < 4 || nbJoueurs > MAX_JOUEURS) {
        printf("Nombre de joueurs invalide.\n");
        return 1;
    }

    printf("Mot des citoyens : ");
    scanf("%s", motCitoyen);
    printf("Mot des Undercover : ");
    scanf("%s", motUndercover);

    printf("Ajouter Mr White ? (1 = oui, 0 = non) : ");
    scanf("%d", &hasMrWhite);

    Joueur joueurs[MAX_JOUEURS];
    initGame(joueurs, nbJoueurs);
    distribuerMots(joueurs, nbJoueurs, motCitoyen, motUndercover, hasMrWhite);

    printf("\n--- Début du jeu Undercover ---\n");

    int victoire = 0;
    while(victoire == 0) {
        int roleElimine = vote(joueurs, nbJoueurs);
        if(roleElimine == -1) continue;
        victoire = checkVictory(joueurs, nbJoueurs, motCitoyen);
    }

    if(victoire == 1) printf("\nLes Citoyens ont gagné !\n");
    else if(victoire == 2) printf("\nL'Undercover a gagné !\n");

    return 0;
}

