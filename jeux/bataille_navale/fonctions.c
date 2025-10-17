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

bool place_bateau_user(Case p[TAILLE][TAILLE], int taille, int x, int y, char dir) {
    if (!peut_placer(p, taille, x, y, dir)) return false;
    int dx = 0, dy = 0;
    if (dir == 'h' || dir == 'H') dx = -1;
    else if (dir == 'b' || dir == 'B') dx = 1;
    else if (dir == 'g' || dir == 'G') dy = -1;
    else if (dir == 'd' || dir == 'D') dy = 1;

    for (int k=0;k<taille;k++) {
        int nx = x + dx*k;
        int ny = y + dy*k;
        p[nx][ny] = BATEAU;
    }
    return true;
}

bool placer_bateau_alea(Case p[TAILLE][TAILLE], int taille) {
    int tries = 0;
    while (tries++ < 2000) {
        int x = rand()%TAILLE;
        int y = rand()%TAILLE;
        char dirs[4] = {'h','b','g','d'};
        char dir = dirs[rand()%4];
        if (peut_placer(p, taille, x, y, dir)) {
            place_bateau_user(p, taille, x, y, dir);
            return true;
        }
    }
    return false;
}

bool tirer(Case cible[TAILLE][TAILLE], Case attaquant[TAILLE][TAILLE], int x, int y) {
    if (!coord_valide(x,y)) return false;
    Case v = cible[x][y];
    if (v == BATEAU) {
        cible[x][y] = TOUCHÉ;
        attaquant[x][y] = TOUCHÉ;
        maj_coules(cible);
        return true;
    } else if (v == VIDE) {
        cible[x][y] = MANQUÉ;
        attaquant[x][y] = MANQUÉ;
        return false;
    } else {
        // case déjà tirée
        return false;
    }
}

int compte_cases_bateau(Case p[TAILLE][TAILLE], int x, int y) {
    // recherche BFS de la composante de bateau (BATEAU ou TOUCHÉ)
    bool vus[TAILLE][TAILLE] = {0};
    Case cible = p[x][y];
    if (!(cible==BATEAU || cible==TOUCHÉ)) return 0;
    int qx[TAILLE*TAILLE], qy[TAILLE*TAILLE];
    int qh=0, qt=0;
    qx[qt]=x; qy[qt]=y; qt++; vus[x][y]=true;
    int cnt = 0;
    while (qh<qt) {
        int cx = qx[qh], cy = qy[qh]; qh++;
        if (p[cx][cy]==BATEAU || p[cx][cy]==TOUCHÉ) cnt++;
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int d=0;d<4;d++) {
            int nx = cx + dirs[d][0];
            int ny = cy + dirs[d][1];
            if (coord_valide(nx,ny) && !vus[nx][ny] && (p[nx][ny]==BATEAU || p[nx][ny]==TOUCHÉ)) {
                vus[nx][ny] = true;
                qx[qt]=nx; qy[qt]=ny; qt++;
            }
        }
    }
    return cnt;
}

void maj_coules(Case p[TAILLE][TAILLE]) {
    // pour chaque case TOUCHÉ, si sa composante n'a plus de BATEAU (tous sont TOUCHÉ), on met COULÉ
    bool vus[TAILLE][TAILLE] = {0};
    for (int i=0;i<TAILLE;i++) for (int j=0;j<TAILLE;j++) {
            if (!vus[i][j] && (p[i][j]==BATEAU || p[i][j]==TOUCHÉ)) {
                // recherche composante
                int qx[TAILLE*TAILLE], qy[TAILLE*TAILLE];
                int qh=0, qt=0;
                qx[qt]=i; qy[qt]=j; qt++; vus[i][j]=true;
                bool anyBateau=false;
                while (qh<qt) {
                    int cx = qx[qh], cy = qy[qh]; qh++;
                    if (p[cx][cy] == BATEAU) anyBateau = true;
                    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
                    for (int d=0;d<4;d++) {
                        int nx = cx + dirs[d][0];
                        int ny = cy + dirs[d][1];
                        if (coord_valide(nx,ny) && !vus[nx][ny] && (p[nx][ny]==BATEAU || p[nx][ny]==TOUCHÉ)) {
                            vus[nx][ny] = true;
                            qx[qt]=nx; qy[qt]=ny; qt++;
                        }
                    }
                }
                if (!anyBateau) {
                    // couler la composante: marquer COULÉ toutes les cases TOUCHÉ/ BATEAU (devra être TOUCHÉ toute si coulé)
                    for (int k=0;k<qt;k++) {
                        int cx = qx[k], cy = qy[k];
                        if (p[cx][cy] == TOUCHÉ || p[cx][cy] == BATEAU) p[cx][cy] = COULÉ;
                    }
                }
            }
        }
}

bool tous_coulés(Case p[TAILLE][TAILLE]) {
    for (int i=0;i<TAILLE;i++) for (int j=0;j<TAILLE;j++)
            if (p[i][j] == BATEAU) return false;
    return true;
}

void clear_input_buffer(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}


