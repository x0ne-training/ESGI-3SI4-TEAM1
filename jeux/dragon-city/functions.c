#include "functions.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

static int clamp(int v, int a, int b) {
    if (v < a) return a;
    if (v > b) return b;
    return v;
}

void init_game(GameState *g) {
    if (!g) return;
    g->count = 0;
    g->gold = 50;   // monnaie de depart
    g->day = 1;
    srand((unsigned)time(NULL));
}

bool add_dragon(GameState *g, const char *name) {
    if (!g || !name) return false;
    if (g->count >= MAX_DRAGONS) return false;
    Dragon *d = &g->dragons[g->count++];
    strncpy(d->name, name, NAME_LEN-1);
    d->name[NAME_LEN-1] = '\0';
    d->level = 1;
    d->health = 100;
    d->hunger = 0;
    d->attack = 10;
    d->alive = true;
    return true;
}

void show_dragon(const Dragon *d) {
    if (!d) return;
    printf("Nom : %s | Niveau : %d | PV : %d | Faim : %d | Att : %d | %s\n",
           d->name, d->level, d->health, d->hunger, d->attack,
           d->alive ? "Vivant" : "Mort");
}

void list_dragons(const GameState *g) {
    if (!g) return;
    if (g->count == 0) {
        printf("Tu n'as aucun dragon pour le moment.\n");
        return;
    }
    for (int i = 0; i < g->count; ++i) {
        printf("[%d] ", i+1);
        show_dragon(&g->dragons[i]);
    }
}

void feed_dragon(GameState *g, int idx) {
    if (!g) return;
    if (idx < 0 || idx >= g->count) {
        printf("Index invalide.\n");
        return;
    }
    Dragon *d = &g->dragons[idx];
    if (!d->alive) {
        printf("%s est mort(e) et ne peut pas etre nourri(e).\n", d->name);
        return;
    }
    const int cost = 5;
    if (g->gold < cost) {
        printf("Pas assez d'or (cout = %d).\n", cost);
        return;
    }
    g->gold -= cost;
    d->hunger = clamp(d->hunger - 30, 0, 100);
    d->health = clamp(d->health + 10, 0, 100);
    printf("%s a ete nourri(e). Faim=%d PV=%d. Or restant: %d\n", d->name, d->hunger, d->health, g->gold);
}

void train_dragon(GameState *g, int idx) {
    if (!g) return;
    if (idx < 0 || idx >= g->count) {
        printf("Index invalide.\n");
        return;
    }
    Dragon *d = &g->dragons[idx];
    if (!d->alive) {
        printf("%s est mort(e) et ne peut pas s'entrainer.\n", d->name);
        return;
    }
    const int cost = 10;
    if (g->gold < cost) {
        printf("Pas assez d'or (cout = %d).\n", cost);
        return;
    }
    g->gold -= cost;
    d->attack += 3;
    d->level += 1;
    d->hunger = clamp(d->hunger + 15, 0, 100);
    d->health = clamp(d->health - 5, 0, 100);
    printf("%s s'est entraine(e). Niveau=%d Att=%d PV=%d Faim=%d. Or restant: %d\n",
           d->name, d->level, d->attack, d->health, d->hunger, g->gold);
    if (d->health <= 0) {
        d->alive = false;
        printf("%s est mort(e) apres l'entrainement...\n", d->name);
    }
}

void pass_day(GameState *g) {
    if (!g) return;
    g->day += 1;
    int income = 0;
    for (int i = 0; i < g->count; ++i) {
        Dragon *d = &g->dragons[i];
        if (!d->alive) continue;
        int produced = 5 + d->level * 2;
        produced = produced * (100 - d->hunger) / 100;
        income += produced;
        d->hunger = clamp(d->hunger + 10, 0, 100);
        if (d->hunger > 80) {
            d->health = clamp(d->health - 10, 0, 100);
            if (d->health == 0) {
                d->alive = false;
                printf("%s est mort(e) de faim.\n", d->name);
            }
        }
    }
    g->gold += income;
    printf("Jour %d : tes dragons ont rapporte %d or. Or total: %d\n", g->day, income, g->gold);
}

void battle_random(GameState *g, int idx) {
    if (!g) return;
    if (idx < 0 || idx >= g->count) {
        printf("Index invalide.\n");
        return;
    }
    Dragon *d = &g->dragons[idx];
    if (!d->alive) {
        printf("%s est mort(e) et ne peut pas combattre.\n", d->name);
        return;
    }

    int monster_level = clamp(d->level + (rand()%3 - 1), 1, d->level + 2);
    int monster_hp = 30 + monster_level * 10;
    int monster_attack = 5 + monster_level * 3;

    printf("Un monstre de niveau %d apparait ! PV=%d Att=%d\n", monster_level, monster_hp, monster_attack);

    while (monster_hp > 0 && d->health > 0) {
        int dmg = d->attack + (rand()%5);
        monster_hp -= dmg;
        printf("%s inflige %d degats. Monstre PV=%d\n", d->name, dmg, monster_hp > 0 ? monster_hp : 0);
        if (monster_hp <= 0) break;
        int mdmg = monster_attack + (rand()%4);
        d->health -= mdmg;
        printf("Monstre inflige %d degats a %s. PV=%d\n", mdmg, d->name, d->health > 0 ? d->health : 0);
    }

    if (d->health > 0) {
        int reward = 10 + monster_level * 5;
        g->gold += reward;
        printf("%s a vaincu le monstre ! Recompense : %d or. Or total : %d\n", d->name, reward, g->gold);
        d->attack += 1;
        if (rand()%100 < 30) {
            d->level += 1;
            printf("%s gagne un niveau ! Niveau %d\n", d->name, d->level);
        }
    } else {
        d->alive = false;
        printf("%s est mort(e) au combat...\n", d->name);
    }
}

int read_int_range(int min, int max) {
    int v;
    while (1) {
        if (scanf("%d", &v) != 1) {
            clear_input();
            printf("Entree invalide, reessaie : ");
            continue;
        }
        clear_input();
        if (v < min || v > max) {
            printf("Choix hors-limites (%d-%d). Reessaie : ", min, max);
            continue;
        }
        return v;
    }
}

void clear_input(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}
