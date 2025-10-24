#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "memory.h"


void displayBoard(Card board[SIZE][SIZE]) {
    printf("\n   ");
    for(int j = 0; j < SIZE; j++) printf("  %d   ", j);
    printf("\n");

    for(int i = 0; i < SIZE; i++) {
        printf("  +");
        for(int j = 0; j < SIZE; j++) printf("-----+");
        printf("\n");

        printf("%d |", i);
        for(int j = 0; j < SIZE; j++) {
            if(board[i][j].revealed)
                printf("  %c  |", board[i][j].value);
            else
                printf("  *  |");
        }
        printf("\n");
    }

    printf("  +");
    for(int j = 0; j < SIZE; j++) printf("-----+");
    printf("\n\n");
}

int isGameOver(Card board[SIZE][SIZE]) {
    for(int i = 0; i < SIZE; i++)
        for(int j = 0; j < SIZE; j++)
            if(board[i][j].revealed == 0)
                return 0;
    return 1;
}

void playGame(Card board[SIZE][SIZE]) {
    int x1, y1, x2, y2;

    while(!isGameOver(board)) {
        displayBoard(board);

        printf("Choisissez la premiere carte (ligne colonne) : ");
        scanf("%d %d", &x1, &y1);
        printf("Choisissez la deuxieme carte (ligne colonne) : ");
        scanf("%d %d", &x2, &y2);

        if(x1 == x2 && y1 == y2) {
            printf("Vous devez choisir deux cartes differentes!\n");
            continue;
        }

        board[x1][y1].revealed = 1;
        board[x2][y2].revealed = 1;

        displayBoard(board);

        if(board[x1][y1].value == board[x2][y2].value) {
            printf("Bravo! C'est une paire!\n");
        } else {
            printf("Pas de chance.\n");
            board[x1][y1].revealed = 0;
            board[x2][y2].revealed = 0;
        }

        printf("\n");
    }

    printf("Felicitation! Vous avez trouve toutes les paires!\n");
}
