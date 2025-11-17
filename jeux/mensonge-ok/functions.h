#ifndef FUNCTIONS_H
#define FUNCTIONS_H

// Pose une question et vérifie si le joueur ment correctement.
// question = texte affiché
// truth = 1 si la réponse vraie serait "YES", 0 sinon
// Retourne 1 si le joueur continue, 0 si il a perdu.
int ask(const char *question, int truth);


