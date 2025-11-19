#ifndef SIMS_H
#define SIMS_H

#define MAX_NAME 32
#define MAX_SIMS 10

typedef struct {
    char name[MAX_NAME];
    int hunger;
    int energy;
    int mood;
    int money;
    int day;
    int alive;
} SimsState;
