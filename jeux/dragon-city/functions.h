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

typedef struct {
    Dragon dragons[MAX_DRAGONS];
    int count;
    int gold;
    int day;
} GameState;

/* initialisation */
void init_game(GameState *g);

/* gestion dragons */
bool add_dragon(GameState *g, const char *name);
void list_dragons(const GameState *g);
void show_dragon(const Dragon *d);

/* actions */
void feed_dragon(GameState *g, int idx);
void train_dragon(GameState *g, int idx);
void pass_day(GameState *g);
void battle_random(GameState *g, int idx);

/* utilitaires */
int read_int_range(int min, int max);
void clear_input(void);

#endif /* FUNCTIONS_H */
