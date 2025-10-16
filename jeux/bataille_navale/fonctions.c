#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "fonctions.h"


const BateauInfo BATEAUX[NB_BATEAUX] = {
        {5, "Porte-avions"},
        {4, "Croiseur"},
        {3, "Contre-torp"},
        {3, "Sous-marin"},
        {2, "Torpilleur"}
};

void init_plateau(Case p[TAILLE][TAILLE]) {
    for (int i=0;i<TAILLE;i++)
        for (int j=0;j<TAILLE;j++)
            p[i][j] = VIDE;
}

void afficher_plateau(Case p[TAILLE][TAILLE], bool cacher) {
    printf("   ");
    for (int c=0;c<TAILLE;c++) printf("%d ", c);
    printf("\n");
    for (int i=0;i<TAILLE;i++) {
        printf("%2d ", i);
        for (int j=0;j<TAILLE;j++) {
            Case v = p[i][j];
            char ch = '.';
            if (v == VIDE) ch = '.';
            else if (v == BATEAU) ch = cacher ? '.' : 'B';
            else if (v == MANQUÉ) ch = 'o';
            else if (v == TOUCHÉ) ch = 'X';
            else if (v == COULÉ) ch = '#';
            printf("%c ", ch);
        }
        printf("\n");
    }
}


bool coord_valide(int x, int y) {
    return x>=0 && x<TAILLE && y>=0 && y<TAILLE;
}

bool peut_placer(Case p[TAILLE][TAILLE], int taille, int x, int y, char dir) {
    int dx = 0, dy = 0;
    if (dir == 'h' || dir == 'H') dx = -1;
    else if (dir == 'b' || dir == 'B') dx = 1;
    else if (dir == 'g' || dir == 'G') dy = -1;
    else if (dir == 'd' || dir == 'D') dy = 1;
    else return false;

    for (int k=0;k<taille;k++) {
        int nx = x + dx*k;
        int ny = y + dy*k;
        if (!coord_valide(nx, ny) || p[nx][ny] != VIDE) return false;
        // vérifier autour pour éviter contact
        for (int ix = nx-1; ix <= nx+1; ix++)
            for (int iy = ny-1; iy <= ny+1; iy++)
                if (coord_valide(ix,iy) && p[ix][iy] == BATEAU && !(ix==nx && iy==ny))
                    return false;
    }
    return true;
}