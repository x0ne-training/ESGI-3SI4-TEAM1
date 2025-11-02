#include <stdio.h>
#include <stdlib.h>
#include "game.h"

int action_success(int skill) {
    return rand() % 100 < skill;
}
