#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "undercover.h"

// Initialisation des joueurs et tirage des rôles
void initGame(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    srand((unsigned int)time(NULL));
    int nbUndercover = 1;
    int nbMrWhite = 0;

    if(nbJoueurs >= 7 && nbJoueurs <= 10) nbUndercover = 2;
    if(nbJoueurs > 10) { nbUndercover = 2; nbMrWhite = 1; }

    int indices[MAX_JOUEURS];
    for(int i = 0; i < nbJoueurs; i++) indices[i] = i;

    // Mélange indices
    for(int i = nbJoueurs-1; i > 0; i--) {
        int j = rand() % (i+1);
        int temp = indices[i];
        indices[i] = indices[j];
        indices[j] = temp;
    }

    // Saisie noms des joueurs
    for(int i = 0; i < nbJoueurs; i++) {
        printf("Nom du joueur %d : ", i+1);
        scanf("%19s", joueurs[i].nom);
        joueurs[i].actif = 1;
        joueurs[i].role = CITOYEN; // par défaut
        strcpy(joueurs[i].mot, "");
    }

    // Tirage de cartes pour les rôles
    for(int i = 0; i < nbUndercover; i++)
        joueurs[indices[i]].role = UNDERCOVER;
    if(nbMrWhite > 0)
        joueurs[indices[nbUndercover]].role = MR_WHITE;

    printf("\nCartes distribuées ! Chaque joueur connait son rôle en secret.\n");
}

// Distribution des mots selon le rôle
void distribuerMots(Joueur joueurs[MAX_JOUEURS], int nbJoueurs, char* motCitoyen, char* motUndercover) {
    for(int i = 0; i < nbJoueurs; i++) {
        if(joueurs[i].role == CITOYEN) strcpy(joueurs[i].mot, motCitoyen);
        else if(joueurs[i].role == UNDERCOVER) strcpy(joueurs[i].mot, motUndercover);
        else strcpy(joueurs[i].mot, "???"); // Mr White improvisera
    }
}

// Affiche les joueurs encore actifs
void afficherJoueurs(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    printf("\nJoueurs actifs :\n");
    for(int i = 0; i < nbJoueurs; i++) {
        if(joueurs[i].actif)
            printf("%d. %s\n", i+1, joueurs[i].nom);
    }
}

// Vote pour éliminer un joueur
int vote(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    int choix;
    afficherJoueurs(joueurs, nbJoueurs);
    printf("Choisissez le joueur a eliminer (numero) : ");
    scanf("%d", &choix);
    choix--; // tableau commence à 0
    if(choix >= 0 && choix < nbJoueurs && joueurs[choix].actif) {
        joueurs[choix].actif = 0;
        printf("%s est elimine ! Son rôle était : ", joueurs[choix].nom);
        if(joueurs[choix].role == CITOYEN) printf("Citoyen, mot: %s\n", joueurs[choix].mot);
        else if(joueurs[choix].role == UNDERCOVER) printf("Undercover, mot: %s\n", joueurs[choix].mot);
        else printf("Mr White\n");
        return joueurs[choix].role == UNDERCOVER;
    } else {
        printf("Vote invalide.\n");
        return 0;
    }
}

// Vérifie conditions de victoire
int checkVictory(Joueur joueurs[MAX_JOUEURS], int nbJoueurs) {
    int undercoverAlive = 0, citoyensAlive = 0, mrWhiteAlive = 0;
    for(int i = 0; i < nbJoueurs; i++) {
        if(joueurs[i].actif) {
            if(joueurs[i].role == UNDERCOVER) undercoverAlive++;
            else if(joueurs[i].role == CITOYEN) citoyensAlive++;
            else mrWhiteAlive++;
        }
    }
    if(undercoverAlive == 0) return 1; // citoyens gagnent
    if(undercoverAlive >= citoyensAlive) return 2; // undercover gagne
    if(mrWhiteAlive == 1) return 3; // Mr White peut gagner
    return 0; // jeu continue
}


