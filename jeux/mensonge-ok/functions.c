#include <stdio.h>
#include <string.h>
#include "functions.h"

int ask(const char *question, int truth) {
    char answer[10];

    printf("%s (YES/NO) : ", question);
    scanf("%9s", answer);

    