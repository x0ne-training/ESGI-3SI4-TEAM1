#include <stdio.h>
#include <string.h>
#include "functions.h"

int ask(const char *question, int truth) {
    char answer[10];

    printf("%s (YES/NO) : ", question);
    scanf("%9s", answer);

    // Convertir en majuscules
    for (int i = 0; answer[i]; i++)
        if (answer[i] >= 'a' && answer[i] <= 'z')
            answer[i] -= 32;

   
