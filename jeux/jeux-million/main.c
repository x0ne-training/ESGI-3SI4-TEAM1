#include "le-million.h"
#include <stdio.h>
#include <string.h>

static const int prizes[15] = {
        100, 200, 300, 500, 1000,        // palier 1-5
        2000, 4000, 8000, 16000, 32000,  // 6-10
        64000, 125000, 250000, 500000, 1000000 // 11-15
};

int main(void) {
    srand((unsigned int)time(NULL));
    init_questions();

    int total = get_questions_count();
    int current = 0;
    int secured_prize = 0; // palier securise (ex: apres Q5 et Q10)
    int used_5050 = 0, used_phone = 0, used_audience = 0;

    printf("Bienvenue dans 'Le million' !\n");
    printf("Repondez aux questions pour gagner de l'argent. Vous avez 3 jokers : 50/50, Appel a un ami, Sondage du public.\n");

    while (current < total) {
        const Question *q = get_question(current);
        int removed_mask = 0;
        int answered = 0;

        while (!answered) {
            print_question(q, removed_mask);
            int choice = ask_user_choice(q, removed_mask);
            if (choice == -1) {
                // quitter
                printf("Vous quittez avec %d euros.\n", (current == 0) ? 0 : prizes[current - 1]);
                return 0;
            } else if (choice == -2) {
                // jokers menu
                printf("\nJokers disponibles :\n");
                printf("1) 50/50 %s\n", used_5050 ? "(utilise)" : "");
                printf("2) Appel a un ami %s\n", used_phone ? "(utilise)" : "");
                printf("3) Sondage du public %s\n", used_audience ? "(utilise)" : "");
                printf("Choisissez 1/2/3 ou autre pour annuler : ");
                char line[32];
                if (!fgets(line, sizeof(line), stdin)) { printf("Erreur entree.\n"); continue; }
                int sel = line[0] - '0';
                if (sel == 1 && !used_5050) {
                    int out[2];
                    if (joker_5050(current, out)) {
                        // construire mask pour retirer les deux autres
                        removed_mask = 0;
                        for (int i = 0; i < 4; ++i) {
                            int keep = 0;
                            if (i == out[0] || i == out[1]) keep = 1;
                            if (!keep) removed_mask |= (1 << i);
                        }
                        used_5050 = 1;
                        printf("50/50 applique. Deux choix retires.\n");
                    } else printf("Impossible d'utiliser 50/50.\n");
                } else if (sel == 2 && !used_phone) {
                    joker_phone(current);
                    used_phone = 1;
                } else if (sel == 3 && !used_audience) {
                    joker_audience(current);
                    used_audience = 1;
                } else {
                    printf("Joker invalide ou deja utilise.\n");
                }
            } else if (choice >= 0 && choice < 4) {
                // verifier reponse
                if (choice == q->correct) {
                    printf("Bonne reponse ! Vous gagnez %d euros.\n", prizes[current]);
                    // palier securise
                    if (current == 4) secured_prize = prizes[4]; // apres Q5
                    if (current == 9) secured_prize = prizes[9]; // apres Q10
                    current++;
                    answered = 1;
                    if (current == total) {
                        printf("Felicitations ! Vous avez gagne 1 000 000 euros !\n");
                        return 0;
                    }
                } else {
                    printf("Mauvaise reponse. La bonne reponse etait %c) %s\n", 'A' + q->correct, q->choices[q->correct]);
                    printf("Vous repartez avec %d euros (palier securise).\n", secured_prize);
                    return 0;
                }
            } else {
                printf("Entree inconnue.\n");
            }
        } // fin while !answered
    } // fin while questions

    return 0;
}


