#ifndef LE_MILLION_H
#define LE_MILLION_H

#define MAX_QUESTIONS 10

typedef struct {
    char question[256];
    char reponses[4][128];
    char bonne_reponse;
    int gain;
} Question;
} Question;

void afficher_question(Question q, int numero);
char demander_reponse();
int verifier_reponse(Question q, char rep);

#endif
