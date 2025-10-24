#include <stdio.h>
#include "fonctions.h"

int main() {
    // Création de l'arbre du jeu
    Node* root = createNode("Voulez-vous aller à gauche ?");
    root->left = createNode("Voulez-vous entrer dans la caverne ?");
    root->right = createNode("Voulez-vous traverser le pont ?");
