#ifndef MEMORY_H
#define MEMORY_H

#define SIZE 4 // 4x4 cartes

typedef struct {
    char value;
    int revealed;
} Card;

void initBoard(Card board[SIZE][SIZE]);
void displayBoard(Card board[SIZE][SIZE]);
int isGameOver(Card board[SIZE][SIZE]);
void playGame(Card board[SIZE][SIZE]);

#endif

