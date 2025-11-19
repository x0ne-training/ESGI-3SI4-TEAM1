#include <stdio.h>
#include <string.h>
#include "undercover.h"

int main() {
    int nbJoueurs;
    printf("Nombre de joueurs (4-20) : ");
    scanf("%d", &nbJoueurs);
    if(nbJoueurs < 4 || nbJoueurs > MAX_JOUEURS) {
        printf("Nombre de joueurs invalide.\n");
        return 1;
    }

    Joueur joueurs[MAX_JOUEURS];
    initGame(joueurs, nbJoueurs);

    char motCitoyen[50], motUndercover[50];
    printf("Mot des citoyens : ");
    scanf("%49s", motCitoyen);
    printf("Mot des undercovers : ");
    scanf("%49s", motUndercover);

    distribuerMots(joueurs, nbJoueurs, motCitoyen, motUndercover);

    printf("\n=== Chaque joueur connait son rôle en secret ! ===\n");

    int victoire = 0;
    while(victoire == 0) {
        vote(joueurs, nbJoueurs);
        victoire = checkVictory(joueurs, nbJoueurs);
    }

    if(victoire == 1) printf("\nLes citoyens ont gagne !\n");
    else if(victoire == 2) printf("\nLes undercovers ont gagne !\n");
    else if(victoire == 3) printf("\nMr White peut tenter de deviner le mot des citoyens !\n");

    return 0;
}


