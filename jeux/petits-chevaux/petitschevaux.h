#ifndef PETITSCHEVAUX_H
#define PETITSCHEVAUX_H

#define NB_JOUEURS 4
#define PIONS_PAR_JOUEUR 4
#define CASES_TOTAL 40

typedef struct {
    int position;   // position sur le plateau (0 = départ)
    int atHome;     // 1 si le pion est à la maison
    int finished;   // 1 si le pion est arrivé
} Pion;
