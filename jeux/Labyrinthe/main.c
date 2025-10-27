#include <stdio.h>
#include "labyrinthe.h"

int main(){
    char lab[SIZE][SIZE];
    Position player, exitPos;

    initLabyrinthe(lab, &player, &exitPos);

    printf("Bienvenue dans le Labyrinthe Numerique !\n");
    printf("Deplacements : z=haut, s=bas, q=gauche, d=droite\n");

    while(!estSortie(player, exitPos)){
        afficherLabyrinthe(lab, player);
        char move;
        printf("Deplacement : ");
        scanf(" %c", &move);
        if(!deplacer(lab, &player, move))
            printf("Deplacement impossible !\n");
    }

    printf("Felicitation ! Vous avez trouve la sortie !\n");
    return 0;
}
