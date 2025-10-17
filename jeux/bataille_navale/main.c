#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "fonctions.h"
#include "ai.h"

void placement_auto_ou_user(Case p[TAILLE][TAILLE], int joueur) {
    printf("\n--- Placement des bateaux joueur %d ---\n", joueur);
    for (int i=0;i<NB_BATEAUX;i++) {
        int t = BATEAUX[i].taille;
        if (joueur == 2) {
            while (!placer_bateau_alea(p, t)) {}
            continue;
        }
        bool ok=false;
        while (!ok) {
            afficher_plateau(p, false);
            printf("Placer %s (taille %d)\n", BATEAUX[i].nom, t);
            printf("Entrez x y direction (h=haut b=bas g=gauche d=droite). Exemple: 3 5 d\n> ");
            int x,y; char dir;
            if (scanf("%d %d %c", &x, &y, &dir) != 3) {
                clear_input_buffer();
                printf("Entrée invalide, recommencez.\n");
                continue;
            }
            clear_input_buffer();
            if (place_bateau_user(p, t, x, y, dir)) ok = true;
            else printf("Placement impossible. Recommencez.\n");
        }
    }
}

int main(void) {
    Case plateau1[TAILLE][TAILLE];
    Case plateau2[TAILLE][TAILLE];
    Case vue1[TAILLE][TAILLE];
    Case vue2[TAILLE][TAILLE];
    init_plateau(plateau1);
    init_plateau(plateau2);
    init_plateau(vue1);
    init_plateau(vue2);

    printf("=== Bataille Navale en C ===\n");
    printf("1) Joueur vs Joueur\n2) Joueur vs IA\nChoix: ");
    int mode = 0;
    if (scanf("%d", &mode) != 1) mode = 2;
    clear_input_buffer();

    ai_init();

    if (mode == 1) {
        placement_auto_ou_user(plateau1, 1);
        placement_auto_ou_user(plateau2, 1);
    } else {
        // joueur 1 manuel, joueur 2 IA
        placement_auto_ou_user(plateau1, 1);
        ai_place_ships(plateau2);
        printf("IA a placé ses bateaux.\n");
    }

    int tour = 1;
    bool joueur1tour = true;
    Point last_ai_shot = {-1,-1};

    while (1) {
        if (joueur1tour) {
            printf("\n--- Tour du Joueur 1 ---\n");
            printf("Votre plateau :\n"); afficher_plateau(plateau1, false);
            printf("Vue sur l'adversaire :\n"); afficher_plateau(vue1, false);
            printf("Entrez coordonnée à tirer x y: ");
            int x,y;
            if (scanf("%d %d", &x, &y) != 2) {
                clear_input_buffer();
                printf("Entrée invalide.\n");
                continue;
            }
            clear_input_buffer();
            if (!coord_valide(x,y)) { printf("Coordonnees invalides.\n"); continue; }
            if (vue1[x][y] == MANQUÉ || vue1[x][y] == TOUCHÉ || vue1[x][y] == COULÉ) {
                printf("Vous avez déjà tiré là.\n"); continue;
            }
            bool hit = tirer(plateau2, vue1, x, y);
            if (hit) {
                printf("Touché !\n");
            } else {
                printf("Manqué.\n");
            }
            if (tous_coulés(plateau2)) { printf("Joueur 1 gagne !\n"); break; }
            joueur1tour = false;
        } else {
            // tour du joueur 2 (IA ou humain)
            if (mode == 1) {
                printf("\n--- Tour du Joueur 2 ---\n");
                printf("Votre plateau :\n"); afficher_plateau(plateau2, false);
                printf("Vue sur l'adversaire :\n"); afficher_plateau(vue2, false);
                printf("Entrez coordonnée à tirer x y: ");
                int x,y;
                if (scanf("%d %d", &x, &y) != 2) {
                    clear_input_buffer();
                    printf("Entrée invalide.\n");
                    continue;
                }
                clear_input_buffer();
                if (!coord_valide(x,y)) { printf("Coordonnees invalides.\n"); continue; }
                if (vue2[x][y] == MANQUÉ || vue2[x][y] == TOUCHÉ || vue2[x][y] == COULÉ) {
                    printf("Vous avez déjà tiré là.\n"); continue;
                }
                bool hit = tirer(plateau1, vue2, x, y);
                if (hit) printf("Touché !\n"); else printf("Manqué.\n");
                if (tous_coulés(plateau1)) { printf("Joueur 2 gagne !\n"); break; }
            } else {
                Point p = ai_choose_shot(vue2);
                last_ai_shot = p;
                printf("\nIA tire en (%d, %d)\n", p.x, p.y);
                bool hit = tirer(plateau1, vue2, p.x, p.y);
                if (hit) { printf("IA a touché votre bateau !\n"); }
                else { printf("IA a manqué.\n"); }
                ai_report_result(p, hit);
                if (tous_coulés(plateau1)) { printf("L'IA gagne !\n"); break; }
            }
            joueur1tour = true;
        }
        tour++;
    }

    printf("Fin de la partie.\n");
    return 0;
}