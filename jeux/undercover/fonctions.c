#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "undercover.h"

void initGame(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    for(int i = 0; i < nbJoueurs; i++) {
        printf("Nom du joueur %d : ", i+1);
        scanf("%19s", joueurs[i].nom);
        joueurs[i].actif = 1;
    }
}

void distribuerMots(Joueur joueurs[MAX_JOUEURS], int nbJoueurs, const char* motCitoyen, const char* motUndercover, int hasMrWhite) {
    srand((unsigned int)time(NULL));

    int nbUndercover = 0;
    if(nbJoueurs >= 4 && nbJoueurs <= 6) nbUndercover = 1;
    else if(nbJoueurs >= 7 && nbJoueurs <= 10) nbUndercover = 2;
    else if(nbJoueurs > 10) nbUndercover = 2; // Mr White sera optionnel

    int indices[MAX_JOUEURS];
    for(int i = 0; i < nbJoueurs; i++) indices[i] = i;

    // Mélange des indices
    for(int i = nbJoueurs-1; i > 0; i--) {
        int j = rand() % (i+1);
        int temp = indices[i];
        indices[i] = indices[j];
        indices[j] = temp;
    }

    // Attribution des Undercover
    for(int i = 0; i < nbUndercover; i++) {
        int idx = indices[i];
        joueurs[idx].role = UNDERCOVER;
        strcpy(joueurs[idx].mot, motUndercover);
    }

    // Attribution du Mr White
    int start = nbUndercover;
    if(hasMrWhite) {
        int idx = indices[start++];
        joueurs[idx].role = MR_WHITE;
        strcpy(joueurs[idx].mot, "???");
    }

    // Attribution des citoyens
    for(int i = start; i < nbJoueurs; i++) {
        int idx = indices[i];
        joueurs[idx].role = CITOYEN;
        strcpy(joueurs[idx].mot, motCitoyen);
    }
}

void afficherJoueursActifs(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    printf("\nJoueurs actifs :\n");
    for(int i = 0; i < nbJoueurs; i++) {
        if(joueurs[i].actif)
            printf("%d. %s\n", i+1, joueurs[i].nom);
    }
}

int vote(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    afficherJoueursActifs(joueurs, nbJoueurs);
    int choix;
    printf("Choisissez le joueur à éliminer (numéro) : ");
    scanf("%d", &choix);
    choix--; // tableau commence à 0

    if(choix < 0 || choix >= nbJoueurs || joueurs[choix].actif == 0) {
        printf("Vote invalide.\n");
        return -1;
    }

    joueurs[choix].actif = 0;

    printf("%s est éliminé ! Rôle : ", joueurs[choix].nom);
    switch(joueurs[choix].role) {
        case CITOYEN: printf("Citoyen, mot : %s\n", joueurs[choix].mot); break;
        case UNDERCOVER: printf("Undercover, mot : %s\n", joueurs[choix].mot); break;
        case MR_WHITE: printf("Mr White, mot improvisé : %s\n", joueurs[choix].mot); break;
    }

    return joueurs[choix].role;
}

int checkVictory(Joueur joueurs[MAX_JOUEURS], int nbJoueurs, const char* motCitoyen) {
    int undercoverAlive = 0;
    int citoyensAlive = 0;
    int mrWhiteAlive = 0;

    for(int i = 0; i < nbJoueurs; i++) {
        if(joueurs[i].actif) {
            if(joueurs[i].role == UNDERCOVER) undercoverAlive++;
            else if(joueurs[i].role == CITOYEN) citoyensAlive++;
            else if(joueurs[i].role == MR_WHITE) mrWhiteAlive++;
        }
    }

    if(undercoverAlive == 0 && mrWhiteAlive == 0) return 1; // citoyens gagnent
    if(undercoverAlive >= citoyensAlive) return 2;          // undercover gagne
    return 0;                                               // jeu continue
}

