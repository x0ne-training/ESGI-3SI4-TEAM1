#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <stdbool.h>

#define MAX_DRAGONS 10
#define NAME_LEN 32

typedef struct {
    char name[NAME_LEN];
    int level;
    int health;      // max 100
    int hunger;      // 0 (faim zéro) .. 100 (faim max => malus)
    int attack;
    bool alive;
} Dragon;

