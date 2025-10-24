#include <stdio.h>
#include "fonctions.h"

int main() {
    // Creation de l'arbre du jeu
    Node* root = createNode("Voulez-vous aller a gauche ?");
    root->left = createNode("Voulez-vous entrer dans la caverne ?");
    root->right = createNode("Voulez-vous traverser le pont ?");

    root->left->left = createNode("Vous trouvez un tresor !");
    root->left->right = createNode("Vous tombez dans un piege !");
    root->right->left = createNode("Vous trouvez un tresor !");
    root->right->right = createNode("Vous etes perdu dans la foret !");

    printf("Bienvenue dans le mini-jeu de l'arbre !\n");
    play(root);

    freeTree(root);
    return 0;
}
