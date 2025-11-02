#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "game.h"

void initPlayers(Player players[], int numPlayers) {
    for(int i=0;i<numPlayers;i++){
        printf("Entrez le nom du joueur %d: ", i+1);
        scanf("%s", players[i].name);
        players[i].alive = 1;
        // Attribution simple: 1 loup, 1 voyante, 1 chasseur, le reste villageois
        if(i==0) players[i].role = LOUP;
        else if(i==1) players[i].role = VOYANTE;
        else if(i==2) players[i].role = CHASSEUR;
        else players[i].role = VILLAGEOIS;
    }
}

