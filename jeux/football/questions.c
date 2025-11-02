#include <stdio.h>
#include "questions.h"

int askChoice() {
    int choice;
    printf("Choisissez votre action (1=Attaque, 2=Défense, 3=Dribble): ");
    scanf("%d", &choice);
    return choice;
}
