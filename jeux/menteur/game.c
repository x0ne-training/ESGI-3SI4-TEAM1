#include <stdio.h>
#include <stdlib.h>
#include "game.h"
#include "utils.h"
#include "score.h"

void tour_joueur() {
    printf("\n--- Tour du joueur ---\n");
    int carte = poser_carte(1);
    int annonce = annoncer_carte(1);
    int mensonge = verifier_mentir(carte, annonce);

    if(mensonge) {
        printf("Vous avez menti ! L'ordinateur dit menteur !\n");
        perdre_vie_joueur();
    } else {
        printf("Annonce correcte ! Vous gardez vos vies.\n");
    }
}

void tour_ordi() {
    printf("\n--- Tour de l'ordinateur ---\n");
    int carte = poser_carte(2);
    int annonce = annoncer_carte(2);
    printf("L'ordinateur annonce : %s\n", nom_carte(annonce));

    int mensonge = verifier_mentir(carte, annonce);
    int joueur_intervient = hasard(0,1);

    if(joueur_intervient) {
        if(mensonge) {
            printf("Vous avez dit menteur et aviez raison ! L'ordinateur perd une vie.\n");
            perdre_vie_ordi();
        } else {
            printf("Vous avez dit menteur mais l'ordinateur disait vrai ! Vous perdez une vie.\n");
            perdre_vie_joueur();
        }
    } else {
        printf("Vous laissez passer.\n");
    }
}

int poser_carte(int joueur) {
    if(joueur == 1) {
        printf("Choisissez une carte (1-13) : ");
        return lire_entier();
    } else {
        return hasard(1,13);
    }
}

int annoncer_carte(int joueur) {
    if(joueur == 1) {
        printf("Annoncez la carte que vous posez (1-13) : ");
        return lire_entier();
    } else {
        return hasard(1,13);
    }
}

int verifier_mentir(int vrai, int annonce) {
    return vrai != annonce;
}
