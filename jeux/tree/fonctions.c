#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fonctions.h"

Node* createNode(char* question) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    strcpy(newNode->question, question);
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void play(Node* root) {
    Node* current = root;
    char choice[10];

    while (current != NULL) {
        printf("%s (oui/non) : ", current->question);
        scanf("%s", choice);

        if (strcmp(choice, "oui") == 0) {
            if (current->left != NULL) {
                current = current->left;
            } else {
                printf("Félicitations ! Vous avez trouvé le trésor !\n");
                break;
            }
        } else if (strcmp(choice, "non") == 0) {
            if (current->right != NULL) {
                current = current->right;
            } else {
                printf("Dommage ! Vous avez perdu !\n");
                break;
            }
        } else {
            printf("Veuillez répondre par 'oui' ou 'non'.\n");
        }
    }
}


