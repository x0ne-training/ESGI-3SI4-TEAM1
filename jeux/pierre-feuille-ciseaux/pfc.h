#ifndef PFC_H
#define PFC_H

#define VERT "\033[1;32m"
#define ROUGE "\033[1;31m"
#define BLEU "\033[1;34m"
#define RESET "\033[0m"

#define PIERRE 1
#define FEUILLE 2
#define CISEAUX 3

#define JOUEUR_GAGNE 1
#define ORDI_GAGNE 2
#define EGALITE 3

#define REJOUER 1
#define NE_PAS_REJOUER 0

extern int victoires_joueur;
extern int victoires_ordi;
extern int egalites;

int choixOrdinateur();
int determinerGagnant(int choix_joueur, int choix_ordi);
void afficherChoix(int choix, char* nom);
void afficherResultat(int resultat);
void afficherScores();
int demanderRejouer();

#endif