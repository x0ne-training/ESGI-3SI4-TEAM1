
typedef struct {
    char nom[20];
    Pion pions[PIONS_PAR_JOUEUR];
} Joueur;

// Fonctions
void initGame(Joueur joueurs[NB_JOUEURS]);
void displayBoard(Joueur joueurs[NB_JOUEURS]);
int lancerDe();
void movePion(Joueur *joueur, int pionIndex, int de);
int isGameOver(Joueur joueurs[NB_JOUEURS]);

#endif
