#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "des.h"

int main(void) {
    srand(time(NULL));

    char c;
    do {
        jouer_manche();
        printf("Rejouer ? (o/n) : ");
        scanf(" %c", &c);
    } while (c == 'o' || c == 'O');

    return 0;
}
