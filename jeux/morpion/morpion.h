#ifndef MORPION_H
#define MORPION_H

#define ROUGE "\033[1;31m"
#define BLEU "\033[1;34m"
#define RESET "\033[0m"

#define VICTOIRE 1
#define PAS_VICTOIRE 0
#define GRILLE_PLEINE 1
#define GRILLE_NON_PLEINE 0
#define REJOUER 1
#define NE_PAS_REJOUER 0

extern char grille[3][3];
extern int victoires_x;
extern int victoires_o;
extern int matchs_nuls;

void initialiserGrille();
void afficherGrille();
int verifierVictoire();
int grillePleine();
int demanderRejouer();
void afficherScores();

#endif