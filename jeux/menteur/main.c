#include <stdio.h>
#include "game.h"
#include "score.h"

int main() {
    init_vies();
    printf("Bienvenue dans le jeu du Menteur !\n");
    printf("Chaque joueur commence avec 3 vies.\n");

    while(!fin_jeu()) {
        tour_joueur();
        if(fin_jeu()) break;
        tour_ordi();
    }

    if(vies_joueur() <= 0)
        printf("Vous avez perdu ! L'ordinateur gagne.\n");
    else
        printf("Bravo ! Vous gagnez !\n");

    return 0;
}
