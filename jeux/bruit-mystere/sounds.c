#include <stdio.h>
#include <string.h>
#include "sounds.h"

int ask_sound(const char *sound, const char *expected) {
    char answer[50];

    printf("Quel est ce son ? : \"%s\"\n> ", sound);
    scanf("%49s", answer);

    // Convertir en minuscules
    for (int i = 0; answer[i]; i++)
        if (answer[i] >= 'A' && answer[i] <= 'Z')
            answer[i] += 32;

    if (strcmp(answer, expected) == 0) {
        printf("✔ Correct !\n\n");
        return 1;
    }

    printf("Faux ! C'était : %s\n\n", expected);
    return 0;
}
