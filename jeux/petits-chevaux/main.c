#include <stdio.h>
#include "petitschevaux.h"

int main() {
    Joueur joueurs[NB_JOUEURS];
    initGame(joueurs);

    int currentPlayer = 0;

    while(!isGameOver(joueurs)) {
        displayBoard(joueurs);
        printf("\nTour de %s, appuyez sur entree pour lancer le de...\n", joueurs[currentPlayer].nom);
        getchar(); // attendre entree

        int de = lancerDe();
        printf("De: %d\n", de);

        // Pour simplifier, on deplace le premier pion disponible
        for(int i = 0; i < PIONS_PAR_JOUEUR; i++) {
            if(!joueurs[currentPlayer].pions[i].finished) {
                movePion(&joueurs[currentPlayer], i, de);
                break;
            }
        }

        currentPlayer = (currentPlayer + 1) % NB_JOUEURS;
    }

    printf("\nFin du jeu !\n");
    return 0;
}
