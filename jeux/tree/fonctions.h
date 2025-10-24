#ifndef FONCTIONS_H
#define FONCTIONS_H

typedef struct Node {
    char question[100];
    struct Node* left;
    struct Node* right;
} Node;

Node* createNode(char* question);
void play(Node* root);
void freeTree(Node* root);

#endif
