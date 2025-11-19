#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "sims.h"

static int clamp(int v, int a, int b) {
    if (v < a) return a;
    if (v > b) return b;
    return v;
}
