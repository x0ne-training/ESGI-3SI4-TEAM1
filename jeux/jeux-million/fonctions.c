#include "le-million.h"
#include <string.h>
#include <ctype.h>

static Question questions[MAX_QUESTIONS];
static int questions_count = 0;
static int jokers_used_5050 = 0, jokers_used_phone = 0, jokers_used_audience = 0;

void init_questions(void) {
    questions_count = 15;

    questions[0] = (Question){
            "Quelle est la capitale de la France ?",
            {"Lyon", "Marseille", "Paris", "Nice"},
            2
    };

    questions[1] = (Question){
            "Quel metal a pour symbole chimique 'Fe' ?",
            {"Fer", "Fluor", "Francium", "Fermium"},
            0
    };

    questions[2] = (Question){
            "Quel est le plus grand ocean sur Terre ?",
            {"Atlantique", "Indien", "Arctique", "Pacifique"},
            3
    };

    questions[3] = (Question){
            "Qui a peint la 'Joconde' ?",
            {"Michel-Ange", "Leonard de Vinci", "Raphael", "Donatello"},
            1
    };

    questions[4] = (Question){
            "Combien de joueurs y a-t-il dans une equipe de football (sur le terrain) ?",
            {"9", "10", "11", "12"},
            2
    };

    questions[5] = (Question){
            "Lequel de ces animaux est un marsupial ?",
            {"Ours", "Kangourou", "Loup", "Dauphin"},
            1
    };

    questions[6] = (Question){
            "Quel element est necessaire a la photosynthese ?",
            {"Azote", "Oxygene", "Carbone", "Lumiere"},
            3
    };

    questions[7] = (Question){
            "En informatique, que signifie 'CPU' ?",
            {"Central Processing Unit", "Computer Personal Unit", "Control Protocol Unit", "Central Program Unit"},
            0
    };

    questions[8] = (Question){
            "Quel pays a remporte la Coupe du Monde de football en 2018 ?",
            {"Bresil", "France", "Allemagne", "Espagne"},
            1
    };

    questions[9] = (Question){
            "Quel nombre est premier ?",
            {"21", "29", "27", "33"},
            1
    };

    questions[10] = (Question){
            "Quel est le plus long des fleuves suivants ?",
            {"Seine", "Nil", "Loire", "Rhone"},
            1
    };

    questions[11] = (Question){
            "Quelle planete est la plus proche du Soleil ?",
            {"Venus", "Mars", "Mercure", "Jupiter"},
            2
    };

    questions[12] = (Question){
            "Qui a ecrit 'Le Petit Prince' ?",
            {"Victor Hugo", "Antoine de Saint-Exupery", "Albert Camus", "Marcel Proust"},
            1
    };

    questions[13] = (Question){
            "Combien de couleurs y a-t-il dans un arc-en-ciel traditionnel ?",
            {"5", "6", "7", "8"},
            2
    };

    questions[14] = (Question){
            "Quelle unite mesure la frequence ?",
            {"Newton", "Watt", "Hertz", "Pascal"},
            2
    };
}

int get_questions_count(void) {
    return questions_count;
}

const Question* get_question(int idx) {
    if (idx < 0 || idx >= questions_count) return NULL;
    return &questions[idx];
}

int joker_5050(int qidx, int out_choices[]) {
    if (jokers_used_5050) return 0;
    const Question *q = get_question(qidx);
    if (!q) return 0;

    int good = q->correct;
    int bads[3], nb = 0;
    for (int i = 0; i < MAX_CHOICES; ++i) {
        if (i != good) bads[nb++] = i;
    }
    int r = rand() % nb;
    out_choices[0] = good;
    out_choices[1] = bads[r];
    jokers_used_5050 = 1;
    return 1;
}

void joker_phone(int qidx) {
    if (jokers_used_phone) {
        printf("Vous avez deja utilise l'appel a un ami.\n");
        return;
    }
    const Question *q = get_question(qidx);
    if (!q) return;
    printf("Vous appelez un ami...\n");
    int prob = (qidx < 8) ? 70 : 50;
    int r = rand() % 100;
    int guess;
    if (r < prob) guess = q->correct;
    else {
        int cand;
        do { cand = rand() % MAX_CHOICES; } while (cand == q->correct);
        guess = cand;
    }
    printf("Votre ami pense que la reponse est : %c) %s\n", 'A' + guess, q->choices[guess]);
    jokers_used_phone = 1;
}

void joker_audience(int qidx) {
    if (jokers_used_audience) {
        printf("Vous avez deja utilise le sondage du public.\n");
        return;
    }
    const Question *q = get_question(qidx);
    if (!q) return;
    printf("Le public vote...\n");
    int base;
    if (qidx < 6) base = 70;
    else if (qidx < 12) base = 55;
    else base = 40;

    int remaining = 100 - base;
    int p[4] = {0,0,0,0};
    p[q->correct] = base;
    int r1 = rand() % (remaining + 1);
    int r2 = rand() % (remaining + 1 - r1);
    p[(q->correct + 1) % 4] = r1;
    p[(q->correct + 2) % 4] = r2;
    p[(q->correct + 3) % 4] = remaining - r1 - r2;

    printf("Resultats du public :\n");
    for (int i = 0; i < 4; ++i) {
        printf(" %c) %s : %d%%\n", 'A'+i, q->choices[i], p[i]);
    }
    jokers_used_audience = 1;
}

void print_question(const Question *q, int removed_mask) {
    printf("\n%s\n", q->question);
    for (int i = 0; i < MAX_CHOICES; ++i) {
        if (removed_mask & (1 << i)) {
            printf(" %c) ---\n", 'A' + i);
        } else {
            printf(" %c) %s\n", 'A' + i, q->choices[i]);
        }
    }
}

int ask_user_choice(const Question *q, int removed_mask) {
    (void)q;
    char line[128];
    while (1) {
        printf("\nEntrez A/B/C/D pour repondre, J pour jokers, Q pour quitter : ");
        if (!fgets(line, sizeof(line), stdin)) return -3;
        char c = '\0';
        for (int i = 0; line[i]; ++i) {
            if (!isspace((unsigned char)line[i])) { c = toupper((unsigned char)line[i]); break; }
        }
        if (c == 'Q') return -1;
        if (c == 'J') return -2;
        if (c >= 'A' && c <= 'D') {
            int idx = c - 'A';
            if (removed_mask & (1 << idx)) {
                printf("Choix non disponible (selection retiree). Choisissez autre chose.\n");
                continue;
            }
            return idx;
        }
        printf("Entree invalide.\n");
    }
}
