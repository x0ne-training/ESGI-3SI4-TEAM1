#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "labyrinthe.h"

void initLabyrinthe(char lab[SIZE][SIZE], Position *player, Position *exitPos) {
    srand(time(NULL));
    for(int i = 0; i < SIZE; i++)
        for(int j = 0; j < SIZE; j++)
            lab[i][j] = (rand()%4==0) ? '#' : '.';

    player->x = 0; player->y = 0;
    lab[player->x][player->y] = 'P';

    exitPos->x = SIZE-1; exitPos->y = SIZE-1;
    lab[exitPos->x][exitPos->y] = 'S';
}

void afficherLabyrinthe(char lab[SIZE][SIZE], Position player) {
    for(int i = 0; i < SIZE; i++){
        for(int j = 0; j < SIZE; j++){
            if(i == player.x && j == player.y)
                printf("P ");
            else
                printf("%c ", lab[i][j]);
        }
        printf("\n");
    }
}

int deplacer(char lab[SIZE][SIZE], Position *player, char direction){
    int nx = player->x;
    int ny = player->y;
    if(direction=='z') nx--;
    else if(direction=='s') nx++;
    else if(direction=='q') ny--;
    else if(direction=='d') ny++;
    else return 0;

    if(nx>=0 && nx<SIZE && ny>=0 && ny<SIZE && lab[nx][ny]!='#'){
        player->x = nx;
        player->y = ny;
        return 1;
    }
    return 0;
}

int estSortie(Position player, Position exitPos){
    return (player.x == exitPos.x && player.y == exitPos.y);
}
