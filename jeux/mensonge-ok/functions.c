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

    int user_says_yes = strcmp(answer, "YES") == 0;

    if (user_says_yes == truth) {
        printf("HA ! Tu as dit la verite !! Tu perds !\n");
        return 0;
    }

    printf("Bien joue... tu mens comme un pro !\n");
    return 1;
}
