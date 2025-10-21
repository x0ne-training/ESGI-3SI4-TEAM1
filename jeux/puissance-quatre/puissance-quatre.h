#ifndef PUISSANCE4_H
#define PUISSANCE4_H

#define ROUGE "\033[1;31m" // pour afficher le texte en rouge
#define JAUNE "\033[1;33m" // pour afficher le texte en jaune
#define RESET "\033[0m" // pour afficher le texte en couleur normale g

#define LIGNES 6
#define COLONNES 7

#define VICTOIRE 1
#define PAS_VICTOIRE 0
#define GRILLE_PLEINE 1
#define GRILLE_NON_PLEINE 0
#define COLONNE_VALIDE 1
#define COLONNE_INVALIDE 0
#define REJOUER 1
#define NE_PAS_REJOUER 0

extern char grille[LIGNES][COLONNES];
extern int victoires_rouge;
extern int victoires_jaune;
extern int matchs_nuls;

void initialiserGrille();
void afficherGrille();
int verifierVictoire();
int grillePleine();
int colonneValide(int colonne);
int placerJeton(int colonne, char joueur);
int demanderRejouer();
void afficherScores();

#endif