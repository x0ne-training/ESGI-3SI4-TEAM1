#ifndef UNDERCOVER_H
#define UNDERCOVER_H

#define MAX_JOUEURS 20
#define MAX_MOT 50

typedef enum {CITOYEN, UNDERCOVER, MR_WHITE} Role;

typedef struct {
    char nom[20];
    char mot[MAX_MOT];
    Role role;
    int actif; // 1 = en jeu, 0 = éliminé
} Joueur;

// Fonctions principales
void initGame(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);
void distribuerMots(Joueur joueurs[MAX_JOUEURS], int nbJoueurs, char* motCitoyen, char* motUndercover);
void afficherJoueurs(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);
int vote(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);
int checkVictory(Joueur joueurs[MAX_JOUEURS], int nbJoueurs);

#endif

