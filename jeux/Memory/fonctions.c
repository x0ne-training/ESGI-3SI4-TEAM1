#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "memory.h"

void shuffle(char arr[], int n) {
    for(int i = n-1; i > 0; i--) {
        int j = rand() % (i+1);
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

void initBoard(Card board[SIZE][SIZE]) {
    char values[SIZE*SIZE];
    for(int i = 0; i < SIZE*SIZE/2; i++) {
        values[2*i] = 'A' + i;
        values[2*i + 1] = 'A' + i;
    }
    srand(time(NULL));
    shuffle(values, SIZE*SIZE);

    int k = 0;
    for(int i = 0; i < SIZE; i++)
        for(int j = 0; j < SIZE; j++) {
            board[i][j].value = values[k++];
            board[i][j].revealed = 0;
        }
}
