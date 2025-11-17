#ifndef QUESTIONS_H
#define QUESTIONS_H

#include "game.h"

typedef struct {
    char question[256];
    char optionA[128];
    char optionB[128];
    int effectsA[4];
    int effectsB[4];
} Question;

Question getRandomQuestion();

#endif
