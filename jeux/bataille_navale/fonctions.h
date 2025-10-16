#ifndef FONCTIONS_H
#define FONCTIONS_H

#include <stdbool.h>

#define TAILLE 10
#define NB_BATEAUX 5

typedef enum {
    VIDE = 0,
    BATEAU,
    TOUCHÉ,
    MANQUÉ,
    COULÉ
} Case;

typedef struct {
    int x, y;
} Point;

typedef struct {
    int taille;
    char nom[16];
} BateauInfo;

extern const BateauInfo BATEAUX[NB_BATEAUX];

void init_plateau(Case p[TAILLE][TAILLE]);
void afficher_plateau(Case p[TAILLE][TAILLE], bool cacher); // cacher=true pour ne pas montrer les bateaux
bool placer_bateau_alea(Case p[TAILLE][TAILLE], int taille);
bool place_bateau_user(Case p[TAILLE][TAILLE], int taille, int x, int y, char dir);
bool tous_coulés(Case p[TAILLE][TAILLE]);
bool tirer(Case cible[TAILLE][TAILLE], Case attaquant[TAILLE][TAILLE], int x, int y);
int compte_cases_bateau(Case p[TAILLE][TAILLE], int x, int y);
void maj_coules(Case p[TAILLE][TAILLE]);
bool coord_valide(int x, int y);
void clear_input_buffer(void);




#endif
