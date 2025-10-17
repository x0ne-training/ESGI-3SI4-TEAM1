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

void ai_place_ships(Case p[TAILLE][TAILLE]) {
    for (int i=0;i<NB_BATEAUX;i++) {
        if (!placer_bateau_alea(p, BATEAUX[i].taille)) {
            // si placement échoue improbable, réinit tout et recommence
            init_plateau(p);
            i = -1;
            continue;
        }
    }
}

Point ai_choose_shot(Case opponent_view[TAILLE][TAILLE]) {
    // si on a des cibles en stack (après toucher), utiliser les voisins
    while (stack_top > 0) {
        Point t = stack_targets[--stack_top];
        if (coord_valide(t.x,t.y) && opponent_view[t.x][t.y]==VIDE) return t;
    }
    // sinon tirer aléatoirement en cherchant cases non testées
    int tries = 0;
    while (tries++ < 10000) {
        int x = rand()%TAILLE;
        int y = rand()%TAILLE;
        if (opponent_view[x][y] == VIDE) {
            Point p = {x,y};
            return p;
        }
    }
    // fallback: trouver la première case vide
    for (int i=0;i<TAILLE;i++) for (int j=0;j<TAILLE;j++)
            if (opponent_view[i][j]==VIDE) return (Point){i,j};
    return (Point){0,0};
}

void ai_report_result(Point last, bool hit) {
    if (hit) {
        // empiler voisins non testés (simple stratégie)
        Point neigh[4] = {{last.x+1,last.y},{last.x-1,last.y},{last.x,last.y+1},{last.x,last.y-1}};
        for (int k=0;k<4;k++) {
            Point np = neigh[k];
            if (coord_valide(np.x,np.y)) {
                if (stack_top < TAILLE*TAILLE) stack_targets[stack_top++] = np;
            }
        }
    }
}