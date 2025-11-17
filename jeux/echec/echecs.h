#ifndef ECHECS_H
#define ECHECS_H

#define TAILLE 8

// Codes des pièces
#define VIDE 0
#define PION_B 1
#define TOUR_B 2
#define CAVALIER_B 3
#define FOU_B 4
#define DAME_B 5
#define ROI_B 6
#define PION_N 7
#define TOUR_N 8
#define CAVALIER_N 9
#define FOU_N 10
#define DAME_N 11
#define ROI_N 12

typedef struct {
    int plateau[TAILLE][TAILLE];
    int joueur_courant; // 1 = blancs, 2 = noirs
    int partie_finie;
} Jeu;

// Prototypes des fonctions
void initialiser_plateau(Jeu *jeu);
void afficher_plateau(Jeu *jeu);
int deplacer_piece(Jeu *jeu, int x1, int y1, int x2, int y2);
int est_mouvement_valide(Jeu *jeu, int x1, int y1, int x2, int y2);
int est_piece_du_joueur(int piece, int joueur);
void changer_joueur(Jeu *jeu);
int partie_terminee(Jeu *jeu);

#endif