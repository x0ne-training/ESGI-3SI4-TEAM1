#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "solitaire.h"

Carte pyramide[7][7];
Carte pioche[NB_CARTES_TOTAL - NB_CARTES_PYRAMIDE];
int nb_pioche = 0;
int victoires = 0;
int defaites = 0;

void melangerCartes(Carte* paquet, int taille) {
    int i, j;
    Carte temp;

    for (i = taille - 1; i > 0; i--) {
        j = rand() % (i + 1);
        temp = paquet[i];
        paquet[i] = paquet[j];
        paquet[j] = temp;
    }
}

void initialiserJeu() {
    int i, j, index;
    Carte paquet[NB_CARTES_TOTAL];
    char couleurs[] = {'C', 'K', 'P', 'T'};

    index = 0;
    for (i = 0; i < 4; i++) {
        for (j = 1; j <= 13; j++) {
            paquet[index].valeur = j;
            paquet[index].couleur = couleurs[i];
            paquet[index].retiree = 0;
            index++;
        }
    }

    melangerCartes(paquet, NB_CARTES_TOTAL);

    index = 0;
    for (i = 0; i < 7; i++) {
        for (j = 0; j <= i; j++) {
            pyramide[i][j] = paquet[index];
            index++;
        }
    }

    nb_pioche = 0;
    for (i = index; i < NB_CARTES_TOTAL; i++) {
        pioche[nb_pioche] = paquet[i];
        nb_pioche++;
    }
}

void afficherCarte(Carte carte) {
    char* couleur_texte;
    char valeur_char[3];

    if (carte.retiree) {
        printf("   ");
        return;
    }

    if (carte.couleur == 'C' || carte.couleur == 'K') {
        couleur_texte = ROUGE;
    } else {
        couleur_texte = NOIR;
    }

    if (carte.valeur == 1) {
        printf("%sA%c%s", couleur_texte, carte.couleur, RESET);
    } else if (carte.valeur == 11) {
        printf("%sV%c%s", couleur_texte, carte.couleur, RESET);
    } else if (carte.valeur == 12) {
        printf("%sD%c%s", couleur_texte, carte.couleur, RESET);
    } else if (carte.valeur == 13) {
        printf("%sR%c%s", couleur_texte, carte.couleur, RESET);
    } else {
        printf("%s%d%c%s", couleur_texte, carte.valeur, carte.couleur, RESET);
    }
}

void afficherPyramide() {
    int i, j, k;

    printf("\n");
    for (i = 0; i < 7; i++) {
        for (k = 0; k < (7 - i) * 2; k++) {
            printf(" ");
        }
        for (j = 0; j <= i; j++) {
            afficherCarte(pyramide[i][j]);
            printf("  ");
        }
        printf("\n");
    }
    printf("\n");
}

int carteAccessible(int ligne, int colonne) {
    if (pyramide[ligne][colonne].retiree) {
        return CARTE_INVALIDE;
    }

    if (ligne == 6) {
        return CARTE_VALIDE;
    }

    if (pyramide[ligne + 1][colonne].retiree && pyramide[ligne + 1][colonne + 1].retiree) {
        return CARTE_VALIDE;
    }

    return CARTE_INVALIDE;
}

int verifierPaire(Carte c1, Carte c2) {
    int somme;
    somme = c1.valeur + c2.valeur;

    if (somme == 13) {
        return CARTE_VALIDE;
    }

    return CARTE_INVALIDE;
}

int retirerPaire(int l1, int c1, int l2, int c2) {
    if (!carteAccessible(l1, c1) || !carteAccessible(l2, c2)) {
        printf("Une des cartes n'est pas accessible !\n");
        return CARTE_INVALIDE;
    }

    if (!verifierPaire(pyramide[l1][c1], pyramide[l2][c2])) {
        printf("Ces cartes ne font pas 13 !\n");
        return CARTE_INVALIDE;
    }

    pyramide[l1][c1].retiree = 1;
    pyramide[l2][c2].retiree = 1;
    printf("Paire retiree !\n");

    return CARTE_VALIDE;
}

int retirerRoi(int ligne, int colonne) {
    if (!carteAccessible(ligne, colonne)) {
        printf("Cette carte n'est pas accessible !\n");
        return CARTE_INVALIDE;
    }

    if (pyramide[ligne][colonne].valeur != 13) {
        printf("Ce n'est pas un Roi !\n");
        return CARTE_INVALIDE;
    }

    pyramide[ligne][colonne].retiree = 1;
    printf("Roi retire !\n");

    return CARTE_VALIDE;
}

int verifierVictoire() {
    int i, j;

    for (i = 0; i < 7; i++) {
        for (j = 0; j <= i; j++) {
            if (!pyramide[i][j].retiree) {
                return PAS_VICTOIRE;
            }
        }
    }

    return VICTOIRE;
}

int demanderRejouer() {
    char reponse;
    int rejouer = NE_PAS_REJOUER;

    printf("\nVoulez-vous rejouer ? (o/n) : ");
    scanf(" %c", &reponse);

    if (reponse == 'o' || reponse == 'O') {
        rejouer = REJOUER;
    }

    return rejouer;
}

void afficherScores() {
    printf("\n========== SCORES ==========\n");
    printf("Victoires : %d\n", victoires);
    printf("Defaites : %d\n", defaites);
    printf("============================\n");
}