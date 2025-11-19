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

typedef struct {
    SimsState sims[MAX_SIMS];
    int count;
    int current;
} Game;

void init_game(Game *g);
int create_sim(Game *g, const char *name);
void show_all_sims(const Game *g);
void switch_sim(Game *g, int index);

void eat(SimsState *s);
void sleep_sims(SimsState *s);
void work(SimsState *s);
void fun(SimsState *s);
void next_day(SimsState *s);
void show_stats(const SimsState *s);
int is_dead(const SimsState *s);

int read_int_range(int min, int max);
void clear_input(void);

#endif
