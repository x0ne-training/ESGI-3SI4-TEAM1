#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "ai.h"


static Point stack_targets[TAILLE*TAILLE];
static int stack_top = 0;

void ai_init(void) {
    srand((unsigned)time(NULL) ^ 0xC0FFEE);
    stack_top = 0;
}

