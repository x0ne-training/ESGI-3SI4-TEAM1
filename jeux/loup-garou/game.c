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

void printStatus(Player players[], int numPlayers) {
    printf("\n=== Statut actuel ===\n");
    for(int i=0;i<numPlayers;i++){
        printf("%s: %s\n", players[i].name, players[i].alive ? "Vivant" : "Mort");
    }
    printf("====================\n");
}

void nightPhase(Player players[], int numPlayers) {
    printf("\n--- Nuit ---\n");
    int victim = rand() % numPlayers;
    while(!players[victim].alive || players[victim].role == LOUP) {
        victim = rand() % numPlayers;
    }
    players[victim].alive = 0;
    printf("Les loups ont attaqué %s !\n", players[victim].name);
}

void dayPhase(Player players[], int numPlayers) {
    printf("\n--- Jour ---\n");
    int vote = rand() % numPlayers;
    while(!players[vote].alive) {
        vote = rand() % numPlayers;
    }
    players[vote].alive = 0;
    printf("Le village a voté pour éliminer %s !\n", players[vote].name);
}

int gameOver(Player players[], int numPlayers) {
    int wolvesAlive=0, villagersAlive=0;
    for(int i=0;i<numPlayers;i++){
        if(players[i].alive){
            if(players[i].role==LOUP) wolvesAlive++;
            else villagersAlive++;
        }
    }
    return wolvesAlive==0 || wolvesAlive>=villagersAlive;
}

void declareWinner(Player players[], int numPlayers) {
    int wolvesAlive=0, villagersAlive=0;
    for(int i=0;i<numPlayers;i++){
        if(players[i].alive){
            if(players[i].role==LOUP) wolvesAlive++;
            else villagersAlive++;
        }
    }
    if(wolvesAlive==0) printf("\nLes villageois ont gagné !\n");
    else printf("\nLes loups-garous ont gagné !\n");
}
