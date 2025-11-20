#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "sims.h"

static int clamp(int v, int a, int b) {
    if (v < a) return a;
    if (v > b) return b;
    return v;
}

void init_sims(SimsState *s, const char *name) {
    strncpy(s->name, name, MAX_NAME - 1);
    s->name[MAX_NAME - 1] = '\0';
    s->hunger = 70;
    s->energy = 70;
    s->mood = 70;
    s->money = 100;
    s->day = 1;
    s->alive = 1;
}

void init_game(Game *g) {
    g->count = 0;
    g->current = -1;
}

int create_sim(Game *g, const char *name) {
    if (g->count >= MAX_SIMS) {
        printf("Nombre maximum de Sims atteint.\n");
        return 0;
    }
    init_sims(&g->sims[g->count], name);
    g->count++;
    if (g->current == -1) g->current = 0;
    return 1;
}

void show_all_sims(const Game *g) {
    if (g->count == 0) {
        printf("Aucun Sim cree.\n");
        return;
    }
    for (int i = 0; i < g->count; i++) {
        const SimsState *s = &g->sims[i];
        printf("[%d] %s - Jour %d - Argent %d - %s\n",
               i + 1, s->name, s->day, s->money,
               s->alive ? "Vivant" : "Mort");
    }
}

void switch_sim(Game *g, int index) {
    if (index < 0 || index >= g->count) {
        printf("Index invalide.\n");
        return;
    }
    g->current = index;
    printf("Vous controllez maintenant %s.\n", g->sims[g->current].name);
}

void eat(SimsState *s) {
    if (!s->alive) return;
    const int cost = 15;
    if (s->money < cost) {
        printf("Pas assez d'argent.\n");
        return;
    }
    s->money -= cost;
    s->hunger = clamp(s->hunger + 30, 0, 100);
    printf("%s mange. Faim +30.\n", s->name);
}

void sleep_sims(SimsState *s) {
    if (!s->alive) return;
    s->energy = clamp(s->energy + 50, 0, 100);
    printf("%s dort. Energie +50.\n", s->name);
    next_day(s);
}

void work(SimsState *s) {
    if (!s->alive) return;
    s->money += 40;
    s->energy = clamp(s->energy - 20, 0, 100);
    s->mood = clamp(s->mood - 15, 0, 100);
    s->hunger = clamp(s->hunger - 10, 0, 100);
    printf("%s travaille. Argent +40.\n", s->name);
}

void fun(SimsState *s) {
    if (!s->alive) return;
    const int cost = 10;
    if (s->money < cost) {
        printf("Pas assez d'argent.\n");
        return;
    }
    s->money -= cost;
    s->mood = clamp(s->mood + 25, 0, 100);
    printf("%s se divertit. Humeur +25.\n", s->name);
}

void next_day(SimsState *s) {
    if (!s->alive) return;
    s->day++;
    s->hunger -= 10;
    s->energy -= 5;
    s->mood -= 5;

    if (is_dead(s)) {
        s->alive = 0;
        printf("%s est decede.\n", s->name);
    } else {
        printf("Jour %d pour %s.\n", s->day, s->name);
    }
}

void show_stats(const SimsState *s) {
    printf("\n---- Stats de %s ----\n", s->name);
    printf("Jour:    %d\n", s->day);
    printf("Faim:    %d\n", s->hunger);
    printf("Energie: %d\n", s->energy);
    printf("Humeur:  %d\n", s->mood);
    printf("Argent:  %d\n", s->money);
    printf("Etat:    %s\n", s->alive ? "Vivant" : "Mort");
}

int is_dead(const SimsState *s) {
    return (s->hunger <= 0 || s->energy <= 0 || s->mood <= 0);
}

int read_int_range(int min, int max) {
    int v;
    while (1) {
        if (scanf("%d", &v) != 1) {
            clear_input();
            printf("Entree invalide. ");
            continue;
        }
        clear_input();
        if (v < min || v > max) {
            printf("Choix hors limites (%d-%d). ", min, max);
            continue;
        }
        return v;
    }
}

void clear_input(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}
