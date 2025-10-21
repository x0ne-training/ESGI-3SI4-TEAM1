#ifndef SOLITAIRE_H
#define SOLITAIRE_H

#define ROUGE "\033[1;31m"
#define NOIR "\033[1;30m"
#define RESET "\033[0m"

#define NB_CARTES_PYRAMIDE 28
#define NB_CARTES_TOTAL 52

#define CARTE_RETIREE -1
#define CARTE_VALIDE 1
#define CARTE_INVALIDE 0

#define VICTOIRE 1
#define PAS_VICTOIRE 0

#define REJOUER 1
#define NE_PAS_REJOUER 0

typedef struct {
    int valeur;
    char couleur;
    int retiree;
} Carte;

extern Carte pyramide[7][7];
extern Carte pioche[NB_CARTES_TOTAL - NB_CARTES_PYRAMIDE];
extern int nb_pioche;
extern int victoires;
extern int defaites;

void initialiserJeu();
void melangerCartes(Carte* paquet, int taille);
void afficherPyramide();
void afficherCarte(Carte carte);
int carteAccessible(int ligne, int colonne);
int verifierPaire(Carte c1, Carte c2);
int retirerPaire(int l1, int c1, int l2, int c2);
int retirerRoi(int ligne, int colonne);
int verifierVictoire();
int demanderRejouer();
void afficherScores();

#endif