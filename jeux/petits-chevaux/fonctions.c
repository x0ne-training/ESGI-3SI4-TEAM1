
int isGameOver(Joueur joueurs[NB_JOUEURS]) {
    for(int i = 0; i < NB_JOUEURS; i++) {
        for(int j = 0; j < PIONS_PAR_JOUEUR; j++) {
            if(!joueurs[i].pions[j].finished)
                return 0;
        }
    }
    return 1;
}
