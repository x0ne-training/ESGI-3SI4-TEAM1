#ifndef UNDERCOVER_H
#define UNDERCOVER_H

#define MAX_JOUEURS 20
#define MAX_MOT 50

typedef enum { CITOYEN, UNDERCOVER, MR_WHITE } Role;

typedef struct {
    char nom[20];
    Role role;
    char mot[MAX_MOT];   // mot secret
    int actif;           // 1 = encore en jeu, 0 = éliminé
} Joueur;

// Fonctions du jeu
void initGame(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);
void distribuerMots(Joueur joueurs[MAX_JOUEURS], int nbJoueurs, const char* motCitoyen, const char* motUndercover, int hasMrWhite);
void afficherJoueursActifs(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);
int vote(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);
int checkVictory(Joueur joueurs[MAX_JOUEURS], int nbJoueurs, const char* motCitoyen);

#endif
