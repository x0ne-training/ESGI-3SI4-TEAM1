#ifndef GAME_H
#define GAME_H

typedef struct {
    int tir;
    int passe;
    int dribble;
    int endurance;
} Player;

int action_success(int skill);
void print_stats(Player p);
int get_player_choice();
void apply_choice(int choice, Player *player, Player *adversaire, int *score_player, int *score_adv);

#endif
