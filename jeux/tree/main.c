#include <stdio.h>
#include "fonctions.h"

int main() {
    // Création de l'arbre du jeu
    Node* root = createNode("Voulez-vous aller à gauche ?");
    root->left = createNode("Voulez-vous entrer dans la caverne ?");
    root->right = createNode("Voulez-vous traverser le pont ?");

    root->left->left = createNode("Vous trouvez un trésor !");
    root->left->right = createNode("Vous tombez dans un piège !");
    root->right->left = createNode("Vous trouvez un trésor !");
    root->right->right = createNode("Vous êtes perdu dans la forêt !");

    printf("Bienvenue dans le mini-jeu de l'arbre !\n");
    play(root);

    freeTree(root);
    return 0;
}
