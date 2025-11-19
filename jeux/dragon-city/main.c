#include <stdio.h>
#include <string.h>
#include "functions.h"

void print_menu(void) {
    printf("\n--- Dragon Mini (console) ---\n");
    printf("1) Lister mes dragons\n");
    printf("2) Élever un nouveau dragon\n");
    printf("3) Nourrir un dragon (5 or)\n");
    printf("4) Entraîner un dragon (10 or)\n");
    printf("5) Faire combattre un dragon contre un monstre\n");
    printf("6) Passer au jour suivant\n");
    printf("7) Afficher infos du jeu\n");
    printf("0) Quitter\n");
    printf("Choix : ");
}

int main(void) {
    GameState game;
    init_game(&game);

    printf("Bienvenue dans Dragon Mini !\n");
    int choice;

    while (1) {
        print_menu();
        choice = read_int_range(0, 7);
        if (choice == 0) {
            printf("Au revoir !\n");
            break;
        }

        int idx;
        char name[NAME_LEN];
        switch (choice) {
            case 1:
                list_dragons(&game);
                break;
            case 2:
                if (game.count >= MAX_DRAGONS) {
                    printf("Tu as atteint le nombre maximum de dragons (%d).\n", MAX_DRAGONS);
                    break;
                }
                printf("Donne un nom au nouveau dragon : ");
                if (fgets(name, sizeof(name), stdin) == NULL) {
                    clear_input();
                    printf("Erreur lecture nom.\n");
                    break;
                }
                // enlever le \n
                name[strcspn(name, "\n")] = '\0';
                if (strlen(name) == 0) {
                    printf("Nom vide, annulation.\n");
                    break;
                }
                if (add_dragon(&game, name)) {
                    printf("Dragon '%s' ajouté !\n", name);
                } else {
                    printf("Impossible d'ajouter le dragon.\n");
                }
                break;
            case 3:
                list_dragons(&game);
                if (game.count == 0) break;
                printf("Quel dragon nourrir (numéro) ? ");
                idx = read_int_range(1, game.count) - 1;
                feed_dragon(&game, idx);
                break;
            case 4:
                list_dragons(&game);
                if (game.count == 0) break;
                printf("Quel dragon entraîner (numéro) ? ");
                idx = read_int_range(1, game.count) - 1;
                train_dragon(&game, idx);
                break;
            case 5:
                list_dragons(&game);
                if (game.count == 0) break;
                printf("Quel dragon combattre (numéro) ? ");
                idx = read_int_range(1, game.count) - 1;
                battle_random(&game, idx);
                break;
            case 6:
                pass_day(&game);
                break;
            case 7:
                printf("Jour: %d | Or: %d | Nombre de dragons: %d\n", game.day, game.gold, game.count);
                break;
            default:
                printf("Choix non géré.\n");
                break;
        }
    }

    return 0;
}
