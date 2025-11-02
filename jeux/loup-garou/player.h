#ifndef PLAYER_H
#define PLAYER_H

typedef enum { VILLAGEOIS, LOUP, VOYANTE, CHASSEUR } Role;

typedef struct {
    char name[50];
    Role role;
    int alive; // 1 = vivant, 0 = mort
} Player;

#endif
