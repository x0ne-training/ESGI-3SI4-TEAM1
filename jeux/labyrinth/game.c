#include <stdio.h>
#include "game.h"

void initializePlayer(Player *p) {
    p->x = 0;
    p->y = 0;
    p->health = 100;
}

void playTurn(Player *p, Maze *m) {
    char choice;
    printf("\nDéplacez-vous (Z=haut, S=bas, Q=gauche, D=droite) : ");
    scanf(" %c", &choice);

    int newX = p->x;
    int newY = p->y;

    switch (choice) {
        case 'Z': case 'z': newX--; break;
        case 'S': case 's': newX++; break;
        case 'Q': case 'q': newY--; break;
        case 'D': case 'd': newY++; break;
        default: printf("Choix invalide !\n"); return;
    }

    if (newX >= 0 && newX < m->rows && newY >= 0 && newY < m->cols && m->grid[newX][newY] != '#') {
        p->x = newX;
        p->y = newY;
        printf("Vous vous déplacez...\n");
    } else {
        printf("Vous heurtez un mur !\n");
    }
}

int isGameOver(Player *p, Maze *m) {
    return p->x == m->exitX && p->y == m->exitY;
}

void endGame(Player *p, Maze *m) {
    if (p->x == m->exitX && p->y == m->exitY) {
        printf("\nFélicitations ! Vous avez trouvé la sortie du labyrinthe !\n");
    } else {
        printf("\nGame Over !\n");
    }
}
