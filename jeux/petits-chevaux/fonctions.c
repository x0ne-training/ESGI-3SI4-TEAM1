
int lancerDe() {
    return rand() % 6 + 1;
}

void movePion(Joueur *joueur, int pionIndex, int de) {
    Pion *pion = &joueur->pions[pionIndex];

    if(pion->finished) {
        printf("Ce pion est deja arrive.\n");
        return;
    }

    if(pion->atHome) {
        if(de == 6) {
            pion->position = 1;
            pion->atHome = 0;
            printf("%s sort un pion de la maison !\n", joueur->nom);
        } else {
            printf("%s ne peut pas sortir le pion (besoin de 6).\n", joueur->nom);
        }
        return;
    }

    pion->position += de;
    if(pion->position >= CASES_TOTAL) {
        pion->position = CASES_TOTAL;
        pion->finished = 1;
        printf("%s a amene un pion a la fin !\n", joueur->nom);
    } else {
        printf("%s deplace un pion de %d cases.\n", joueur->nom, de);
    }
}

int isGameOver(Joueur joueurs[NB_JOUEURS]) {
    for(int i = 0; i < NB_JOUEURS; i++) {
        for(int j = 0; j < PIONS_PAR_JOUEUR; j++) {
            if(!joueurs[i].pions[j].finished)
                return 0;
        }
    }
    return 1;
}
