#include <stdio.h>
#include <string.h>
#include "sounds.h"

int ask_sound(const char *sound, const char *expected) {
    char answer[50];

    printf("👉 Quel est ce son ? : \"%s\"\n> ", sound);
    scanf("%49s", answer);

