#ifndef MASTERMIND_H
#define MASTERMIND_H

#define ROUGE "\033[1;31m"
#define VERT "\033[1;32m"
#define JAUNE "\033[1;33m"
#define BLEU "\033[1;34m"
#define MAGENTA "\033[1;35m"
#define CYAN "\033[1;36m"
#define BLANC "\033[1;37m"
#define RESET "\033[0m"

#define NB_COULEURS 6
#define LONGUEUR_CODE 4
#define NB_TENTATIVES_MAX 10

#define VICTOIRE 1
#define DEFAITE 0
#define EN_COURS 2

#define REJOUER 1
#define NE_PAS_REJOUER 0

extern int code_secret[LONGUEUR_CODE];
extern int tentatives[NB_TENTATIVES_MAX][LONGUEUR_CODE];
extern int nb_tentatives;
extern int victoires;
extern int defaites;

void genererCodeSecret();
void afficherReglesCouleurs();
void afficherTentatives();
void afficherCouleur(int couleur);
int proposerCode(int proposition[LONGUEUR_CODE]);
void evaluerProposition(int proposition[LONGUEUR_CODE], int* bien_places, int* mal_places);
int verifierVictoire(int proposition[LONGUEUR_CODE]);
int demanderRejouer();
void afficherScores();

#endif